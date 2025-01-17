from pathlib import Path
from zenml import step
from typing import Annotated
import os
import langchain_core
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_nomic import NomicEmbeddings
from langchain_community.vectorstores import FAISS


@step
def embeddingsXvectore_store(doc:list) -> Annotated[str,"embeddings_file"]:
    os.environ["NOMIC_API_KEY"] = "nk-uC7cI5olWsQ8GFL5d_y54N5zpNlx9vH86SgOieRzBWA"
    embeddings = NomicEmbeddings(model="nomic-embed-text-v1.5")   
    vector_store = FAISS.from_documents(documents=doc, embedding=embeddings)

    # faiss_file = (r"C:/Users/LENOVO/AppData/Roaming/zenml/local_stores/faiss_index")
    faiss_file = ("./faiss_index")

    vector_store.save_local(faiss_file)
    return faiss_file
