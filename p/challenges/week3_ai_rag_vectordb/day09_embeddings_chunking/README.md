# Day 09: Text Chunking Strategies & Vector Embeddings

## 💡 Concept Overview
Preparing documents for RAG requires breaking raw text into semantic chunks and encoding them into high-dimensional vector representations. If chunks are too small, context is lost; if too large, vector similarity degrades due to noise.

## 🎯 Backend Scenario
Build a production text chunker and vector similarity calculator:
1. `recursive_text_chunker(text: str, chunk_size: int = 100, chunk_overlap: int = 20, separators: List[str] = None) -> List[str]`: Recursively splits document text preserving paragraph/sentence boundaries.
2. `cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float`: Computes mathematical dot product cosine distance between two embedding vectors.

## 🛠️ Instructions
1. Implement logic in `starter.py`.
2. Run tests:
   ```bash
   python daily_push.py --test 9
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 9
   ```
