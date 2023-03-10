#module import
import json

#class that reads in json file and stores inputs as a dictionary
class ReadJson():
    def __init__(self, file_name:str):
        self.file_name = file_name
        self.user_input = None
        self.execute()

    def execute(self):
        f = open(self.file_name)
        self.user_input = json.load(f)
        self.user_input
