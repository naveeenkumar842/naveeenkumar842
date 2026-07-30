import math
from typing import List, Optional

def recursive_text_chunker(
    text: str,
    chunk_size: int = 100,
    chunk_overlap: int = 20,
    separators: Optional[List[str]] = None
) -> List[str]:
    """Recursively splits text into overlapping chunks based on separators."""
    if not text.strip():
        return []

    if separators is None:
        separators = ["\n\n", "\n", ". ", " ", ""]

    def _split_text(content: str, seps: List[str]) -> List[str]:
        if len(content) <= chunk_size:
            return [content.strip()] if content.strip() else []

        if not seps:
            # Fallback hard slice if no separators remaining
            chunks = []
            start = 0
            while start < len(content):
                chunks.append(content[start:start + chunk_size].strip())
                start += (chunk_size - chunk_overlap)
            return [c for c in chunks if c]

        sep = seps[0]
        sub_seps = seps[1:]
        splits = content.split(sep) if sep else list(content)

        final_chunks = []
        current_chunk = ""

        for part in splits:
            item = part + sep if sep else part
            if len(current_chunk) + len(item) <= chunk_size:
                current_chunk += item
            else:
                if current_chunk.strip():
                    final_chunks.append(current_chunk.strip())
                
                # Check if item itself is larger than chunk_size
                if len(item) > chunk_size and sub_seps:
                    final_chunks.extend(_split_text(item, sub_seps))
                    current_chunk = ""
                else:
                    current_chunk = item

        if current_chunk.strip():
            final_chunks.append(current_chunk.strip())

        return final_chunks

    raw_chunks = _split_text(text, separators)
    
    # Post-process overlap sliding window
    overlapped = []
    for i, c in enumerate(raw_chunks):
        if i == 0:
            overlapped.append(c)
        else:
            prev = raw_chunks[i - 1]
            overlap_prefix = prev[-chunk_overlap:] if len(prev) >= chunk_overlap else prev
            combined = (overlap_prefix + " " + c).strip()
            overlapped.append(combined[:chunk_size + chunk_overlap])

    return [c for c in overlapped if c]

def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    """Computes cosine similarity between two float vectors."""
    if len(vec_a) != len(vec_b):
        raise ValueError("Vector dimensions must match")

    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))

    if norm_a == 0.0 or norm_b == 0.0:
        return 0.0

    return dot_product / (norm_a * norm_b)
