from pydantic import BaseModel, Field
from typing import List, Optional

# --- ML Project: Insurance ---
class InsuranceRequest(BaseModel):
    age: int = Field(..., gt=0, lt=120)
    sex: str = Field(..., pattern="^(male|female)$")
    bmi: float = Field(..., gt=0)
    children: int = Field(..., ge=0)
    smoker: str = Field(..., pattern="^(yes|no)$")
    region: str = Field(..., pattern="^(southwest|southeast|northwest|northeast)$")

class InsuranceResponse(BaseModel):
    predicted_charges: float

# --- RAG Project ---
class RagRequest(BaseModel):
    question: str = Field(..., min_length=1)
    top_k: int = Field(default=3, ge=1, le=10)

class RagResponse(BaseModel):
    answer: str
    sources: List[str]

# --- GenAI Project: Money Mentor ---
class ExpenseRequest(BaseModel):
    message: str = Field(..., example="Spent 250 on pizza via UPI")

class ExpenseResponse(BaseModel):
    reply: str

class HealthCheck(BaseModel):
    score: int = Field(..., ge=0, le=100)
    status: str
    biggest_expense_category: str
    saving_tip: str
