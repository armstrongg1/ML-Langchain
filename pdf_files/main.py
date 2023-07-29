import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone
import pinecone
from typing import Any
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.llms import OpenAI


load_dotenv()
#pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIROMENT"))


if __name__ == "__main__":
    #run_llm("Como fazer pra ler pdfs?")

    pdf_path = r'C:\trabalho_upwork\langchan_course\pdf_files\1053.pdf'

    loader = PyPDFDirectoryLoader(path=r"C:\trabalho_upwork\langchan_course\pdf_files\pdfs")

    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
    docs = text_splitter.split_documents(documents=documents)

    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(docs, embeddings)

    #vector_store.save_local("faiss_index_pdfs")
    vector_store.save_local("faiss_index_folder_pdfs")

    #new_vector_store = FAISS.load_local("faiss_index_pdfs", embeddings)
    new_vector_store = FAISS.load_local("faiss_index_folder_pdfs", embeddings)

    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=new_vector_store.as_retriever())

    res = qa.run("Me da a lista de gastos com ifood. Coloque isso em uma tabela para eu ler.Gere um link em html para eu baixar.")





    print(res)


