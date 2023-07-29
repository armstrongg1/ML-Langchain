from langchain.text_splitter import CharacterTextSplitter
import os
from dotenv import load_dotenv
# from langchain.document_loaders import TextLoader
from langchain.document_loaders import WhatsAppChatLoader
from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain.vectorstores import Pinecone
from langchain import VectorDBQA, OpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA


load_dotenv()
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIROMENT"))

if __name__ == '__main__':

    print("Hello World")

    loader = WhatsAppChatLoader(r"C:\trabalho_upwork\langchan_course\whatsapp_bruna\_chat.txt")
    document = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    texts = text_splitter.split_documents(document)
    print(len(texts))

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    #docsearch = Pinecone.from_documents(texts, embeddings, index_name='whatsapp-bruna-embeddings-index')
    #docsearch = Pinecone.from_existing_index(embedding=embeddings, index_name='whatsapp-bruna-embeddings-index')
    # local machine
    vectorstore = FAISS.from_documents(texts, embeddings)
    vectorstore.save_local("faiss_index_react")

    new_vectorstore = FAISS.load_local("faiss_index_react", embeddings)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=new_vectorstore.as_retriever())

    res = qa.run("A Bruna é minha esposa. Como é o meu relacionamento com a Bruna?")
    print(res)

    #qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=docsearch, return_source_document=True)

    #query = "Qual a pergunta que mais faço para a Bruna?"

    #result = qa.query(query)
    #print(result)






