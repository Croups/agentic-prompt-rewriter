import streamlit as st
from typing import Optional
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
import nest_asyncio
from dotenv import load_dotenv
import os
import time

nest_asyncio.apply()
load_dotenv()

# Define the input schema
class GeneratePromptFromScratchInput(BaseModel):
    initial_intent: str = Field(description="The input text to generate the prompt from scratch")
    examples: Optional[str] = None    
    
class GeneratePromptFromScratchOutput(BaseModel):
    system_role: str = Field(description="The role/persona the AI should adopt")
    task_description: str = Field(description="Clear description of task")
    input_structure: str = Field(description="Structure of expected input variables with XML tags")
    step_by_step: str = Field(description="Detailed step-by-step instructions")
    output_format: str = Field(description="Expected format of the output with XML tags")
    guidelines: str = Field(description="Guidelines for the model to follow")
    constraints: str = Field(description="Any constraints or restrictions to follow")

class FinalPrompt(BaseModel):
    prompt : str 
    
# Initialize OpenAI model and agent
model = OpenAIModel("gpt-4")

GeneratePromptFromScratchAgent = Agent(
    model=model,
    result_type=GeneratePromptFromScratchOutput,
    deps_type=GeneratePromptFromScratchInput,
    system_prompt="""You are an AI Expert specialized in crafting detailed prompts for AI models."""
)

@GeneratePromptFromScratchAgent.system_prompt
async def add_deps(ctx: RunContext[GeneratePromptFromScratchInput]) -> str:
    return f"""Generate a comprehensive prompt for an AI model based on this intent: '{ctx.deps.initial_intent}'.
    Examples for reference: '{ctx.deps.examples if ctx.deps.examples else 'None provided'}'.
    The prompt should be detailed, structured, and include all necessary components for reliable AI execution."""

rewriter_agent = Agent(
    model=model,
    deps_type=GeneratePromptFromScratchOutput,
    result_type=FinalPrompt,
    system_prompt="You are an AI Expert that specializes in rewriting unstructured prompt to improve."
)

@rewriter_agent.system_prompt
async def add_deps(ctx: RunContext[GeneratePromptFromScratchOutput]) -> str:
    return f"""Rewrite the following prompt to be more structured and clear:
    {ctx.deps.system_role}
    {ctx.deps.task_description}
    {ctx.deps.input_structure}
    {ctx.deps.step_by_step}
    {ctx.deps.output_format}
    {ctx.deps.guidelines}
    {ctx.deps.constraints}
    
    Example final prompt should be like for given input (write an article):
    You are tasked with writing an article based on the given inputs. Follow these instructions carefully to produce a well-structured and engaging article.

You will be provided with the following inputs:
<topic>{{TOPIC}}</topic>
This is the main subject of your article. Ensure that your content remains focused on this topic throughout.

<word_count>{{WORD_COUNT}}</word_count>
This is the target length for your article. Aim to come within 10% of this word count.

<style>{{STYLE}}</style>
This describes the tone and approach you should use in your writing. Adapt your language and structure to match this style.

Before you begin writing, follow these steps:

1. Brainstorming and Outlining:
   - Spend a few minutes brainstorming key points related to the topic.
   - Create a basic outline with an introduction, 3-5 main points for the body, and a conclusion.

2. Writing the Introduction:
   - Start with a hook to grab the reader's attention.
   - Briefly introduce the topic and its importance.
   - End with a thesis statement that outlines the main points you'll cover.

3. Developing the Main Body:
   - Dedicate a paragraph to each main point from your outline.
   - Use topic sentences to introduce each paragraph's main idea.
   - Support your points with evidence, examples, or explanations.
   - Ensure smooth transitions between paragraphs.

4. Concluding the Article:
   - Summarize the main points discussed.
   - Restate the thesis in a new way.
   - End with a thought-provoking statement or call to action.

5. Proofreading and Editing:
   - Check for grammar and spelling errors.
   - Ensure the article flows logically and maintains the specified style.
   - Verify that you've met the target word count.

Present your final article within <article> tags. Include a word count at the end of your article, outside the <article> tags.

Remember to adhere to the given topic, word count, and style throughout your writing process. Good luck!
    
    """


def simulate_streaming(text: str, placeholder):
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(displayed_text)
        time.sleep(0.01)

def main():
    st.title("Agentic Prompt Generator")
    
    # Sidebar for API key
    with st.sidebar:
        st.header("Settings")
        api_key = st.text_input("Enter your OpenAI API Key:", type="password")
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
            st.success("API Key set successfully!", icon="✅")
        else:
            st.warning("Please enter your OpenAI API key to continue", icon="⚠️")
            st.stop()

    # User inputs
    initial_intent = st.text_input(
        "What is your initial prompt?", 
        placeholder="e.g., write an article, analyze sentiment, generate a story"
    )
    
    include_examples = st.checkbox("Include examples?")
    examples = None
    if include_examples:
        examples = st.text_area(
            "Enter examples:", 
            placeholder="Enter example inputs and outputs to guide the AI"
        )

    if st.button("Generate Prompt"):
        if initial_intent:
            try:
                import random
                
                stages = [
                    "Understanding the prompt...",
                    "Generating system role...",
                    "Templatizing the variables...",
                    "Determining the restrictions...",
                    "Setting up guidelines...",
                    "Creating step-by-step flow...",
                    "Structuring the output format...",
                    "Finalizing the prompt..."
                ]
                
                
                status_placeholder = st.empty()
                
                # First steps with random timing
                for stage in stages[:-1]:
                    status_placeholder.text(stage)
                    time.sleep(random.uniform(1.25, 2.5))
                
                # Final step with actual processing
                status_placeholder.text(stages[-1])
                
                input_data = GeneratePromptFromScratchInput(
                    initial_intent=initial_intent,
                    examples=examples
                )
                
                print(f"Input data generated: {input_data}")
                
                first_response = GeneratePromptFromScratchAgent.run_sync(
                    user_prompt=f"Create a detailed AI prompt for: {initial_intent}",
                    deps=input_data
                )
                
                print(f"Response generated: {first_response.data}")
                
                # Convert the first response to the expected input format for the second agent
                rewriter_input = GeneratePromptFromScratchOutput(
                    system_role=first_response.data.system_role,
                    task_description=first_response.data.task_description,
                    input_structure=first_response.data.input_structure,
                    step_by_step=first_response.data.step_by_step,
                    output_format=first_response.data.output_format,
                    guidelines=first_response.data.guidelines,
                    constraints=first_response.data.constraints
                )
                
                final_response = rewriter_agent.run_sync(
                    deps=rewriter_input, 
                    user_prompt="Rewrite the prompt to be more structured"
                )
                
                print(f"Rewritten prompt: {final_response.data}")
                
                output_placeholder = st.empty()
                st.success("Prompt generated successfully!", icon="✅")
                
                simulate_streaming(final_response.data.prompt, output_placeholder)
                
                st.download_button(
                    label="Download Prompt",
                    data=final_response.data.prompt,
                    file_name="ai_prompt.md",
                    mime="text/markdown"
                )
            except Exception as e:
                st.error(f"Error generating prompt: {str(e)}")
        else:
            st.error("Please enter what you want the AI to do")

if __name__ == "__main__":
    main()