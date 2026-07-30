import pytest
from challenges.week3_ai_rag_vectordb.day12_hybrid_search_reranking.solution import (
    compute_bm25_score,
    reciprocal_rank_fusion
)

def test_compute_bm25_score():
    score = compute_bm25_score("FastAPI async", "FastAPI is an async framework")
    assert score > 0.0

def test_reciprocal_rank_fusion():
    dense = ["doc_A", "doc_B", "doc_C"]
    sparse = ["doc_B", "doc_A", "doc_D"]

    fused = reciprocal_rank_fusion(dense, sparse, k=60)
    # doc_B is rank 2 in dense and rank 1 in sparse -> should get top RRF score
    assert len(fused) == 4
    top_doc = fused[0][0]
    assert top_doc in ["doc_A", "doc_B"]
