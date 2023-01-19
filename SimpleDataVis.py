#module import
import os
import sys
import pandas as pd

#user created module import
from modules.UserInputHandler import ReadJson
from modules.ReadDataHandler import ReadCsv
from modules.StatHandler import CreateStats
from modules.CreateExcelHandler import CreateExcel

#main data visualization class
class SimpleDataVis():
    def __init__(self):
        self.input_file = sys.argv[1]

    def main(self):
        #check for json file if not present exit
        if not os.path.isfile(self.input_file):
            print(f'The input file can not be found\nPlease check your path and file name:\n{self.input_file}')
            print('Press any key to exit the program.')
            input()
            sys.exit()
        #store json inputs as dictionary
        user_input = ReadJson(self.input_file).user_input
        #store csv data as pandas dataframe
        data_df = ReadCsv(user_input['file_name'], user_input['delimiter'])
        stats = CreateStats(data_df.data_df, user_input['dependent_variable'], user_input['exclude'])
        CreateExcel(data_df.data_df, stats.stat_data, user_input['export_folder'])


#call main
if __name__ == '__main__':
    SimpleDataVis().main()