# Day 17: RAG Evaluation Framework (Faithfulness & Relevance)

## 💡 Concept Overview
Deploying LLM RAG pipelines without automated evaluation leads to silent regressions in production. RAG evaluation frameworks (such as RAGAS) calculate quantitative scores across three critical pillars:
1. **Faithfulness**: Is the generated answer strictly grounded in the retrieved contexts without hallucination?
2. **Answer Relevancy**: Does the generated answer directly answer the user's question?
3. **Context Recall**: Were all necessary source documents retrieved?

## 🎯 Backend Scenario
Build `RAGEvaluator`:
1. `calculate_faithfulness(answer: str, context: str) -> float`: Measures string groundedness ratio.
2. `calculate_answer_relevance(question: str, answer: str) -> float`: Measures question/answer semantic overlap.
3. `evaluate(question: str, answer: str, context: str) -> Dict[str, float]`: Returns complete evaluation score report.

## 🛠️ Instructions
1. Implement evaluator in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 17
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 17
   ```
