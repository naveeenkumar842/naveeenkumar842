import pytest
import types
from challenges.week1_core_mastery.day02_generators_memory.solution import (
    stream_log_lines,
    parse_log_entry,
    filter_log_events
)

LOG_SAMPLE = [
    "2026-07-30T10:00:00 INFO /api/v1/users 200 45\n",
    "   \n",
    "# Comment line\n",
    "2026-07-30T10:00:01 ERROR /api/v1/checkout 500 650\n",
    "2026-07-30T10:00:02 WARN /api/v1/products 404 120\n",
    "2026-07-30T10:00:03 ERROR /api/v1/pay 502 890\n"
]

def test_stream_log_lines_is_generator():
    gen = stream_log_lines(LOG_SAMPLE)
    assert isinstance(gen, types.GeneratorType)
    lines = list(gen)
    assert len(lines) == 4
    assert lines[0].startswith("2026-07-30T10:00:00")

def test_parse_log_entry():
    entry = parse_log_entry("2026-07-30T10:00:01 ERROR /api/v1/checkout 500 650")
    assert entry["level"] == "ERROR"
    assert entry["endpoint"] == "/api/v1/checkout"
    assert entry["status_code"] == 500
    assert entry["duration_ms"] == 650.0

def test_filter_log_events_pipeline():
    raw_lines = stream_log_lines(LOG_SAMPLE)
    parsed = (parse_log_entry(line) for line in raw_lines)
    errors = list(filter_log_events(parsed, level="ERROR", min_duration_ms=500.0))

    assert len(errors) == 2
    assert errors[0]["endpoint"] == "/api/v1/checkout"
    assert errors[1]["endpoint"] == "/api/v1/pay"
