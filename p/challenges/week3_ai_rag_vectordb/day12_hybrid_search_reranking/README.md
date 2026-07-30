# Day 12: Hybrid Search (BM25 + Vector) & Reciprocal Rank Fusion

## 💡 Concept Overview
Dense vector search excels at conceptual semantic similarity, but can miss exact keyword matches (e.g. error codes, product SKUs). Sparse BM25 search excels at exact keyword matching. Combining dense + sparse search with Reciprocal Rank Fusion (RRF) delivers state-of-the-art retrieval accuracy.

## 🎯 Backend Scenario
Build `HybridSearchEngine`:
1. `compute_bm25_score(query: str, text: str) -> float`: Computes sparse term frequency keyword match score.
2. `reciprocal_rank_fusion(dense_ranks: List[str], sparse_ranks: List[str], k: int = 60) -> List[Tuple[str, float]]`: Combines ranking lists via RRF formula: $RRF(d) = \sum \frac{1}{k + r(d)}$.

## 🛠️ Instructions
1. Implement hybrid search in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 12
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 12
   ```
