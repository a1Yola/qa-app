from langchain.llms import CTransformers

def load_llm():
    llm = CTransformers(
        model = "mistral-7b-instruct-v0.1.Q4_K_S.gguf",
        model_type="mistral",
        max_new_tokens = 1048,
        temperature = 0.3
    )
    return llm
