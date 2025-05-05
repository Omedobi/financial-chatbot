def build_prompt(question: str, context: str) -> str:
    return f"""
You are an expert financial analyst with access to the following context:

{context}

Answer this question:
{question}
"""