from app.services.ai_service import semantic_search
from app.core.groq_client import client


MODEL = "llama-3.3-70b-versatile"


def chat_with_memories(
    user_id: int,
    question: str
):

    results = semantic_search(
        query=question,
        user_id=user_id,
        top_k=5
    )

    context = ""

    if results["documents"]:

        for document in results["documents"][0]:

            context += document
            context += "\n\n"

    else:

        context = "No relevant memories found."

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Memora AI.\n"
                    "Answer ONLY using the user's saved memories.\n"
                    "If the answer is not present in the memories, "
                    "say you couldn't find it."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Context:\n\n{context}\n\n"
                    f"Question:\n{question}"
                )
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content