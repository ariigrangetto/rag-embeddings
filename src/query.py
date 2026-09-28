from src.client import supabase, gemini_client
from src.embeddings import get_embeddings

def search_documents(query: str, limit: int = 3, threshold: float = 1.5):
    # convirtiendo la query en vector
    query_vector = get_embeddings(query)

    # invocar funcion RPC en Supabase usando la distancia euclidia
    # luego de haber sido construido en vector, se utiliza la función para encontrar los otros vectores cercanos (la distancia tiene que ser menor que el threshold)
    response = supabase.rpc("match_documents_l2", {
        "query_embedding": query_vector,
        "distance_threshold": threshold,
        "match_count": limit
    }).execute()

    return response.data
    # aqui va a retornar los vectores que han pasado directamente por la función. Es decir lo vectores "finalistas"

def ask_rag(question: str):
    print(f"\nPregunta: {question}")

    docs = search_documents(question)

    if not docs: 
        print("No se encontró información relevante.")
        return

    context = "\n---\n".join([d['content'] for d in docs])
    prompt = f"""Eres un asistente que responde preguntas de forma estricta.
    REGLAS OBLIGATORIAS:
    1. Responde a la pregunta basándote EXCLUSIVAMENTE en la información provista en el contexto.
    2. No utilices conocimiento previo ni información externa a este contexto.
    3. Si la respuesta no se encuentra de forma explícita en el contexto previo, responde exactamente: "No dispongo de esa información en los documentos suministrados."
    4. Cita o menciona los datos tal cual aparecen en el contexto.

    CONTEXTO:
    {context}

    PREGUNTA: {question}
    RESPUESTA: """

    response = gemini_client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("\nRespuesta generada:")
    print(response.text)

if __name__ == "__main__":
    ask_rag("¿Quién ganó el mundial de fútbol en 2022?");


