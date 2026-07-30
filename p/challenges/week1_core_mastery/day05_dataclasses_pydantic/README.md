# Day 05: Dataclasses & Pydantic Request Validation Layer

## 💡 Concept Overview
Modern Python web frameworks (FastAPI, SQLModel) rely heavily on Pydantic and dataclasses for strict runtime data validation, serialization, and type safety.

## 🎯 Backend Scenario
You are designing the user authentication payload validator for an API gateway.
Create Pydantic V2 schemas:
1. `UserRegistrationRequest`:
   - `email`: Valid EmailStr format.
   - `password`: String, min length 8, must contain at least 1 digit and 1 uppercase letter (custom field validator `@field_validator`).
   - `role`: Enum `["admin", "developer", "viewer"]` (default `"developer"`).
2. `UserResponseDTO`:
   - `id`: UUID string.
   - `email`: str.
   - `role`: str.
   - `created_at`: Datetime ISO string.
   - Method `from_input(user_dict, user_id)`: Transforms registration dictionary into DTO.

## 🛠️ Instructions
1. Implement Pydantic models in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 5
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 5
   ```
