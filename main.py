from dotenv import load_dotenv
from pydantic import BaseModel
#from langchain_openai import ChatOpenAI # for openai
#from langchain_anthropic import ChatAnthropic # for claude
# from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool,wiki_tool,save_tool

load_dotenv()

# llm2= ChatOpenAI(model="gpt-4o-mini") I am going to use claude 
class ResearchResponse(BaseModel):
    topic:str
    summary:str
    sources: list[str]
    tools_used: list[str]


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                             temperature=0,
                             max_tokens=None,
                             timeout=None,
                              max_retries=2,
                              )

parser= PydanticOutputParser(pydantic_object=ResearchResponse)

prompt=ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and  save the research result also using necessary tools
            Wrap the outputs in this format and provide no other text\n{format_instructions}
            """),
            ("placeholder","{chat_history}"),
            ("human","{query}"),
            ("placeholder","{agent_scratchpad}"),
        
    ]
).partial(format_instructions=parser.get_format_instructions())


tools= [search_tool,wiki_tool,save_tool]
agent=create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("What can I help you research?")
raw_response=agent_executor.invoke({"query": query })

try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    print(structured_response)
except Exception as e:
    print("Error parsing response", e, "Raw Response - ", raw_response)