"""
Memory System Implementation

This module provides utilities for implementing memory systems.
"""

import numpy as np
from typing import List, Dict, Any, Optional
import json
import hashlib
from datetime import datetime


class VectorStore:
    """Simple vector store with metadata indexing."""
    
    def __init__(self, dimension: int = 768):
        self.dimension = dimension
        self.vectors: List[np.ndarray] = []
        self.metadata: List[Dict] = []
        self.entity_index: Dict[str, List[int]] = {}
        self.time_index: Dict[str, List[int]] = {}
    
    def add(self, text: str, metadata: Dict[str, Any] = None) -> int:
        """Add document to store."""
        metadata = metadata or {}
        embedding = self._embed(text)
        index = len(self.vectors)

        self.vectors.append(embedding)
        self.metadata.append(metadata)

        # Index by entity
        if "entity" in metadata:
            entity = metadata["entity"]
            if entity not in self.entity_index:
                self.entity_index[entity] = []
            self.entity_index[entity].append(index)
        
        # Index by time
        if "valid_from" in metadata:
            time_key = self._time_key(metadata["valid_from"])
            if time_key not in self.time_index:
                self.time_index[time_key] = []
            self.time_index[time_key].append(index)
        
        return index
    
    def search(self, query: str, limit: int = 5, 
               filters: Dict[str, Any] = None) -> List[Dict]:
        """Search for similar documents."""
        query_embedding = self._embed(query)
        
        scores = []
        for i, vec in enumerate(self.vectors):
            score = np.dot(query_embedding, vec) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(vec) + 1e-8
            )
            
            # Apply filters
            if filters and not self._matches_filters(self.metadata[i], filters):
                score = -1
            
            scores.append((i, score))
        
        scores.sort(key=lambda x: x[1], reverse=True)
        
        results = []
        for idx, score in scores[:limit]:
            if score > 0:
                results.append({
                    "index": idx,
                    "score": score,
                    "text": self.metadata[idx].get("text", ""),
                    "metadata": self.metadata[idx]
                })
        
        return results
    
    def search_by_entity(self, entity: str, query: str = "", 
                         limit: int = 5) -> List[Dict]:
        """Search within specific entity."""
        indices = self.entity_index.get(entity, [])
        
        if not indices:
            return []
        
        if query:
            query_embedding = self._embed(query)
            scored = []
            for i in indices:
                vec = self.vectors[i]
                score = np.dot(query_embedding, vec) / (
                    np.linalg.norm(query_embedding) * np.linalg.norm(vec) + 1e-8
                )
                scored.append((i, score, self.metadata[i]))
            
            scored.sort(key=lambda x: x[1], reverse=True)
            return [{"index": i, "score": s, "metadata": m} 
                    for i, s, m in scored[:limit]]
        else:
            return [{"index": i, "score": 1.0, "metadata": self.metadata[i]} 
                    for i in indices[:limit]]
    
    def _embed(self, text: str) -> np.ndarray:
        """Generate embedding for text."""
        # In production, use actual embedding model
        np.random.seed(hash(text) % (2**32))
        return np.random.randn(self.dimension)
    
    def _time_key(self, timestamp: Any) -> str:
        """Create time key for indexing."""
        if isinstance(timestamp, datetime):
            return timestamp.strftime("%Y-%m")
        return str(timestamp)
    
    def _matches_filters(self, metadata: Dict, filters: Dict) -> bool:
        """Check if metadata matches filters."""
        for key, value in filters.items():
            if key not in metadata:
                return False
            if isinstance(value, list):
                if metadata[key] not in value:
                    return False
            elif metadata[key] != value:
                return False
        return True


