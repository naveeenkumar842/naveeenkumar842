import math
from typing import List, Dict, Any, Callable

def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    if len(vec_a) != len(vec_b):
        return 0.0
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0
    return dot / (norm_a * norm_b)

class RAGPipeline:
    def __init__(self, embedding_func: Callable[[str], List[float]]):
        self.embedding_func = embedding_func
        self.store: List[Dict[str, Any]] = []

    def index_knowledge(self, documents: List[Dict[str, str]]) -> None:
        for doc in documents:
            text = doc["text"]
            vec = self.embedding_func(text)
            self.store.append({
                "id": doc.get("id", str(len(self.store))),
                "text": text,
                "embedding": vec
            })

    def query(self, user_query: str, mock_llm_callable: Callable[[str], str], top_k: int = 2) -> Dict[str, Any]:
        query_vec = self.embedding_func(user_query)
        scored_docs = []

        for doc in self.store:
            score = cosine_similarity(query_vec, doc["embedding"])
            scored_docs.append((score, doc["text"]))

        scored_docs.sort(key=lambda x: x[0], reverse=True)
        retrieved_contexts = [doc[1] for doc in scored_docs[:top_k]]

        formatted_context = "\n---\n".join(retrieved_contexts)
        prompt = f"Answer using context:\n{formatted_context}\n\nQuestion: {user_query}"
        answer = mock_llm_callable(prompt)

        return {
            "answer": answer,
            "retrieved_contexts": retrieved_contexts,
            "prompt": prompt
        }
