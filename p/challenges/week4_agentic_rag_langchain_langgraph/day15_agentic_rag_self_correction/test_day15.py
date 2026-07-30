import pytest
from challenges.week4_agentic_rag_langchain_langgraph.day15_agentic_rag_self_correction.solution import SelfCorrectiveRAGAgent

def test_self_corrective_rag_successful_first_try():
    agent = SelfCorrectiveRAGAgent()

    def mock_retriever(q: str):
        return ["FastAPI is an async framework in Python."]

    def mock_llm(q: str, c: str):
        return f"Answer based on {c}"

    res = agent.run_pipeline("FastAPI framework", mock_retriever, mock_llm)
    assert res["attempts"] == 1
    assert res["relevant_docs_count"] == 1
    assert "FastAPI" in res["answer"]

def test_self_corrective_rag_triggers_query_rewrite():
    agent = SelfCorrectiveRAGAgent()

    def mock_retriever(q: str):
        if "detailed information" in q:
            return ["detailed information on database optimization in PostgreSQL"]
        return ["Irrelevant text about gardening"]

    def mock_llm(q: str, c: str):
        return "Grounded Answer"

    res = agent.run_pipeline("database optimization", mock_retriever, mock_llm)
    assert res["attempts"] == 2
    assert "detailed information on database optimization" in res["final_query"]
    assert res["relevant_docs_count"] == 1
