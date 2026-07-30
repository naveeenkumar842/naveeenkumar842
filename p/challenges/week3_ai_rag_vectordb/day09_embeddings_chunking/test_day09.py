import pytest
import math
from challenges.week3_ai_rag_vectordb.day09_embeddings_chunking.solution import (
    recursive_text_chunker,
    cosine_similarity
)

def test_cosine_similarity_identical_vectors():
    vec = [0.2, 0.8, -0.5]
    sim = cosine_similarity(vec, vec)
    assert math.isclose(sim, 1.0, rel_tol=1e-5)

def test_cosine_similarity_orthogonal_vectors():
    v1 = [1.0, 0.0]
    v2 = [0.0, 1.0]
    assert math.isclose(cosine_similarity(v1, v2), 0.0, abs_tol=1e-5)

def test_recursive_text_chunker_basic():
    sample_text = (
        "FastAPI is a modern, fast Python web framework. "
        "It supports high performance async execution. "
        "Pydantic provides runtime validation and speed."
    )
    chunks = recursive_text_chunker(sample_text, chunk_size=60, chunk_overlap=10)
    assert len(chunks) >= 2
    assert all(len(c) <= 80 for c in chunks)
