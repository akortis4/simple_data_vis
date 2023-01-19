# simple_data_vis

#Quick overview
This project is a meant to be a simple data summary and
data visualization tool. The purpose of this program is 
to take user input, a data file, and export an excel with
simple data summary and charts. It will also export all
charts as there own png file to be used in other
applications.

#User Input
This will be a json file with specific user inputs.
file_name --> (string) file directory and name
delimiter --> (string) the delimiter used in the file
dependent_variable --> (string) the column name of the dependent varible, y-axis on charts 
as_object --> (list) list of strings of variables that may be being read as numeric but need to be treated as objects
export_folder --> (string) file path to be used for saving the exported data
chart_png_export --> (bool) default to False, will tell the program to export charts to png objects

#Data set
I will be using the train.csv data set from Kaggle.com's housing prediciton training competition.
It is located here:
https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data
In theory this initial version should work with in csv data set.

#Ouput
1. Excel
The first output will be a an excel that notates the dependent variable chosen, and a drop down for
all numeric (int, float) independent variables to selected. Once an indpendent variable several
metrics will be filled in:
Min
25%
Mean
Median
75%
Max
Variance
Standard Deviation
And a scatter plot chart will be filled plotting the independent variable to the dependent variable

2. Scatter plot charts as png's
These will be a full set of scatter charts saved as png to used in other applications, if
chart_png_export = True

#Python Version
3.11

#Dependent External Modules
These modules will need to be install before running the program
pandas
matplotlib
openpyxl
json --> most likely installed by default

#Module Descriptions
SimpleDataVis --> main module used to call and create all other classes
UserInputHandler --> module to store user input from json input file
ReadData --> module used to handle loading of data and creating it as a dataframe
CreateExcel --> module used to create and format excel, store defualt excel formatting, and writing data to excel
CreatePlotPng --> module used to create scatter plot pngs