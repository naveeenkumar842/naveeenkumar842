# Day 15: Self-Corrective Agentic RAG (Corrective RAG / Self-RAG)

## 💡 Concept Overview
Standard RAG fails when retrieved documents are irrelevant or contain hallucinations. Self-Corrective Agentic RAG evaluates retrieved context quality, rewrites unhelpful queries, and triggers web search fallbacks to ensure high-accuracy responses.

## 🎯 Backend Scenario
Build `SelfCorrectiveRAGAgent`:
1. `grade_document_relevance(query: str, doc_text: str) -> bool`: Evaluates document relevance to the query.
2. `generate_and_check_hallucination(query: str, context: str, mock_llm: Callable) -> Dict[str, Any]`:
   - Generates answer.
   - Verifies whether answer is grounded in retrieved context (`is_grounded: bool`).
   - If not grounded or unhelpful, rewrites query (`rewritten_query`) and retries retrieval.

## 🛠️ Instructions
1. Implement Self-RAG agent in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 15
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 15
   ```
