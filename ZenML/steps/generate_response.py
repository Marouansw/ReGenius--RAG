from zenml import step
from typing import Annotated, List, Tuple
from langchain_ollama.llms import OllamaLLM
from langchain_mistralai import ChatMistralAI
from zenml.types import MarkdownString
import os

@step
def generate_response(context:MarkdownString,query:str) ->Tuple[Annotated[MarkdownString,"LLAMA's 3.2 Response"],Annotated[MarkdownString,"Mistral's Response"]] :
    """Generate a response using a language model."""
    # LLAMA
    llm=OllamaLLM(model='llama3.2:latest')
    
    # GEMINI
    if "MISTRAL_API_KEY" not in os.environ:
        os.environ["MISTRAL_API_KEY"] = 'ekGhgJvxhbpAkTX9m2CZa59rja74AHDf'
    llm2 = ChatMistralAI(model="mistral-large-latest",temperature=0.1,max_retries=2)
    
    # PROMPT
    # context = "\n".join(retrieved_docs)
    prompt = f"Reponds a la question suivante en se basant sur le context :\n\nContext:\n{context}\n\nQuestion:\n{query}"
    
    # RESPONSES
    response1 = llm.invoke(prompt)
    response2 = llm2.invoke(prompt)
    
    return MarkdownString(str(response1)),MarkdownString(str(response2))
