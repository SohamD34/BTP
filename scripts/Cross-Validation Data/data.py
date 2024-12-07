'''  Using data from time_data to create validation set - contains only Analyte 3 '''

import numpy as np
import pandas as pd

s1 = pd.read_excel('/home/soham/Desktop/GitHub/BTP/data/time_data/no_of_days/Sensor 1_no of days_analyte 3.xlsx')
s2 = pd.read_excel('/home/soham/Desktop/GitHub/BTP/data/time_data/no_of_days/Sensor 2_no of days_analyte 3.xlsx')
s3 = pd.read_excel('/home/soham/Desktop/GitHub/BTP/data/time_data/no_of_days/Sensor 3_no of days_analyte 3.xlsx')
s4 = pd.read_excel('/home/soham/Desktop/GitHub/BTP/data/time_data/no_of_days/Sensor 4 _no of days_analyte3.xlsx')

cols = ['Dil.1', 'Dil.2', 'Dil.3', 'Dil.4', 'Dil.5', 'Dil.6', 'Dil.7', 'Dil.8']

dataset = []

for i in range(5):
    row = np.random.randint(0, 7)
    col = np.random.randint(1, 8)

    point = [s1.iloc[row, col], s2.iloc[row, col], s3.iloc[row, col], s4.iloc[row, col], 3]
    dataset.append(point)

dataset = pd.DataFrame(dataset, columns=['Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Label'])

dataset.to_excel('/home/soham/Desktop/GitHub/BTP/data/validation_data/analyte3_validation_data.xlsx', index=False)