from typing import Any
from fastapi import HTTPException

def CustomNotFoundException(entity: Any, key: str, value: Any):
    raise HTTPException(status_code=404, detail=f"{entity.__name__} with {key} '{value}' not found")

def CustomExistException(entity: Any, key: str, value: Any):
    raise HTTPException(status_code=400, detail=f"{entity.__name__} with {key} '{value}' already exists")

def CustomAccessForbiddenException():
    raise HTTPException(status_code=403, detail=f"Access is forbidden! You are not an admin")

def CustomCountException(entity: Any, key: str, value: Any):
    raise HTTPException(status_code=400, detail=f"Not enough {(entity.__name__).lower()}s with {key} {value} in stock")