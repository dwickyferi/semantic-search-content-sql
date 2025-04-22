from flask import Flask, request, jsonify
from sqlalchemy import text
import openai
from config import OPENAI_API_KEY, EMBEDDING_MODEL
from embedding.utils import get_db
import numpy as np

app = Flask(__name__)
openai.api_key = OPENAI_API_KEY

def get_query_embedding(query):
    response = openai.embeddings.create(
        input=[query],
        model=EMBEDDING_MODEL
    )
    return response.data[0].embedding

@app.route("/semantic-search", methods=["POST"])
def semantic_search():
    data = request.json
    query = data.get("query")
    top_k = int(data.get("top_k", 5)) 
    
    embedding = get_query_embedding(query)
    embedding_str = f"[{', '.join(f'{x:.8f}' for x in embedding)}]"

    for db in get_db():
        result = db.execute(text("""
            SELECT id, description, 
               (1 - (embedding <-> CAST(:embedding AS vector))) * 100 as similarity
            FROM tour_descriptions
            ORDER BY embedding <-> CAST(:embedding AS vector)
            LIMIT :top_k
        """), {"embedding": embedding_str, "top_k": top_k})
        
        matches = [{"id": r.id, "description": r.description, "similarity":r.similarity} for r in result]
        return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)