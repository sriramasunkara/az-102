import os
from dotenv import load_dotenv
from typing import List, Dict

# Add references
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


def get_openai_client(api_version: str = "2024-10-21"):
    """Initialize and return an OpenAI client obtained from AIProjectClient.

    Returns a tuple: (openai_client, model_deployment)
    """
    load_dotenv()
    project_endpoint = os.getenv("PROJECT_ENDPOINT")
    model_deployment = os.getenv("MODEL_DEPLOYMENT")

    if not project_endpoint:
        raise ValueError("PROJECT_ENDPOINT environment variable is not set")
    if not model_deployment:
        raise ValueError("MODEL_DEPLOYMENT environment variable is not set")

    project_client = AIProjectClient(
        credential=DefaultAzureCredential(
            exclude_environment_credential=True,
            exclude_managed_identity_credential=True,
        ),
        endpoint=project_endpoint,
    )

    openai_client = project_client.get_openai_client(api_version=api_version)
    return openai_client, model_deployment


def get_completion(openai_client, model_deployment: str, messages: List[Dict]) -> str:
    """Send messages to the chat completions API and return the assistant reply text."""
    response = openai_client.chat.completions.create(model=model_deployment, messages=messages)
    completion = response.choices[0].message.content
    return completion


def main():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        openai_client, model_deployment = get_openai_client()

        # Initialize prompt with system message
        prompt = [
            {"role": "system", "content": "You are a helpful AI assistant that answers questions."}
        ]

        # Loop until the user types 'quit'
        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            # Get a chat completion
            prompt.append({"role": "user", "content": input_text})
            completion = get_completion(openai_client, model_deployment, prompt)
            print(completion)
            prompt.append({"role": "assistant", "content": completion})

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()