from langchain_community.document_loaders import PyPDFLoader
from zenml import step
from typing import Annotated


@step
def import_data() -> Annotated[list,"My_Data"] : 
# Replace this with your actual document or whatever (Web page, Word...)
    loader = PyPDFLoader(r"C:\Users\LENOVO\Desktop\DATA_SCIENCE\S3\Deep_Learning\ReGenuis--RAG\loi001.pdf")
    data = loader.load()
    return data