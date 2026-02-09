#!/bin/bash

# Configuration
CONFIG_FILE="skills_sources.json"
TARGET_SOURCE=$1

# Check requirements
if ! command -v jq &> /dev/null; then
    echo "Error: jq is required but not installed. Please install it (e.g., brew install jq)."
    exit 1
fi

if ! command -v git &> /dev/null; then
    echo "Error: git is required but not installed."
    exit 1
fi

if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Configuration file '$CONFIG_FILE' not found."
    exit 1
fi

# Filter configuration
if [ -n "$TARGET_SOURCE" ]; then
    # Create temp file for filtered config
    ACTIVE_CONFIG=$(mktemp)
    jq --arg name "$TARGET_SOURCE" '[.[] | select(.name == $name)]' "$CONFIG_FILE" > "$ACTIVE_CONFIG"
    
    # Check if we found it
    count=$(jq '. | length' "$ACTIVE_CONFIG")
    if [ "$count" -eq 0 ]; then
        echo "Error: Source '$TARGET_SOURCE' not found in $CONFIG_FILE"
        rm "$ACTIVE_CONFIG"
        exit 1
    fi
    echo "🎯 Targeting single source: $TARGET_SOURCE"
else
    # Use all sources
    ACTIVE_CONFIG="$CONFIG_FILE"
fi

# Create a temporary directory for git operations
TEMP_DIR=$(mktemp -d)

cleanup() {
  rm -rf "$TEMP_DIR"
  # Only remove ACTIVE_CONFIG if it's a temporary file (when TARGET_SOURCE is set)
  if [ -n "$TARGET_SOURCE" ] && [ -f "$ACTIVE_CONFIG" ]; then
    rm "$ACTIVE_CONFIG"
  fi
}
trap cleanup EXIT

# Get the number of skills
count=$(jq '. | length' "$ACTIVE_CONFIG")

echo "Found $count skills to sync."
echo ""

# Loop through each skill
for ((i=0; i<count; i++)); do
    # Extract skill details using ACTIVE_CONFIG
    name=$(jq -r ".[$i].name" "$ACTIVE_CONFIG")
    repo_url=$(jq -r ".[$i].repo_url" "$ACTIVE_CONFIG")
    branch=$(jq -r ".[$i].branch // \"main\"" "$ACTIVE_CONFIG")

    echo "🔄 Syncing skill: $name from $repo_url ($branch)..."

    # Clone the repository
    # Use a subdirectory in temp for this skill
    SKILL_TEMP="$TEMP_DIR/$name"
    rm -rf "$SKILL_TEMP"
    
    echo "  Cloning to temporary directory..."
    if ! git clone --quiet --depth 1 --branch "$branch" "$repo_url" "$SKILL_TEMP"; then
        echo "  ❌ Failed to clone $name"
        continue
    fi

    # Get the number of copy rules
    rule_count=$(jq ".[$i].copy_rules | length" "$ACTIVE_CONFIG")

    for ((j=0; j<rule_count; j++)); do
        source_sub=$(jq -r ".[$i].copy_rules[$j].source // \".\"" "$ACTIVE_CONFIG")
        dest_sub=$(jq -r ".[$i].copy_rules[$j].dest" "$ACTIVE_CONFIG")

        if [ "$dest_sub" == "null" ] || [ -z "$dest_sub" ]; then
            echo "  ⚠️ Skipping rule without destination for $name"
            continue
        fi
        
        # Absolute path for source in temp
        # Removing leading ./ from source_sub if present to avoid path issues
        clean_source_sub=${source_sub#./}
        source_path="$SKILL_TEMP/$clean_source_sub"
        
        if [ ! -e "$source_path" ]; then
            echo "  ❌ Source path does not exist in repo: $source_sub"
            continue
        fi

        echo "  Copying from '$source_sub' to '$dest_sub'..."
        
        # Create destination directory
        mkdir -p "$dest_sub"

        # Read includes and excludes into arrays from ACTIVE_CONFIG
        includes_json=$(jq -r ".[$i].copy_rules[$j].include[]?" "$ACTIVE_CONFIG")
        excludes_json=$(jq -r ".[$i].copy_rules[$j].exclude[]?" "$ACTIVE_CONFIG")
        rsync_opts="-a"

        # Build exclude arguments
        exclude_args=()
        if [ -n "$excludes_json" ]; then
            while IFS= read -r exc; do
                if [ -n "$exc" ]; then
                    exclude_args+=(--exclude "$exc")
                fi
            done <<< "$excludes_json"
        fi

        # Perform the copy
        if [ -d "$source_path" ]; then
            if [ -n "$includes_json" ]; then
                # Explicit includes: Copy only specific items found in source_path
                sources_to_copy=()
                while IFS= read -r inc; do
                   if [ -n "$inc" ]; then
                        # Remove leading slash if present
                        clean_inc=${inc#/}
                        item_path="$source_path/$clean_inc"
                        if [ -e "$item_path" ]; then
                            sources_to_copy+=("$item_path")
                        else
                            echo "  ⚠️ Included item not found: $inc"
                        fi
                   fi
                done <<< "$includes_json"

                if [ ${#sources_to_copy[@]} -gt 0 ]; then
                    rsync $rsync_opts "${exclude_args[@]}" "${sources_to_copy[@]}" "$dest_sub/"
                else
                    echo "  ⚠️ No valid items found to include for $name"
                fi
            else
                # Default: Copy everything from source directory
                rsync $rsync_opts "${exclude_args[@]}" "$source_path/" "$dest_sub/"
            fi
        else
            # File copy
            cp "$source_path" "$dest_sub/"
        fi
        
        echo "  ✅ Copied successfully."
    done

    echo "✅ Finished syncing $name."
    echo ""
done