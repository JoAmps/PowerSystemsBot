from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import (
    VectorStoreToolkit,
    VectorStoreInfo
)
import os
from chroma.data_process import create_load_pdf_loader

api_key = os.getenv('API_KEY')
def chroma_vectordb():
    
    pages = create_load_pdf_loader()
    # Load documents into ChromaDB vector database
    store = Chroma.from_documents(pages, collection_name='power_systems')

    vectorstore_info = VectorStoreInfo(
        name="power_systems",
        description="power systems protection as a pdf",
        vectorstore=store
    )
    # Convert the document store into a langchain toolkit
    toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info, openai_api_key=api_key)
    return toolkit, store