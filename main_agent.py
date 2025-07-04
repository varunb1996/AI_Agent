from langchain.agents import initialize_agent, AgentType, Tool
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_toolkits import PythonREPLTool
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import VectorStoreRetrieverMemory
from tools.search_tool import search
from tools.calc_tool import calculator

# Load vector memory
embedding = OpenAIEmbeddings()
vectordb = FAISS.load_local("data/vector_store", embedding)
retriever = vectordb.as_retriever(search_kwargs={"k": 3})
memory = VectorStoreRetrieverMemory(retriever=retriever)

llm = ChatOpenAI(model_name="gpt-4", temperature=0.3)

tools = [
    Tool(name="WebSearch", func=search, description="Search recent information online"),
    Tool(name="Calculator", func=calculator, description="Useful for math tasks"),
    PythonREPLTool(),
]

agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, memory=memory, verbose=True)

def run_agent_task(task):
    return agent.run(task)