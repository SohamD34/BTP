import pandas as pd
import numpy as np
import os

def linear_interpolation():
    data1 = pd.read_csv('data/unsampled/Unsampled_Analyte1.csv')
    dummy_data1 = data1.copy()

    for i in range(1, len(data1)):
        if (data1.iloc[i, 0] != data1.iloc[i-1, 0]):
            high = data1.iloc[i, :]
            low = data1.iloc[i-1, :]
            mean = (high + low) / 2
            std_dev = np.abs(high - low) / 2
            samples = np.random.normal(loc=mean, scale=std_dev/10, size=(10, len(data1.columns)))
            dummy_data1 = pd.concat([dummy_data1, pd.DataFrame(samples, columns=data1.columns)], ignore_index=True)

    dummy_data1 = dummy_data1.sort_values(by='CFU/mL').reset_index(drop=True)



    data2 = pd.read_csv('data/unsampled/Unsampled_Analyte2.csv')
    dummy_data2 = data2.copy()

    for i in range(1, len(data2)):
        if (data2.iloc[i, 0] != data2.iloc[i-1, 0]):
            high = data2.iloc[i, :]
            low = data2.iloc[i-1, :]
            mean = (high + low) / 2
            std_dev = np.abs(high - low) / 2
            samples = np.random.normal(loc=mean, scale=std_dev/4, size=(10, len(data2.columns)))
            dummy_data2 = pd.concat([dummy_data2, pd.DataFrame(samples, columns=data2.columns)], ignore_index=True)

    dummy_data2 = dummy_data2.sort_values(by='CFU/mL').reset_index(drop=True)



    data3 = pd.read_csv('data/unsampled/Unsampled_Analyte3.csv')
    dummy_data3 = data3.copy()

    for i in range(1, len(data3)):
        if (data3.iloc[i, 0] != data3.iloc[i-1, 0]):
            high = data3.iloc[i, :]
            low = data3.iloc[i-1, :]
            mean = (high + low) / 2
            std_dev = np.abs(high - low) / 2
            samples = np.random.normal(loc=mean, scale=std_dev/4, size=(10, len(data3.columns)))
            dummy_data3 = pd.concat([dummy_data3, pd.DataFrame(samples, columns=data3.columns)], ignore_index=True)

    dummy_data3 = dummy_data3.sort_values(by='CFU/mL').reset_index(drop=True)

    dummy_data1.to_csv('data/sampled/Sampled_Analyte1.csv', index=False)
    dummy_data2.to_csv('data/sampled/Sampled_Analyte2.csv', index=False)
    dummy_data3.to_csv('data/sampled/Sampled_Analyte3.csv', index=False)



if __name__ == '__main__':
    linear_interpolation()
    print('Linear interpolation complete')