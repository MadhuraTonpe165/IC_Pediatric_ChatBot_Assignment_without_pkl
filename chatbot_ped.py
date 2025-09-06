# chatbot_ped.py
import openai

class PediatricChatbot:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": "You are a Pediatrician specialize in pre-teens and teens, child abuse, or children's developmental issues."
            }
        ]

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_response(self, model="gpt-3.5-turbo"):
        response = openai.ChatCompletion.create(
            model=model,
            messages=self.messages
        )
        reply = response["choices"][0]["message"]["content"]
        self.add_message("assistant", reply)
        return reply