class PropertyGraph:
    """Simple property graph storage."""

    def __init__(self):
        self.nodes: Dict[str, Dict] = {}
        self.edges: Dict[str, Dict] = {}
        self.entity_registry: Dict[str, str] = {}  # name -> node_id
        self.node_index: Dict[str, List[str]] = {}  # label -> node_ids
        self.edge_index: Dict[str, List[str]] = {}  # type -> edge_ids

    def get_or_create_node(self, name: str, label: str = "Entity",
                           properties: Dict = None) -> str:
        """Get existing node by name, or create a new one.
        Uses entity_registry to maintain identity across interactions."""
        if name in self.entity_registry:
            node_id = self.entity_registry[name]
            if properties:
                self.nodes[node_id]["properties"].update(properties)
            return node_id
        node_id = self.create_node(label, {**(properties or {}), "name": name})
        self.entity_registry[name] = node_id
        return node_id

    def create_node(self, label: str, properties: Dict = None) -> str:
        """Create node with label and properties."""
        import time
        node_id = hashlib.md5(f"{label}{time.time()}".encode()).hexdigest()[:16]
        
        self.nodes[node_id] = {
            "id": node_id,
            "label": label,
            "properties": properties or {},
            "created_at": time.time()
        }
        
        if label not in self.node_index:
            self.node_index[label] = []
        self.node_index[label].append(node_id)
        
        return node_id
    
    def create_relationship(self, source_id: str, rel_type: str, 
                           target_id: str, properties: Dict = None) -> str:
        """Create directed relationship between nodes."""
        import time
        if source_id not in self.nodes:
            raise ValueError(f"Unknown source node: {source_id}")
        if target_id not in self.nodes:
            raise ValueError(f"Unknown target node: {target_id}")
        
        edge_id = hashlib.md5(f"{source_id}{rel_type}{target_id}{time.time()}".encode()).hexdigest()[:16]
        
        self.edges[edge_id] = {
            "id": edge_id,
            "source": source_id,
            "target": target_id,
            "type": rel_type,
            "properties": properties or {},
            "created_at": time.time()
        }
        
        if rel_type not in self.edge_index:
            self.edge_index[rel_type] = []
        self.edge_index[rel_type].append(edge_id)
        
        return edge_id
    
    def query(self, pattern: Dict) -> List[Dict]:
        """Query graph with simple pattern matching."""
        results = []
        
        # Match by edge type
        if "type" in pattern:
            edge_ids = self.edge_index.get(pattern["type"], [])
            for eid in edge_ids:
                edge = self.edges[eid]
                source = self.nodes.get(edge["source"], {})
                target = self.nodes.get(edge["target"], {})
                
                # Match source label
                if "source_label" in pattern:
                    if source.get("label") != pattern["source_label"]:
                        continue
                
                # Match target label
                if "target_label" in pattern:
                    if target.get("label") != pattern["target_label"]:
                        continue
                
                results.append({
                    "source": source,
                    "edge": edge,
                    "target": target
                })
        
        return results
    
    def get_node(self, node_id: str) -> Optional[Dict]:
        """Get node by ID."""
        return self.nodes.get(node_id)
    
    def get_relationships(self, node_id: str, 
                          direction: str = "both") -> List[Dict]:
        """Get relationships for a node."""
        relationships = []
        
        for edge in self.edges.values():
            if direction in ["outgoing", "both"] and edge["source"] == node_id:
                relationships.append({
                    "edge": edge,
                    "target": self.nodes.get(edge["target"]),
                    "direction": "outgoing"
                })
            if direction in ["incoming", "both"] and edge["target"] == node_id:
                relationships.append({
                    "edge": edge,
                    "source": self.nodes.get(edge["source"]),
                    "direction": "incoming"
                })
        
        return relationships


