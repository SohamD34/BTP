import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def fill_nan(df):
    """
    Fill NaN values in a DataFrame with the mean of the column.
    """
    return df.fillna(0)


def scale_features(df, features):
    """
    Scale the features of a DataFrame.
    """
    scaler = MinMaxScaler()
    columns = [i for i in features if i != 'Label']
    
    for col in columns:
        df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))

    return df


def analyte_vs_sensor(df, analyte, sensor):
    """
    Filter a DataFrame by analyte and sensor.
    """
    sensor_reading = list(df[sensor])
    conc = list(df['CFU/mL'])
    
    plt.figure(figsize=(4,3))
    plt.plot(conc, sensor_reading)
    plt.xlabel('Concentration (CFU/mL)')
    plt.ylabel(f'{sensor} Reading')
    plt.title(f'{analyte} vs {sensor}')
    plt.show()