"""
Design a class Msg that models an e-mail message.
A message has a recipient, a sender, and a message text.
"""


class Msg:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text

    def append(self, new_text):
        self.text += '\n\t\t' + new_text

    def __str__(self):
        return "From {}\nTo: {}\nContent: {}".format(self.sender, self.recipient, self.text)


if __name__ == '__main__':
    sender = input('input a sender : ')
    recipient = input('input a recipient : ')
    text = input('input a text (endpoint is .) : ')

    message = Msg(sender, recipient, text)
    while True:
        new_text = input()
        message.append(new_text)

        if new_text == ".":
            break

    print(message)
