# pgvector for RAG Pipelines

pgvector is an open-source PostgreSQL extension for vector similarity search—ideal for RAG (Retrieval-Augmented Generation) pipelines where you need to store and query embeddings.

## Quick Start

### Option 1: With Docker (Recommended)

**Single container:**
```bash
docker run --name pgvector-db \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_DB=rag_db \
  -p 5432:5432 \
  -d \
  pgvector/pgvector:pg16
```

**With Docker Compose:**
```yaml
version: '3.8'
services:
  pgvector:
    image: pgvector/pgvector:pg16
    environment:
      POSTGRES_PASSWORD: mysecretpassword
      POSTGRES_DB: rag_db
    ports:
      - "5432:5432"
    volumes:
      - pgvector_data:/var/lib/postgresql/data

volumes:
  pgvector_data:
```

Run with: `docker compose up --pull always`

### Option 2: Local PostgreSQL Installation

**macOS:**
```bash
brew install postgresql
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt install postgresql postgresql-contrib
```

**Windows:** Download from [postgresql.org](https://www.postgresql.org/download/)

Then install pgvector following [pgvector's GitHub setup](https://github.com/pgvector/pgvector).

## How pgvector Works

pgvector lets PostgreSQL store and query dense vectors (embeddings). For RAG pipelines:

1. **Embed documents**: Use an LLM (OpenAI, local model, etc.) to convert text chunks into vectors (e.g., 1536-dimensional)
2. **Store in database**: Insert embeddings into a pgvector-enabled PostgreSQL table
3. **Index for speed**: pgvector uses IVFFLAT or HNSW indexes for efficient similarity search at scale
4. **Query and retrieve**: Embed the user's question → search for similar vectors → retrieve matching documents → pass as context to LLM

## Core SQL Operations

### Enable pgvector extension

```sql
CREATE EXTENSION vector;
```

### Create a table with vector column

```sql
CREATE TABLE documents (
  id SERIAL PRIMARY KEY,
  content TEXT,
  embedding vector(1536)
);
```

### Create an index for fast search

```sql
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops);
```

### Insert embeddings

```sql
INSERT INTO documents (content, embedding) 
VALUES ('RAG is retrieval-augmented generation', '[0.1, 0.2, ..., 0.9]'::vector);
```

### Search by similarity (cosine distance)

```sql
SELECT content FROM documents 
ORDER BY embedding <=> '[query_vector]'::vector 
LIMIT 5;
```

## Distance Operators

- **`<=>`** = Cosine distance (fastest for high-dimensional embeddings, recommended)
- **`<->`** = L2 distance (Euclidean)
- **`<#>`** = Inner product distance

## Why pgvector for RAG?

- **Native SQL**: No separate vector database needed
- **ACID transactions**: Data consistency and reliability
- **Scalability**: Handles millions of embeddings efficiently
- **Indexing**: IVFFLAT and HNSW indexes for fast retrieval
- **Simplicity**: Integrate with existing PostgreSQL infrastructure

## Testing with Docker

### Connect to running container

```bash
docker exec -it pgvector-db psql -U postgres -d rag_db
```

### Enable pgvector extension

```sql
CREATE EXTENSION vector;
```

### Test with sample data

```sql
CREATE TABLE test_embeddings (
  id SERIAL PRIMARY KEY,
  text TEXT,
  embedding vector(3)
);

INSERT INTO test_embeddings (text, embedding) VALUES
('hello world', '[0.1, 0.2, 0.3]'::vector),
('goodbye world', '[0.1, 0.2, 0.4]'::vector),
('hello there', '[0.1, 0.3, 0.3]'::vector);

SELECT text FROM test_embeddings 
ORDER BY embedding <=> '[0.1, 0.2, 0.35]'::vector 
LIMIT 2;
```

## Language-Specific Integration

### Python Example (psycopg2)

```python
import psycopg2
import numpy as np

conn = psycopg2.connect(
    host="localhost",
    database="rag_db",
    user="postgres",
    password="mysecretpassword"
)

cur = conn.cursor()

# Insert embedding
embedding = np.random.rand(1536).tolist()
cur.execute(
    "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
    ("Sample document", embedding)
)

# Search by similarity
query_embedding = np.random.rand(1536).tolist()
cur.execute(
    "SELECT content FROM documents ORDER BY embedding <=> %s LIMIT 5",
    (query_embedding,)
)

results = cur.fetchall()
cur.close()
conn.close()
```

### Node.js Example (pg)

```javascript
const { Client } = require('pg');

const client = new Client({
  host: 'localhost',
  database: 'rag_db',
  user: 'postgres',
  password: 'mysecretpassword'
});

await client.connect();

// Insert embedding
const embedding = Array.from({ length: 1536 }, () => Math.random());
await client.query(
  'INSERT INTO documents (content, embedding) VALUES ($1, $2)',
  ['Sample document', JSON.stringify(embedding)]
);

// Search by similarity
const queryEmbedding = Array.from({ length: 1536 }, () => Math.random());
const result = await client.query(
  'SELECT content FROM documents ORDER BY embedding <=> $1 LIMIT 5',
  [JSON.stringify(queryEmbedding)]
);

console.log(result.rows);
await client.end();
```

## Indexing Strategies

### IVFFLAT Index (Inverted File Flat)
- Good for large datasets (millions of vectors)
- Trade-off: recall vs. speed
- Fast query time, lower memory

```sql
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops) 
WITH (lists = 100);
```

### HNSW Index (Hierarchical Navigable Small World)
- Better recall than IVFFLAT
- Slightly slower but more accurate
- Good for high-quality retrieval

```sql
CREATE INDEX ON documents USING hnsw (embedding vector_cosine_ops) 
WITH (m = 16, ef_construction = 64);
```

## Performance Tuning

- **Batch inserts**: Group multiple inserts to reduce round trips
- **Index parameters**: Tune `lists` (IVFFLAT) or `m`/`ef_construction` (HNSW) based on your data size
- **Connection pooling**: Use PgBouncer for high-concurrency scenarios
- **Partitioning**: For extremely large datasets (100M+ vectors), consider table partitioning

## Next Steps

- Integrate with your AI/ML framework (LangChain, LlamaIndex, etc.)
- Build document ingestion pipelines
- Implement multi-model retrieval strategies
- Optimize indexes based on your embedding dimensions and data volume
- Set up monitoring and observability for production workloads
