#module import
import os
import pandas as pd
import matplotlib.pyplot as plt

#class to take pandas dataframe and create scatter plots
#using matplotlib and save those as png files
class CreatePlots():
    def __init__(self, data_drame:pd.DataFrame, dep_var:str, ind_vars:list, export:str):
        self.data_frame = data_drame
        self.dep_var = dep_var
        self.ind_vars = ind_vars
        self.export = export
        self.execute()

    def execute(self):
        self.create_scatter()

    def create_scatter(self):
        y = list(self.data_frame[self.dep_var].values)
        for ind_var in self.ind_vars:
            x = list(self.data_frame[ind_var].values)
            plt.scatter(x, y)
            plt.savefig(f'{self.export}/{ind_var}_vs_{self.dep_var}.png')
            plt.clf()
            