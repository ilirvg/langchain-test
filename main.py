from dotenv import load_dotenv
from langchain_classic import hub
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from langchain_core.prompts import PromptTemplate, format_document
from langchain_core.runnables import RunnableLambda


from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schemas import AgentResponse

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")
tools = [TavilySearch()]
react_prompt = hub.pull("hwchase17/react")
structured_llm = llm.with_structured_output(AgentResponse)

react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input", "agent_scratchpad", "tool_names", "tools"]
).partial(format_instructions="")


agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt_with_format_instructions)

agent_excutor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
extract_output = RunnableLambda(lambda x: x["output"])
chain = agent_excutor | extract_output | structured_llm

def main():
    result = chain.invoke(input={"input": "Search 3 jobs listing for ai engineer using langchian, works should be remote, and list tehire details",})
    print(result)

if __name__ == "__main__":
    main()
