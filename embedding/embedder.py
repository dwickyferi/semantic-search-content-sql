import openai
import numpy as np
from sqlalchemy import text
from config import OPENAI_API_KEY, EMBEDDING_MODEL
from embedding.utils import get_db

openai.api_key = OPENAI_API_KEY

def get_embedding(text):
    response = openai.embeddings.create(
        input=[text],
        model=EMBEDDING_MODEL
    )
    return response.data[0].embedding

def sync_embeddings():
    for db in get_db():
        result = db.execute(text("""
            SELECT id, description FROM tour_descriptions
            WHERE embedding IS NULL
        """))
        for row in result:
            emb = get_embedding(row.description)
            db.execute(
                text("UPDATE tour_descriptions SET embedding = :embedding WHERE id = :id"),
                {"embedding": emb, "id": row.id}
            )
        db.commit()