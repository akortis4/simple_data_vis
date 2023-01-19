#module import
import os
import sys
import pandas as pd

#user created module import
from modules.UserInputHandler import ReadJson
from modules.ReadDataHandler import ReadCsv

class SimpleDataVis():
    def __init__(self):
        self.input_file = sys.argv[1]

    def main(self):
        if not os.path.isfile(self.input_file):
            print(f'The input file can not be found\nPlease check your path and file name:\n{self.input_file}')
            print('Press any key to exit the program.')
            input()
            sys.exit()
        user_input = ReadJson(self.input_file).user_input
        data_df = ReadCsv(user_input['file_name'], user_input['delimiter'])
        print(data_df.data_df)

if __name__ == '__main__':
    SimpleDataVis().main()