class TemporalKnowledgeGraph(PropertyGraph):
    """Property graph with temporal validity for facts."""
    
    def create_temporal_relationship(
        self, 
        source_id: str, 
        rel_type: str, 
        target_id: str,
        valid_from: datetime,
        valid_until: Optional[datetime] = None,
        properties: Dict = None
    ) -> str:
        """Create relationship with temporal validity."""
        edge_id = super().create_relationship(
            source_id, rel_type, target_id, properties
        )
        
        # Add temporal properties
        self.edges[edge_id]["valid_from"] = valid_from.isoformat()
        self.edges[edge_id]["valid_until"] = (
            valid_until.isoformat() if valid_until else None
        )
        
        return edge_id
    
    def query_at_time(self, query: Dict, query_time: datetime) -> List[Dict]:
        """Query graph state at specific time."""
        results = []
        
        # Get base query results
        base_results = self.query(query)
        
        for result in base_results:
            edge = result["edge"]
            valid_from = datetime.fromisoformat(edge.get("valid_from", "1970-01-01"))
            valid_until = edge.get("valid_until")
            
            # Check temporal validity
            if valid_from <= query_time:
                if valid_until is None or datetime.fromisoformat(valid_until) > query_time:
                    results.append({
                        **result,
                        "valid_from": valid_from,
                        "valid_until": valid_until
                    })
        
        return results
    
    def query_time_range(self, query: Dict, 
                         start_time: datetime, 
                         end_time: datetime) -> List[Dict]:
        """Query facts valid during time range."""
        results = []
        
        base_results = self.query(query)
        
        for result in base_results:
            edge = result["edge"]
            valid_from = datetime.fromisoformat(edge.get("valid_from", "1970-01-01"))
            valid_until = edge.get("valid_until")
            
            # Check if overlaps with query range
            until_dt = datetime.fromisoformat(valid_until) if valid_until else datetime.max
            
            if until_dt >= start_time and valid_from <= end_time:
                results.append({
                    **result,
                    "valid_from": valid_from,
                    "valid_until": valid_until
                })
        
        return results


# Memory System Integration

class IntegratedMemorySystem:
    """Integrated memory system combining vector store and graph."""
    
    def __init__(self):
        self.vector_store = VectorStore()
        self.graph = TemporalKnowledgeGraph()
        self.session_id: str = ""
    
    def start_session(self, session_id: str):
        """Start a new memory session."""
        self.session_id = session_id
    
    def store_fact(self, fact: str, entity: str,
                   timestamp: datetime = None,
                   relationships: List[Dict] = None):
        """Store a fact with entity and relationships."""
        # Store in vector store
        self.vector_store.add(fact, {
            "text": fact,
            "entity": entity,
            "valid_from": (timestamp or datetime.now()).isoformat(),
            "session_id": self.session_id
        })

        # Get or create entity node (uses registry for identity)
        entity_node_id = self.graph.get_or_create_node(entity)

        # Create relationships
        if relationships:
            for rel in relationships:
                target_node_id = self.graph.get_or_create_node(rel["target"])
                self.graph.create_relationship(
                    entity_node_id,
                    rel["type"],
                    target_node_id,
                    properties=rel.get("properties", {})
                )
    
    def retrieve_memories(self, query: str, 
                          entity_filter: str = None,
                          time_filter: Dict = None,
                          limit: int = 5) -> List[Dict]:
        """Retrieve memories matching query."""
        # Vector search
        filters = {"session_id": self.session_id}
        if entity_filter:
            filters["entity"] = entity_filter
        
        results = self.vector_store.search(query, limit=limit, filters=filters)
        
        # Enrich with graph relationships
        for result in results:
            entity = result["metadata"].get("entity")
            if entity:
                node_id = self.graph.entity_registry.get(entity)
                if node_id:
                    result["relationships"] = self.graph.get_relationships(node_id)
        
        return results
    
    def retrieve_entity_context(self, entity: str) -> Dict:
        """Retrieve complete context for an entity."""
        node_id = self.graph.entity_registry.get(entity)

        # Get entity node
        entity_node = self.graph.get_node(node_id) if node_id else None

        # Get relationships
        relationships = self.graph.get_relationships(node_id) if node_id else []

        # Get vector memories
        memories = self.vector_store.search_by_entity(entity, limit=10)

        return {
            "entity": entity_node,
            "relationships": relationships,
            "memories": memories
        }
    
    def consolidate(self):
        """Consolidate memories and remove outdated information."""
        # In production, implement actual consolidation logic
        # - Merge related facts
        # - Update validity periods
        # - Archive obsolete facts
        pass
