from langchain.embeddings.openai import OpenAIEmbeddings
import pinecone
from langchain.vectorstores import Pinecone
import os
from dotenv import load_dotenv
import re
import json

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")


embeddings = OpenAIEmbeddings(
    model=MODEL_NAME,
    openai_api_key=OPENAI_API_KEY
)

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_ENV,  # next to api key in console
)

index_name = PINECONE_INDEX_NAME

docsearch = Pinecone.from_existing_index(index_name, embeddings)

def get_recommendations(query):
    if query:
        
        try:
            query = query
            docs = docsearch.similarity_search(query, k = 30)

            recommendations = []

            for doc in docs:
                prod_id = re.findall(r'id:\s*\s*(\w+)\s*.*title:\s*\s*', doc.page_content)
                recommendations.append(prod_id[0])

            response = {"response": recommendations}
            
            return response
        
        except:
            response = {"response": "No Item Found"}
            return response
    
    else:
        response = {"response": "Enter a Valid Search Query"}
        return response
