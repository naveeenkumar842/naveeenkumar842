from typing import Iterable, Iterator, Dict, Any, Optional

def stream_log_lines(lines_iterable: Iterable[str]) -> Iterator[str]:
    """Yield non-empty stripped log lines."""
    for line in lines_iterable:
        cleaned = line.strip()
        if cleaned and not cleaned.startswith("#"):
            yield cleaned

def parse_log_entry(line: str) -> Dict[str, Any]:
    """
    Parses format: "TIMESTAMP LEVEL ENDPOINT STATUS_CODE RESPONSE_TIME_MS"
    """
    parts = line.split()
    if len(parts) < 5:
        raise ValueError(f"Invalid log line format: {line}")

    return {
        "timestamp": parts[0],
        "level": parts[1],
        "endpoint": parts[2],
        "status_code": int(parts[3]),
        "duration_ms": float(parts[4])
    }

def filter_log_events(
    parsed_stream: Iterable[Dict[str, Any]],
    level: Optional[str] = None,
    min_status: Optional[int] = None,
    min_duration_ms: Optional[float] = None
) -> Iterator[Dict[str, Any]]:
    """Yield parsed log events matching criteria."""
    for entry in parsed_stream:
        if level and entry["level"].upper() != level.upper():
            continue
        if min_status and entry["status_code"] < min_status:
            continue
        if min_duration_ms and entry["duration_ms"] < min_duration_ms:
            continue
        yield entry
