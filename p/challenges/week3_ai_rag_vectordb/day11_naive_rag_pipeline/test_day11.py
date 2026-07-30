import pytest
from challenges.week3_ai_rag_vectordb.day11_naive_rag_pipeline.solution import RAGPipeline

def mock_embedder(text: str):
    if "python" in text.lower():
        return [1.0, 0.0]
    return [0.0, 1.0]

def test_rag_pipeline_execution():
    pipeline = RAGPipeline(embedding_func=mock_embedder)
    docs = [
        {"id": "1", "text": "Python is a high-level programming language."},
        {"id": "2", "text": "Cooking pasta requires boiling water."}
    ]
    pipeline.index_knowledge(docs)

    def mock_llm(prompt: str) -> str:
        assert "Python" in prompt
        return "Python is a language."

    res = pipeline.query("Tell me about Python", mock_llm_callable=mock_llm, top_k=1)
    assert res["answer"] == "Python is a language."
    assert len(res["retrieved_contexts"]) == 1
    assert "Python is a high-level" in res["retrieved_contexts"][0]
