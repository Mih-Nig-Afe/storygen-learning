from google.adk.agent import Agent
from google.adk.components import Act, Generate
from .imagen_tool import ImagenTool

# Define the root agent for image generation
root_agent = Agent(
    name="ImageGenerator",
    description="An agent that generates images based on provided descriptions.",
    components=[
        Act(
            tool=ImagenTool(),
            # The input to the tool will be the raw text content of the message.
            # The tool expects a dictionary with 'prompt' as a key.
            # The agent will extract the 'prompt' from the incoming message and pass it to the tool.
            parameters={
                "prompt": "{{ .last_user_message.text }}"
            }
        ),
        Generate(
            prompt="Return the tool output as a JSON object."
        )
    ]
)
