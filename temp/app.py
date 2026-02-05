import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "gpt-4o-mini"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


messages = [
    SystemMessage("You need to reply in kannada"),
]

print("Chatbot started. Type 'exit' or 'quit' to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append(UserMessage(user_input))

    response = client.complete(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model
    )

    assistant_response = response.choices[0].message.content
    print("Bot:", assistant_response)
    messages.append(AssistantMessage(assistant_response))
