import npyscreen
from collections import deque


class ChatForm(npyscreen.FormBaseNew):
    def create(self):
        y, x = self.useable_space()
        self.chat_history = self.add(
            npyscreen.MultiLineEdit,
            relx=2,
            rely=2,
            width=x - 4,
            height=y - 6,
            editable=False,
        )
        self.new_message = self.add(
            npyscreen.MultiLineEdit, relx=2, rely=y - 4, width=x - 4
        )

    def on_ok(self):
        message = self.new_message.value
        self.chat_history.value += "You: " + message + "\n"
        self.new_message.value = (
            ""  # Effacer le champ de saisie après l'envoi du message
        )
        self.display()


class ChatApplication(npyscreen.StandardApp):
    def onStart(self):
        self.internal_queue = deque()  # Initialiser la file d'attente interne
        self.addForm("MAIN", ChatForm, name="Simple Chat")

    def main_loop(self):
        while True:
            if self.internal_queue:  # Vérifier si la file d'attente n'est pas vide
                yield self.internal_queue.pop()
            else:
                yield


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
