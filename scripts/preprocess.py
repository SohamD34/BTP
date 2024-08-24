import os
import sys
os.chdir('/home/raid/Desktop/Soham/BTP/')
sys.path.append(os.getcwd())

from utils.preprocessing import slice_datasets, drop_columns, rename_columns
import pandas as pd


data = pd.read_excel('data/CFU per mL Analyte1_analyte2_analyte3_Sensor1_Sensor2_Sensor3.xlsx')

analyte_1, analyte_2, analyte_3 = slice_datasets(data)
[analyte_1, analyte_2, analyte_3] = drop_columns([analyte_1, analyte_2, analyte_3])
[analyte_1, analyte_2, analyte_3] = rename_columns([analyte_1, analyte_2, analyte_3])

analyte_1.to_csv('data/Analyte1.csv')
analyte_2.to_csv('data/Analyte2.csv')
analyte_3.to_csv('data/Analyte3.csv')