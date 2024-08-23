import pandas as pd 

data = pd.read_excel('../data/CFU per mL Analyte1_analyte2_analyte3_Sensor1_Sensor2_Sensor3.xlsx')

# We have 10 points of Analyte1 data, Analyte2 data and Analyte3 data respectively.

data = data.drop(['Unnamed: 4', 'Unnamed: 8'], axis=1)

analyte1 = data.iloc[1:11, :]
analyte2 = data.iloc[11:21, :]
analyte3 = data.iloc[21:31, :]

# Extracting the data for each analyte and sensor combination into separate CSV files.

analyte1_data = analyte1.drop(['Analyte2_sensor1', 'Analyte2_sensor2', 'Analyte2_sensor3', 'Analyte3_Sensor1', 'Analyte3_Sensor2', 'Analyte3_Sensor3'], axis=1)
analyte1_data.to_csv('../data/Analyte1.csv', index=False)

analyte2_data = analyte2.drop(['Analyte1_Sensor1', 'Analyte1_Sensor2', 'Analyte1_Sensor3', 'Analyte3_Sensor1', 'Analyte3_Sensor2', 'Analyte3_Sensor3'], axis=1)
analyte2_data.to_csv('../data/Analyte2.csv', index=False)

analyte3_data = analyte3.drop(['Analyte1_Sensor1', 'Analyte1_Sensor2', 'Analyte1_Sensor3', 'Analyte2_sensor1', 'Analyte2_sensor2', 'Analyte2_sensor3'], axis=1)
analyte3_data.to_csv('../data/Analyte3.csv', index=False)