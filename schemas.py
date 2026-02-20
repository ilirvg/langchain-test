from pydantic import BaseModel, Field
from typing import List

class Source(BaseModel):
    """
    Schema for the source used by the agent
    """
    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """
    Schema for response that the agent generates. It has the answer and the sources
    """
    answer: str = Field(description="The agents answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of URL links used when generating the response")