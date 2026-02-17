---
name: memory-systems
description: >
  Guides implementation of agent memory systems, compares production frameworks
  (Mem0, Zep/Graphiti, Letta, LangMem), and designs persistence architectures
  for cross-session knowledge retention. Use when the user asks to "implement
  agent memory", "persist state across sessions", "build knowledge graph for agents",
  "track entities over time", "add long-term memory", "choose a memory framework",
  or mentions temporal knowledge graphs, vector stores, entity memory, or memory
  benchmarks (LoCoMo, LongMemEval).
---

# Memory System Design

Memory provides the persistence layer that allows agents to maintain continuity across sessions and reason over accumulated knowledge. Simple agents rely entirely on context for memory, losing all state when sessions end. Sophisticated agents implement layered memory architectures that balance immediate context needs with long-term knowledge retention. The evolution from vector stores to knowledge graphs to temporal knowledge graphs represents increasing investment in structured memory for improved retrieval and reasoning.

## When to Activate

Activate this skill when:
- Building agents that must persist knowledge across sessions
- Choosing between memory frameworks (Mem0, Zep/Graphiti, Letta, LangMem)
- Needing to maintain entity consistency across conversations
- Implementing reasoning over accumulated knowledge
- Designing memory architectures that scale in production
- Evaluating memory systems against benchmarks (LoCoMo, LongMemEval, DMR)

## Core Concepts

Memory spans a spectrum from volatile context window to persistent storage. Key insight from benchmarks: **tool complexity matters less than reliable retrieval** — Letta's filesystem agents scored 74% on LoCoMo using basic file operations, beating Mem0's specialized tools at 68.5%. Start simple, add structure (graphs, temporal validity) only when retrieval quality demands it.

## Detailed Topics

### Production Framework Landscape

| Framework | Architecture | Best For | Trade-off |
|-----------|-------------|----------|-----------|
| **Mem0** | Vector store + graph memory, pluggable backends | Multi-tenant systems, broad integrations | Less specialized for multi-agent |
| **Zep/Graphiti** | Temporal knowledge graph, bi-temporal model | Enterprise requiring relationship modeling + temporal reasoning | Advanced features cloud-locked |
| **Letta** | Self-editing memory with tiered storage (in-context/core/archival) | Full agent introspection, stateful services | Complexity for simple use cases |
| **LangMem** | Memory tools for LangGraph workflows | Teams already on LangGraph | Tightly coupled to LangGraph |
| **File-system** | Plain files with naming conventions | Simple agents, prototyping | No semantic search, no relationships |

Zep's Graphiti engine builds a three-tier knowledge graph (episode, semantic entity, community subgraphs) with a bi-temporal model tracking both when events occurred and when they were ingested. Mem0 offers the fastest path to production with managed infrastructure. Letta provides the deepest agent control through its Agent Development Environment.

**Benchmark Performance Comparison**

| System | DMR Accuracy | LoCoMo | Latency |
|--------|-------------|--------|---------|
| Zep (Temporal KG) | 94.8% | — | 2.58s |
| Letta (filesystem) | — | 74.0% | — |
| Mem0 | — | 68.5% | — |
| MemGPT | 93.4% | — | Variable |
| GraphRAG | ~75-85% | — | Variable |
| Vector RAG baseline | ~60-70% | — | Fast |

Zep achieves up to 18.5% accuracy improvement on LongMemEval while reducing latency by 90%. Key insight: Letta's filesystem-based agents achieved 74% on LoCoMo using basic file operations, outperforming specialized memory tools — tool complexity matters less than reliable retrieval.

### Memory Layers (Decision Points)

| Layer | Persistence | Implementation | When to Use |
|-------|------------|----------------|-------------|
| **Working** | Context window only | Scratchpad in system prompt | Always — optimize with attention-favored positions |
| **Short-term** | Session-scoped | File-system, in-memory cache | Intermediate tool results, conversation state |
| **Long-term** | Cross-session | Key-value store → graph DB | User preferences, domain knowledge, entity registries |
| **Entity** | Cross-session | Entity registry + properties | Maintaining identity ("John Doe" = same person across conversations) |
| **Temporal KG** | Cross-session + history | Graph with validity intervals | Facts that change over time, time-travel queries, preventing context clash |

### Retrieval Strategies

