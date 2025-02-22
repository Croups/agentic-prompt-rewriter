from typing import Optional
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel

import nest_asyncio #type:ignore
from dotenv import load_dotenv
import os

nest_asyncio.apply()
load_dotenv()

## THIS IS A VERY BASIC EXPLANATION OF WHAT WE ARE GOING TO DO ACTUALLY. THE KEY POINT TO EXTRACT INSIGHTS FROM THE USER'S INTENT AND GENERATE THE FULL PROMPT
## AFTER GENERATING THE PROMPT, WE WILL USE THE GENERATED PROMPT TO GENERATE THE FINAL PROMPT WITH A REWRITER AGENT (it is implemented in the app.py)
## This is only for you to understand the concept. Run the app.py to see the full implementation

# DEFINE THE INPUT SCHEMA FOR GENERATE FROM STRATCH 

class GeneratePromptFromScratchInput(BaseModel):
    initial_intent : str = Field(description="The input text to generate the prompt from scratch")
    examples : Optional[str] = None    
    
class GeneratePromptFromScratchOutput(BaseModel):
    beginning_line : str = Field(description="Explaining what to do e.g. 'Summarize the following text'")
    variables : str = Field(description="variables to pass in the prompt, e.g. 'document', 'paragraph', 'topic'")
    instructions : str = Field(description="clear and well-structured instruction to the model e.g. 'First identify the topic, then summarize the text' ")
    examples : str = Field(description="Generate examples for the model to understand. ")
    guidelines : str = Field(description="Guidelines for the model to follow e.g. 'Be concise and clear'")
    restriction : str = Field(description="Restrictions for the model to follow e.g. 'Do not include any personal opinion'")
    

model = OpenAIModel("gpt-4o")

GeneratePromptFromScratchAgent = Agent(
    name = "GeneratePromptFromScratch Agent",
    model=model,
    result_type= GeneratePromptFromScratchOutput,
    deps_type=GeneratePromptFromScratchInput,
    system_prompt="You are an AI Expert on generating system prompts for AI models."
    )

@GeneratePromptFromScratchAgent.system_prompt
async def add_deps(ctx: RunContext[GeneratePromptFromScratchInput]) -> str:
    return f"Generate a detailed and well-structured prompt with user's intention. The user wants to generate a prompt from scratch with the intent:  '{ctx.deps.initial_intent}' and examples '{ctx.deps.examples}'."

if __name__ == "__main__":
    SampleUserDetails = GeneratePromptFromScratchInput(initial_intent="write a article")
    user_prompt = "Write a detailed article. Make sure it is interesting and engaging."
    response = GeneratePromptFromScratchAgent.run_sync(user_prompt=user_prompt, deps=SampleUserDetails)

    response.all_messages()
    print(response.result)
    
    