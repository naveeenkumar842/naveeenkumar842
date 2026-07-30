import uuid
from enum import Enum
from datetime import datetime, timezone
from typing import Optional, Dict, Any
from pydantic import BaseModel, EmailStr, Field, field_validator

class UserRole(str, Enum):
    ADMIN = "admin"
    DEVELOPER = "developer"
    VIEWER = "viewer"

class UserRegistrationRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    role: UserRole = UserRole.DEVELOPER

    @field_validator("password")
    @classmethod
    def validate_password_complexity(cls, v: str) -> str:
        if not any(char.isdigit() for char in v):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isupper() for char in v):
            raise ValueError("Password must contain at least one uppercase letter")
        return v

class UserResponseDTO(BaseModel):
    id: str
    email: str
    role: UserRole
    created_at: str

    @classmethod
    def from_input(cls, req: UserRegistrationRequest, user_id: Optional[str] = None) -> "UserResponseDTO":
        return cls(
            id=user_id or str(uuid.uuid4()),
            email=req.email,
            role=req.role,
            created_at=datetime.now(timezone.utc).isoformat()
        )
