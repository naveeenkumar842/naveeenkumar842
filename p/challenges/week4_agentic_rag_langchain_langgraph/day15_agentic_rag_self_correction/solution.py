from typing import List, Dict, Any, Callable

class SelfCorrectiveRAGAgent:
    def grade_document_relevance(self, query: str, doc_text: str) -> bool:
        """Evaluates whether doc_text contains keywords matching query."""
        query_words = set(q.lower().strip() for q in query.split() if len(q) > 2)
        doc_words = set(d.lower().strip() for d in doc_text.split())
        overlap = query_words.intersection(doc_words)
        return len(overlap) > 0

    def rewrite_query(self, query: str) -> str:
        """Optimizes user query for better search retrieval."""
        return f"detailed information on {query.strip()}"

    def run_pipeline(
        self,
        query: str,
        retriever_func: Callable[[str], List[str]],
        llm_func: Callable[[str, str], str]
    ) -> Dict[str, Any]:
        attempts = 0
        current_query = query
        relevant_docs = []

        while attempts < 2:
            attempts += 1
            retrieved = retriever_func(current_query)
            relevant_docs = [doc for doc in retrieved if self.grade_document_relevance(current_query, doc)]

            if relevant_docs:
                break

            # If no docs relevant, rewrite query and retry
            current_query = self.rewrite_query(current_query)

        context = "\n".join(relevant_docs) if relevant_docs else "No relevant documents found."
        answer = llm_func(current_query, context)

        return {
            "final_query": current_query,
            "attempts": attempts,
            "relevant_docs_count": len(relevant_docs),
            "answer": answer
        }
