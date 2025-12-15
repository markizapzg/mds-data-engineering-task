class Bucket:
    def __init__(self):
        self.files = []
        self.size = 0

    def add(self, file):
        self.files.append(file)
        self.size += file.size