| Strategy | Use When | Limitation |
|----------|----------|------------|
| **Semantic** (embedding similarity) | Direct factual queries | Degrades on multi-hop reasoning |
| **Entity-based** (graph traversal) | "Tell me everything about X" | Requires graph structure |
| **Temporal** (validity filter) | Facts change over time | Requires validity metadata |
| **Hybrid** (semantic + keyword + graph) | Best overall accuracy | Most infrastructure |

Zep's hybrid approach achieves 90% latency reduction (2.58s vs 28.9s) by retrieving only relevant subgraphs.

### Memory Consolidation

Consolidate periodically to prevent unbounded growth. **Invalidate but don't discard** — preserving history matters for temporal queries. Trigger on memory count thresholds, degraded retrieval quality, or scheduled intervals. See [implementation reference](./references/implementation.md) for working consolidation code.

## Practical Guidance

### Choosing a Memory Architecture

**Start simple, add complexity only when retrieval fails.** Most agents don't need a temporal knowledge graph on day one.

1. **Prototype**: File-system memory. Store facts as structured JSON with timestamps. Good enough to validate agent behavior.
2. **Scale**: Move to Mem0 or vector store with metadata when you need semantic search and multi-tenant isolation.
3. **Complex reasoning**: Add Zep/Graphiti when you need relationship traversal, temporal validity, or cross-session synthesis.
4. **Full control**: Use Letta when you need agent self-management of memory with deep introspection.

### Integration with Context

Memories must integrate with context systems to be useful. Use just-in-time memory loading to retrieve relevant memories when needed. Use strategic injection to place memories in attention-favored positions (beginning/end of context).

### Error Recovery

- **Empty retrieval**: Fall back to broader search (remove entity filter, widen time range). If still empty, prompt user for clarification.
- **Stale results**: Check `valid_until` timestamps. If most results are expired, trigger consolidation before retrying.
- **Conflicting facts**: Prefer the fact with the most recent `valid_from`. Surface the conflict to the user if confidence is low.
- **Storage failure**: Queue writes for retry. Never block the agent's response on a memory write.

### Anti-Patterns

- **Stuffing everything into context**: Long inputs are expensive and degrade performance. Use just-in-time retrieval.
- **Ignoring temporal validity**: Facts go stale. Without validity tracking, outdated information poisons context.
- **Over-engineering early**: A filesystem agent can outperform complex memory tooling. Add sophistication when simple approaches fail.
- **No consolidation strategy**: Unbounded memory growth degrades retrieval quality over time.

## Examples

**Example 1: Mem0 Integration**
```python
from mem0 import Memory

m = Memory()
m.add("User prefers dark mode and Python 3.12", user_id="alice")
m.add("User switched to light mode", user_id="alice")

# Retrieves current preference (light mode), not outdated one
results = m.search("What theme does the user prefer?", user_id="alice")
```

**Example 2: Temporal Query**
```python
# Track entity with validity periods
graph.create_temporal_relationship(
    source_id=user_node,
    rel_type="LIVES_AT",
    target_id=address_node,
    valid_from=datetime(2024, 1, 15),
    valid_until=datetime(2024, 9, 1),  # moved out
)

# Query: Where did user live on March 1, 2024?
results = graph.query_at_time(
    {"type": "LIVES_AT", "source_label": "User"},
    query_time=datetime(2024, 3, 1)
)
```

## Guidelines

1. Start with file-system memory; add complexity only when retrieval quality demands it
2. Track temporal validity for any fact that can change over time
3. Use hybrid retrieval (semantic + keyword + graph) for best accuracy
4. Consolidate memories periodically — invalidate but don't discard
5. Design for retrieval failure: always have a fallback when memory lookup returns nothing
6. Consider privacy implications of persistent memory (retention policies, deletion rights)
7. Benchmark your memory system against LoCoMo or LongMemEval before and after changes
8. Monitor memory growth and retrieval latency in production

## Integration

This skill builds on context-fundamentals. It connects to:

- multi-agent-patterns - Shared memory across agents
- context-optimization - Memory-based context loading
- evaluation - Evaluating memory quality

## References

Internal reference:
- [Implementation Reference](./references/implementation.md) - Detailed implementation patterns

Related skills in this collection:
- context-fundamentals - Context basics
- multi-agent-patterns - Cross-agent memory

External resources:
- Zep temporal knowledge graph paper (arXiv:2501.13956)
- Mem0 production architecture paper (arXiv:2504.19413)
- LoCoMo benchmark (Snap Research)
- MemBench evaluation framework (ACL 2025)
- Graphiti open-source temporal KG engine (github.com/getzep/graphiti)

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2026-02-12
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 2.0.0
