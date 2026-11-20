from fastapi import FastAPI
from routers import insurance, rag, finance
import os

app = FastAPI(title="Santhosh AI Portfolio API")

# Include Routers
app.include_router(insurance.router)
app.include_router(rag.router)
app.include_router(finance.router)

@app.on_event("startup")
async def startup_event():
    print("Initializing AI Portfolio API...")
    # Load ML assets
    insurance.load_assets()
    # Load RAG assets
    rag.load_rag_assets()
    print("All assets loaded successfully!")

@app.get("/")
def root():
    return {"message": "Welcome to Santhosh's AI Portfolio API. Visit /docs for the interactive UI."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
