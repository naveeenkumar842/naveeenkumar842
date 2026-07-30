from enum import Enum
from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, EmailStr, Field, field_validator

class UserRole(str, Enum):
    ADMIN = "admin"
    DEVELOPER = "developer"
    VIEWER = "viewer"

class UserRegistrationRequest(BaseModel):
    # TODO: Define fields and password custom validator
    pass

class UserResponseDTO(BaseModel):
    # TODO: Define output DTO model and from_input factory method
    pass
