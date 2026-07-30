from typing import Optional, Type, Any

class MockDatabaseConnection:
    def __init__(self):
        self.state = "IDLE"
        self.operations = []

    def begin(self):
        self.state = "IN_TRANSACTION"

    def commit(self):
        self.state = "COMMITTED"

    def rollback(self):
        self.state = "ROLLED_BACK"

class DatabaseTransactionGuard:
    def __init__(self, db_conn: MockDatabaseConnection, suppress_errors: bool = False):
        self.db_conn = db_conn
        self.suppress_errors = suppress_errors
        self.committed = False
        self.rolled_back = False

    def __enter__(self) -> MockDatabaseConnection:
        self.db_conn.begin()
        return self.db_conn

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any]
    ) -> bool:
        if exc_type is not None:
            self.db_conn.rollback()
            self.rolled_back = True
            return self.suppress_errors

        self.db_conn.commit()
        self.committed = True
        return False
