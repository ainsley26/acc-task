from data_handler import *

print(f'Running test...')
print(f'Load the data set from csv')

names = DataHandler(csv_path='name_gender.csv')
print(len(names.data_set))
