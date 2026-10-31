import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
import re
import contractions
import spacy

def index_data():
    print("Indexing documents for RAG...")
    try:
        # 1. Load data
        with open('D:/pysp1/Notes/FastAPI/projects/data.txt', 'r', encoding='utf-8') as f:
            data = f.read()
        
        # 2. Basic Normalization (Simplified version of your notebook)
        data = data.lower()
        data = re.sub(r'\s{2,}', ' ', data)
        data = contractions.fix(data)
        data = re.sub(r'[^0-9a-zA-Z\s]', '', data)
        
        # 3. Chunking
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.create_documents([data])
        
        # 4. Embedding and FAISS
        embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
        vectordb = FAISS.from_documents(chunks, embeddings)
        
        # 5. Save to the models folder
        vectordb.save_local('D:/pysp1/Notes/FastAPI/projects/ai_portfolio/models/faiss_index')
        print("Vector DB saved successfully to /models/faiss_index!")
    except Exception as e:
        print(f"Error during indexing: {e}")

if __name__ == "__main__":
    index_data()
