from dataclasses import dataclass
from typing import Optional, Dict, Any

from langchain_payman_tool.tool import PaymanAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_core.runnables import RunnableConfig, chain

@dataclass
class PaychainConfig:
    model: str = "gpt-4"
    temperature: float = 0.7
    max_tokens: int = 150
    additional_tools: list = None

class PaychainProcessor:
    def __init__(self, config: Optional[PaychainConfig] = None):
        self.config = config or PaychainConfig()
        self.setup_chain()

    def setup_chain(self):
        # Initialize Payman tool
        self.payman_tool = PaymanAI(
            name="send_payment",
            description="Send a payment to a specified payee."
        )

        # Create prompt template
        self.prompt = ChatPromptTemplate([
            ("system", "You are a helpful AI that can process payments safely and efficiently."),
            ("human", "{user_input}"),
            ("placeholder", "{messages}")
        ])

        # Setup LLM and chain
        self.llm = ChatOpenAI(
            model=self.config.model,
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens
        )
        
        self.llm_with_tools = self.llm.bind_tools(
            [self.payman_tool], 
            tool_choice=self.payman_tool.name
        )

        self.chain = self.prompt | self.llm_with_tools

    @chain
    def process(self, user_input: str, config: Optional[RunnableConfig] = None) -> Dict[str, Any]:
        """
        Process a payment request in natural language.
        
        Args:
            user_input (str): Natural language payment request
            config (Optional[RunnableConfig]): Optional configuration
            
        Returns:
            Dict[str, Any]: Processing result
        """
        input_data = {"user_input": user_input}
        ai_response = self.chain.invoke(input_data, config=config)
        tool_messages = self.payman_tool.batch(ai_response.tool_calls, config=config)
        
        return self.chain.invoke(
            {**input_data, "messages": [ai_response, *tool_messages]},
            config=config
        ) 