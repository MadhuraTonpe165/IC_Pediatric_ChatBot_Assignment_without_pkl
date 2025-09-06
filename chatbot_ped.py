# chatbot_ped.py
import openai

def system_prompt():
    """
    Returns the system role for the pediatric chatbot.
    """
    return {
        "role": "system",
        "content": "You are a Pediatrician specialize in pre-teens and teens, child abuse, or children's developmental issues."
    }

def add_message(messages, role, content):
    """
    Appends a new message to the conversation history.
    """
    messages.append({"role": role, "content": content})
    return messages

def get_response(messages, model="gpt-3.5-turbo"):
    """
    Calls OpenAI's API with the current message history and returns the assistant's reply.
    """
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    return response["choices"][0]["message"]["content"]
