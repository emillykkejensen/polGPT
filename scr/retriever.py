from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from langchain.agents.agent_toolkits import create_retriever_tool
import pinecone
import os

def retriever():

    # Initialize HuggingFaceEmbeddings
    hfEmbedding = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-small",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': False}
    )
    
    # Initialize Pinecone
    pinecone.init(
        api_key=os.environ.get("PINECONE_API_KEY"),
        environment=os.environ.get("PINECONE_ENV"))

    index = pinecone.Index(os.environ.get("PINECONE_INDEX"))
    
    # Create a Pinecone vectorstore connection
    vectorstore = Pinecone(index, hfEmbedding.embed_query, "text")

    # Create retriever tool
    tool = create_retriever_tool(
        retriever=vectorstore.as_retriever(), 
        name="soeg_folketinget_referater",
        description="Søger efter og returnerer referater fra møder i Folketinget."
    )

    return tool