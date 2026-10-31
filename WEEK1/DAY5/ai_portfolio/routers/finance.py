from fastapi import APIRouter, Depends, HTTPException
from schemas import ExpenseRequest, ExpenseResponse, HealthCheck
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.tools import tool
from langchain.agents import create_agent
import os

router = APIRouter(prefix="/finance", tags=["Money Mentor"])

# --- Simple In-Memory Store ---
LEDGER = []
BUDGETS = {"food": 3000, "travel": 1500, "shopping": 2000, "entertainment": 1000}

@tool
def log_expense(amount: float, category: str) -> str:
    '''Save an expense into the ledger.'''
    LEDGER.append({"amount": amount, "category": category.lower()})
    return f"Logged ₹{amount} under {category}"

@tool
def check_budget(category: str) -> str:
    '''Check budget for a category.'''
    cat = category.lower()
    limit = BUDGETS.get(cat, 1000)
    spent = sum(e["amount"] for e in LEDGER if e["category"] == cat)
    return f"{cat}: spent ₹{spent} of ₹{limit} (Remaining: {limit-spent})"

@tool
def total_spent() -> str:
    '''Get total spent.'''
    return f"Total spent: ₹{sum(e['amount'] for e in LEDGER)}"

tools = [log_expense, check_budget, total_spent]

def get_llm():
    # REPLACED: Gemini with local Ollama
    return ChatOllama(
        model="qwen2.5:1.5b",
        temperature=0
    )

@router.post("/expense", response_model=ExpenseResponse)
def report_expense(req: ExpenseRequest):
    try:
        llm = get_llm()
        money_agent = create_agent(llm, tools, system_prompt="You are a financial assistant. Log expenses and report budget status in one short line.")
        result = money_agent.invoke({"messages": [("user", req.message)]})
        return ExpenseResponse(reply=result["messages"][-1].content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.get("/report", response_model=HealthCheck)
def get_health_report():
    try:
        if not LEDGER:
            return HealthCheck(score=100, status="Healthy", biggest_expense_category="None", saving_tip="Start logging expenses!")
        
        return HealthCheck(
            score=85, 
            status="Healthy", 
            biggest_expense_category="food", 
            saving_tip="Try to reduce food delivery costs."
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
