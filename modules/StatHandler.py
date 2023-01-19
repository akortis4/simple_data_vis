#module import
import sys
import pandas as pd

#class to take the dataframe and create stats for
#dependent and indepent variables
class CreateStats():
    def __init__(self, data_frame:pd.DataFrame, dependent_var:str, exclude:list):
        self.data_frame = data_frame
        self.dependent_var = dependent_var
        self.exclude = exclude
        self.stat_data = {'dep_var': {}, 'ind_var': {}}
        self.execute()

    def execute(self):
        if self.dependent_var == '':
            print('No dependent variable defined in json.')
            print('Press any key to exit.')
            input()
            sys.exit()
        self.create_dep_stats()
        self.create_ind_stats()

    def calc_stats(self, data):
        dep_min = float(data.min())
        dep_25 = float(data.quantile(.25))
        dep_mean = float(data.mean())
        dep_median = float(data.median())
        dep_75 = float(data.quantile(.75))
        dep_max = float(data.max())
        dep_var = float(data.var())
        dep_std = float(data.std())
        stat_dict = {'Minimum': dep_min,
                    '25%': dep_25,
                    'Mean': dep_mean,
                    'Median': dep_median,
                    '75%': dep_75,
                    'Maximum': dep_max,
                    'Variance': dep_var,
                    'Standard': dep_std}
        return stat_dict

    def create_dep_stats(self):
        self.stat_data['dep_var'] = {self.dependent_var: self.calc_stats(self.data_frame[self.dependent_var].copy())}

    def create_ind_stats(self):
        columns = list(self.data_frame.columns)
        for col in columns:
            if len(self.exclude) > 0 and col in self.exclude:
                continue
            if str(self.data_frame[col].dtypes) in ('int64', 'float64'):
                if col != self.dependent_var:
                    self.stat_data['ind_var'][col] = self.calc_stats(self.data_frame[col].copy())
