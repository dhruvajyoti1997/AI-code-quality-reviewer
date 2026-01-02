from llama_index.core import VectorStoreIndex, Document

def retrieve_context_node(state):
    documents = [
        Document(text=chunk) for chunk in state["code_chunks"]
    ]
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()

    response = query_engine.query(
        "Find related logic, design patterns, dependencies, and risks"
    )

    return {
        "retrieved_context": str(response)
    }