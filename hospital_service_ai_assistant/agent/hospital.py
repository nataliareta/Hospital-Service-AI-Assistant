from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory

from tools.registration_info import registration_info_tool
from tools.doctor_schedule import doctor_schedule_tool
from tools.inpatient_info import inpatient_info_tool
from tools.general_info import general_info_tool

from dotenv import load_dotenv
load_dotenv()

def create_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )

    tools = [
        registration_info_tool,
        doctor_schedule_tool,
        inpatient_info_tool,
        general_info_tool
    ]

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        memory=memory,
        verbose=True
    )

    return agent