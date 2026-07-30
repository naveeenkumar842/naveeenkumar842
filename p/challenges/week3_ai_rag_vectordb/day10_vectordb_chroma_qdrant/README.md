# Day 10: Vector DB Indexing & Metadata Filtering Engine

## 💡 Concept Overview
Vector databases (Chroma, Qdrant, Milvus, Pinecone) index dense vector embeddings to perform Approximate Nearest Neighbor (ANN) search along with structured metadata filters (e.g. `category == 'backend'`).

## 🎯 Backend Scenario
Build a lightweight `VectorDBEngine`:
1. `add_document(doc_id: str, text: str, embedding: List[float], metadata: Dict[str, Any])`: Stores vector document.
2. `search(query_vector: List[float], top_k: int = 3, filter_metadata: Dict[str, Any] = None) -> List[Dict[str, Any]]`:
   - Filters candidate documents matching `filter_metadata`.
   - Computes vector cosine similarity and returns top `top_k` documents sorted by score descending.

## 🛠️ Instructions
1. Implement vector database engine in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 10
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 10
   ```
