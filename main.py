from dotenv import load_dotenv
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()
llm = ChatOpenAI(model="gpt-4o")
tools = [TavilySearch()]
react_prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)
agent_excutor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
chain = agent_excutor

def main():
    result = chain.invoke(input={"input": "Search 3 jobs listing for ai engineer using langchian, works should be remote, and list tehire details",})
    print(result)

if __name__ == "__main__":
    main()
