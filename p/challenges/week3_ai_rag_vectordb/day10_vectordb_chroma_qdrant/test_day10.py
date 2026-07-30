import pytest
from challenges.week3_ai_rag_vectordb.day10_vectordb_chroma_qdrant.solution import VectorDBEngine

def test_vector_db_search_and_metadata_filter():
    vdb = VectorDBEngine()
    vdb.add_document("doc1", "FastAPI web dev", [1.0, 0.0, 0.0], {"category": "backend"})
    vdb.add_document("doc2", "React JS UI", [0.0, 1.0, 0.0], {"category": "frontend"})
    vdb.add_document("doc3", "Python AsyncIO", [0.9, 0.1, 0.0], {"category": "backend"})

    # Query matching backend vectors
    results = vdb.search([1.0, 0.0, 0.0], top_k=2, filter_metadata={"category": "backend"})
    assert len(results) == 2
    assert results[0]["id"] == "doc1"
    assert results[1]["id"] == "doc3"

def test_vector_db_top_k_limit():
    vdb = VectorDBEngine()
    for i in range(5):
        vdb.add_document(f"doc_{i}", f"Text {i}", [0.5, 0.5, 0.0])

    res = vdb.search([0.5, 0.5, 0.0], top_k=3)
    assert len(res) == 3
