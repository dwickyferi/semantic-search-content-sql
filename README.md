# Semantic Search with pgvector

This project implements semantic search functionality for SQL content using vector embeddings. It uses PostgreSQL with pgvector extension for vector similarity search, OpenAI embeddings, and Flask for the API interface.

## Features

- Vector similarity search using pgvector
- OpenAI embeddings integration
- RESTful API for semantic search queries
- Docker containerization

## Prerequisites

- Docker and Docker Compose
- Python 3.x
- OpenAI API key

## Quick Start

### 1. Environment Setup

Copy the `.env.example` file to `.env` and update the values:

```bash
cp .env.example .env
```

Then update the values in `.env` with your configuration.

Create a `config.py` file in the root directory with your OpenAI API key:

```python
OPENAI_API_KEY = "your-api-key-here"
EMBEDDING_MODEL = "text-embedding-3-small"
```

### 2. Start PostgreSQL with pgvector

```bash
docker-compose up -d
```

This will:

- Start PostgreSQL with pgvector extension
- Initialize the database with sample data
- Expose the database on port 5432

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Sync Embeddings

Run the embedding synchronization script to generate and store embeddings for existing content:

```bash
python sync_embedding.py
```

### 5. Start the API Server

```bash
python run.py
```

The API will be available at `http://localhost:5000`

## API Usage

### Semantic Search Endpoint

**Endpoint:** `POST /semantic-search`

**Request Body:**

```json
{
  "query": "Your search query here",
  "top_k": 5
}
```

**Example Request:**

```bash
curl -X POST http://localhost:5000/semantic-search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Europe tour",
    "top_k": 3
  }'
```

**Example Response:**

```json
[
    {
        "id": 1,
        "description": "Tour keliling Eropa: Menjelajahi kota-kota ikonik dari Paris hingga Roma dengan kereta cepat.",
        "similarity": 89.5
    },
    ...
]
```

## Project Structure

```
.
├── api/
│   └── app.py            # Flask API implementation
├── data/
│   └── init.sql          # Database initialization script
├── embedding/
│   ├── embedder.py       # Embedding generation logic
│   └── utils.py          # Utility functions
├── docker-compose.yml    # Docker configuration
├── requirements.txt      # Python dependencies
├── config.py            # Configuration settings
└── sync_embedding.py    # Embedding synchronization script
```

## Technical Details

- Uses pgvector for efficient vector similarity search
- OpenAI's text-embedding-ada-002 model for generating embeddings
- Flask for RESTful API implementation
- SQLAlchemy for database operations

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
