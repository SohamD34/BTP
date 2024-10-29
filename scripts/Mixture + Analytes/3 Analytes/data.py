import os
os.chdir('/home/soham/Desktop/GitHub/BTP/')
import pandas as pd
import numpy as np

analyte1 = pd.read_csv('data/unsampled/Unsampled_Analyte1.csv').drop(['CFU/mL'], axis=1)
analyte2 = pd.read_csv('data/unsampled/Unsampled_Analyte2.csv').drop(['CFU/mL'], axis=1)
analyte3 = pd.read_csv('data/unsampled/Unsampled_Analyte3.csv').drop(['CFU/mL'], axis=1)

mix_111_sensor1 = pd.read_excel('data/time_data/ratio_111/Sensor 1_111.xlsx')

analyte1['Dilution'] = mix_111_sensor1['Dilutions']
analyte1['Label'] = ['A1' for i in range(len(analyte1))]

analyte2['Dilution'] = mix_111_sensor1['Dilutions'] 
analyte2['Label'] = ['A2' for i in range(len(analyte2))]

analyte3['Dilution'] = mix_111_sensor1['Dilutions']
analyte3['Label'] = ['A3' for i in range(len(analyte3))]

total_data = pd.concat([analyte1, analyte2, analyte3], axis=0)
total_data = total_data[['Sensor1', 'Sensor2', 'Sensor3', 'Dilution', 'Label']]

total_data.to_csv('data/mixture/3 solutions/total_data.csv', index=False)
total_data.to_excel('data/mixture/3 solutions/total_data.xlsx', index=False)

del analyte1, analyte2, analyte3, mix_111_sensor1