from langchain.document_loaders import PyPDFLoader
import sys
sys.path.append("data")

# Create and load PDF Loader
def create_load_pdf_loader():
    loader = PyPDFLoader('src/chroma/EE 559 Protection of Power Systems.pdf')
    # Split pages from pdf 
    pages = loader.load_and_split()
    return pages
