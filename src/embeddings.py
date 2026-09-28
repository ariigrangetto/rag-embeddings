from src.client import gemini_client
from google.genai import types

def get_embeddings(text: str) -> list[float]:
    # genera un vector de 768 dimensiones para el texto dado.

    response = gemini_client.models.embed_content(
        model="gemini-embedding-2",
        contents=text,
        config=types.EmbedContentConfig(output_dimensionality=768)
    )
    return response.embeddings[0].values