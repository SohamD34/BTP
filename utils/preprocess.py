import os
os.chdir('/home/soham/Desktop/GitHub/BTP/')

import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from utils.utils import slice_datasets, drop_columns, rename_columns
import sys
sys.path.append(os.getcwd())


def oversampling():
    for i in range(1,4):
        analyte = pd.read_csv(f'data/Analyte{i}.csv')
        ros = RandomOverSampler()
        analyte_oversampled, _ = ros.fit_resample(analyte, analyte['CFU/mL'])
        analyte_oversampled.to_csv(f'data/Analyte{i}_oversampled.csv', index=False)
    print('Oversampling complete')



def manage_null_concentration():
    data = pd.read_excel('data/CFU per mL Analyte1_analyte2_analyte3_Sensor1_Sensor2_Sensor3.xlsx')

    analyte_1, analyte_2, analyte_3 = slice_datasets(data)
    [analyte_1, analyte_2, analyte_3] = drop_columns([analyte_1, analyte_2, analyte_3])
    [analyte_1, analyte_2, analyte_3] = rename_columns([analyte_1, analyte_2, analyte_3])

    for a in [analyte_1, analyte_2, analyte_3]:
        a['CFU/mL'] = a['CFU/mL'].replace(0, 1)

    analyte_1.to_csv('data/unsampled/Unsampled_Analyte1.csv', index=False)
    analyte_2.to_csv('data/unsampled/Unsampled_Analyte2.csv', index=False)
    analyte_3.to_csv('data/unsampled/Unsampled_Analyte3.csv', index=False)



if __name__ == '__main__':
    manage_null_concentration()
    print('Null concentration managed')
    print('Data stored at - data/unsampled')