from typing import List, Dict, Any, Callable

class RAGPipeline:
    def __init__(self, embedding_func: Callable[[str], List[float]]):
        self.embedding_func = embedding_func
        self.store = []

    def index_knowledge(self, documents: List[Dict[str, str]]) -> None:
        # TODO: Embed documents and index in store
        pass

    def query(self, user_query: str, mock_llm_callable: Callable[[str], str], top_k: int = 2) -> Dict[str, Any]:
        # TODO: Retrieve context, format RAG prompt, call LLM, return response
        pass
