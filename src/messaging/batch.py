class MiniBatch:
    def __init__(self, start_time):
        self.start_time = start_time
        self.messages = []

    def add(self, message):
        self.messages.append(message)

    def __len__(self):
        return len(self.messages)
