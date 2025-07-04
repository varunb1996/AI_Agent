from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
store = FAISS.from_texts(["Agent initialized"], OpenAIEmbeddings())
store.save_local("data/vector_store")