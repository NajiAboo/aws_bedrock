import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_aws import ChatBedrock
from langchain_aws.embeddings import BedrockEmbeddings
from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.indexes import VectorstoreIndexCreator

def create_index(path="The-Life-of-Abraham-Lincoln_page2.pdf"):
    data_load = PyPDFLoader(path)
    data_split = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " "], chunk_size=100, chunk_overlap=10)
    data_embedding = BedrockEmbeddings(credentials_profile_name="macvscode", model_id="amazon.titan-embed-text-v1", region_name="us-east-1")
    data_index = VectorstoreIndexCreator(text_splitter=data_split, embedding=data_embedding, vectorstore_cls=FAISS)
    db_index = data_index.from_loaders([data_load])
    return db_index

def get_llm():
    llm = ChatBedrock(credentials_profile_name='macvscode', model_id="anthropic.claude-3-sonnet-20240229-v1:0", region_name='us-east-1')
    return llm


def rag_response(index, question):
    llm = get_llm()
    response = index.query(question, llm)
    return response


#llm = get_llm()
response = rag_response(create_index(), "when was lincon born?")
print(response)

