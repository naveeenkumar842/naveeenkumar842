import pytest
from challenges.week1_core_mastery.day04_context_managers.solution import (
    MockDatabaseConnection,
    DatabaseTransactionGuard
)

def test_successful_transaction_commits():
    db = MockDatabaseConnection()
    guard = DatabaseTransactionGuard(db)

    with guard as conn:
        conn.operations.append("INSERT INTO users VALUES (1, 'Alice')")

    assert db.state == "COMMITTED"
    assert guard.committed is True
    assert guard.rolled_back is False

def test_failed_transaction_rolls_back():
    db = MockDatabaseConnection()
    guard = DatabaseTransactionGuard(db, suppress_errors=False)

    with pytest.raises(ZeroDivisionError):
        with guard as conn:
            conn.operations.append("UPDATE accounts SET balance = 0")
            _ = 1 / 0

    assert db.state == "ROLLED_BACK"
    assert guard.committed is False
    assert guard.rolled_back is True

def test_failed_transaction_suppressed():
    db = MockDatabaseConnection()
    guard = DatabaseTransactionGuard(db, suppress_errors=True)

    with guard as conn:
        raise ValueError("Non-critical sync error")

    assert db.state == "ROLLED_BACK"
    assert guard.rolled_back is True
