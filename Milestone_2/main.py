from langchain_community.chat_models import ChatOllama
from langchain.agents import initialize_agent, AgentType

from tools import calculator, weather_tool, unit_converter_tool, time_tool, fact_tool


# Load local model
llm = ChatOllama(model="phi3:mini", temperature=0)

tools = [calculator, weather_tool, unit_converter_tool, time_tool, fact_tool]


agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=1,  # 🔴 prevents infinite loops
)


while True:

    user_input = input("\nAsk something (type 'exit' to quit): ")

    if user_input.lower() == "exit":
        break

    try:
        response = agent.invoke({"input": user_input})
        print("\nFinal Answer:", response["output"])

    except Exception as e:
        print("Error:", e)
