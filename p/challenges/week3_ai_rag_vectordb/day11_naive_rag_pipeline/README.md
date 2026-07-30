# Day 11: End-to-End Naive RAG Pipeline

## 💡 Concept Overview
Retrieval-Augmented Generation (RAG) augments Large Language Model (LLM) prompts with authoritative context retrieved from domain-specific vector stores.

## 🎯 Backend Scenario
Build `RAGPipeline`:
1. `index_knowledge(documents: List[Dict[str, Any]])`: Embeds and indexes documents into the vector store.
2. `query(user_query: str, mock_llm_callable: Callable) -> Dict[str, Any]`:
   - Retrieves top matching contexts.
   - Constructs grounded prompt: `"Answer using context:\n{context}\n\nQuestion: {query}"`.
   - Invokes LLM callable and returns `{"answer": str, "retrieved_contexts": List[str], "prompt": str}`.

## 🛠️ Instructions
1. Implement in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 11
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 11
   ```
