from app.core.groq_client import client
from app.core.embeddings import generate_embedding
from app.core.chroma import collection


MODEL = "llama-3.3-70b-versatile"


def generate_summary(text: str):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI assistant that summarizes webpages. "
                    "Return only a concise summary."
                )
            },
            {
                "role": "user",
                "content": text[:12000]
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


def store_embedding(
    memory_id: int,
    title: str,
    content: str
):

    embedding = generate_embedding(content)

    collection.add(
        ids=[str(memory_id)],
        embeddings=[embedding],
        documents=[content],
        metadatas=[
            {
                "title": title
            }
        ]
    )




def semantic_search(query: str, top_k: int = 5):

    embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=top_k
    )

    return results

def delete_embedding(memory_id: int):

    collection.delete(
        ids=[str(memory_id)]
    )