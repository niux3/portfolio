import json

class Model:
    def __init__(self):
        self.path = None
        self.data = None

    def get(self, path):
        self.path = path
        with open(path, 'r') as fileJson:
            fileData = fileJson.read()
        fileJson.close()

        self.data = json.loads(fileData)
        return self.data
