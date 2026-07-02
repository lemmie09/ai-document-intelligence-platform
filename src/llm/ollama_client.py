import ollama


class OllamaClient:

    def ask(self, question: str, context: str):

        prompt = f"""
You are an expert research assistant.

Your task is to answer questions ONLY using the provided context.

Instructions:
- Read all retrieved context carefully.
- Summarize the document in your own words.
- If multiple chunks discuss the same topic, combine the information.
- If the answer is not contained in the context, clearly say:
  "I couldn't find that information in the document."

Context:
{context}

Question:
{question}

Answer:
"""

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]