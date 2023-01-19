import sys
import pandas as pd

class ReadCsv():
    def __init__(self, file_name:str, delimiter:str=','):
        self.file_name = file_name
        self.delimiter = delimiter
        self.data_df = pd.DataFrame()
        self.execute()

    def execute(self):
        try:
            self.data_df = pd.read_csv(self.file_name, header=0, sep=self.delimiter)
        except ImportError:
            print('Can not find file.\nPlease check file directory and path.')
            print(f'{self.file_name}')
            print('Press any key to exit.')
            input()
            sys.exit()
        return self.data_df