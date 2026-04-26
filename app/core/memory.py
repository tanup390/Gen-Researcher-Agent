class SimpleMemory:
    def __init__(self):
        self.history = []

    def add(self, user_input, response):
        self.history.append({
            "user": user_input,
            "assistant": response
        })

    def get_history(self):
        formatted = ""
        for h in self.history:
            formatted += f"User: {h['user']}\nAssistant: {h['assistant']}\n"
        return formatted