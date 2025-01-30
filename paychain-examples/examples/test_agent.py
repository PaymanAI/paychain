import os
from dotenv import load_dotenv
from typing import List

# Load environment variables first
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_payman_tool import (
    SendPaymentTool,
    SearchPayeesTool,
    AddPayeeTool,
    AskForMoneyTool,
    GetBalanceTool
)

def create_payment_agent():
    # Initialize all tools
    tools = [
        SendPaymentTool(),
        SearchPayeesTool(),
        AddPayeeTool(),
        AskForMoneyTool(),
        GetBalanceTool()
    ]
    
    # Create the prompt template - Removed chat_history
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful payment processing assistant that can help with sending payments, 
        managing payees, and checking balances. You have access to various payment tools and will use them
        appropriately based on user requests.
        
        Always verify amounts and payee information before processing payments.
        If you're unsure about any details, ask for clarification."""),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    # Initialize the LLM
    llm = ChatOpenAI(temperature=0)
    
    # Create the agent
    agent = create_openai_functions_agent(llm, tools, prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    return agent_executor

def test_agent():
    agent = create_payment_agent()
    
    # Test cases
    test_queries = [
        "What's my current balance?",
        "Search for a payee named Alice",
        "Add a payee named Alice, make a mock routing and account number for testing"
        "Send $5 to Alice"
    ]
    
    for query in test_queries:
        print(f"\n\nTesting query: {query}")
        print("-" * 50)
        try:
            response = agent.invoke({"input": query})
            print("Response:", response)
        except Exception as e:
            print(f"Error processing query: {str(e)}")

if __name__ == "__main__":
    test_agent() 