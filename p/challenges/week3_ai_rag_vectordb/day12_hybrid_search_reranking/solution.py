from collections import defaultdict
from typing import List, Tuple, Dict

def compute_bm25_score(query: str, text: str) -> float:
    """Computes basic term frequency score for keyword matching."""
    query_tokens = [q.lower().strip() for q in query.split() if q.strip()]
    text_tokens = [t.lower().strip() for t in text.split() if t.strip()]

    if not query_tokens or not text_tokens:
        return 0.0

    score = 0.0
    for qt in query_tokens:
        count = text_tokens.count(qt)
        if count > 0:
            score += (count / len(text_tokens)) * 1.5

    return round(score, 4)

def reciprocal_rank_fusion(
    dense_ranks: List[str],
    sparse_ranks: List[str],
    k: int = 60
) -> List[Tuple[str, float]]:
    """Combines dense and sparse ranking lists using RRF."""
    rrf_scores: Dict[str, float] = defaultdict(float)

    for rank, doc_id in enumerate(dense_ranks, start=1):
        rrf_scores[doc_id] += 1.0 / (k + rank)

    for rank, doc_id in enumerate(sparse_ranks, start=1):
        rrf_scores[doc_id] += 1.0 / (k + rank)

    sorted_results = sorted(rrf_scores.items(), key=lambda item: item[1], reverse=True)
    return [(doc_id, round(score, 6)) for doc_id, score in sorted_results]
