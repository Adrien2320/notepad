class Data:
    def __init__(self):
        self.text = ""

    def save(self):
        with open("data.txt", "a+") as file:
            file.write(self.text)
