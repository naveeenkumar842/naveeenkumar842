import pytest
from pydantic import ValidationError
from challenges.week1_core_mastery.day05_dataclasses_pydantic.solution import (
    UserRegistrationRequest,
    UserResponseDTO,
    UserRole
)

def test_valid_user_registration():
    req = UserRegistrationRequest(
        email="dev@example.com",
        password="SecurePassword123",
        role=UserRole.ADMIN
    )
    assert req.email == "dev@example.com"
    assert req.role == UserRole.ADMIN

def test_invalid_email_raises_validation_error():
    with pytest.raises(ValidationError):
        UserRegistrationRequest(
            email="invalid-email-string",
            password="SecurePassword123"
        )

def test_password_missing_digit_raises():
    with pytest.raises(ValidationError) as exc_info:
        UserRegistrationRequest(
            email="dev@example.com",
            password="NoDigitPassword"
        )
    assert "Password must contain at least one digit" in str(exc_info.value)

def test_password_missing_uppercase_raises():
    with pytest.raises(ValidationError) as exc_info:
        UserRegistrationRequest(
            email="dev@example.com",
            password="lowercase123"
        )
    assert "Password must contain at least one uppercase letter" in str(exc_info.value)

def test_user_response_dto_creation():
    req = UserRegistrationRequest(
        email="dev@example.com",
        password="SecurePassword123"
    )
    dto = UserResponseDTO.from_input(req, user_id="user-999")

    assert dto.id == "user-999"
    assert dto.email == "dev@example.com"
    assert dto.role == UserRole.DEVELOPER
    assert "T" in dto.created_at
