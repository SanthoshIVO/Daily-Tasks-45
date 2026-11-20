from fastapi import APIRouter, HTTPException
from schemas import RagRequest, RagResponse
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
import os

router = APIRouter(prefix="/rag", tags=["RAG Bot"])

# Global variables for RAG assets
vectordb = None
llm = None

def load_rag_assets():
    global vectordb, llm
    # Load embeddings and vector store
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    try:
        vectordb = FAISS.load_local("D:/pysp1/Notes/FastAPI/files/projects/ai_portfolio/models/faiss_index", embeddings, allow_dangerous_deserialization=True)
    except:
        vectordb = None

    # REPLACED: Gemini with local Ollama (qwen2.5:1.5b)
    llm = ChatOllama(
        model="qwen2.5:1.5b",
        temperature=0
    )

@router.post("/ask", response_model=RagResponse)
def ask_question(req: RagRequest):
    if vectordb is None:
        raise HTTPException(status_code=503, detail="Vector DB not found. Please index your documents first.")
    
    # 1. Similarity Search
    docs = vectordb.similarity_search(req.question, k=req.top_k)
    context = "\n".join([d.page_content for d in docs])
    sources = [d.metadata.get('file', 'Unknown') for d in docs]
    
    # 2. Prompt & Generation
    prompt = f"Answer the question based ONLY on the following context:\n\n{context}\n\nQuestion: {req.question}"
    response = llm.invoke(prompt)
    
    return RagResponse(answer=response.content, sources=list(set(sources)))
