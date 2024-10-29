import pandas as pd
import os
os.chdir('/home/soham/Desktop/GitHub/BTP/')

all_data = pd.read_excel('data/mixture/Sensor 1_sensor 2_sensor 3_111_121_112_211.xlsx')
all_data.head(2)


# Mixture 1:1:1

mix_111_sensor1 = pd.read_excel('data/time_data/ratio_111/Sensor 1_111.xlsx')
mix_111_sensor2 = pd.read_excel('data/time_data/ratio_111/Sensor 2_111.xlsx')
mix_111_sensor3 = pd.read_excel('data/time_data/ratio_111/Sensor 3_111.xlsx')
mix_111 = pd.DataFrame()
mix_111['Dilution'] = mix_111_sensor1['Dilutions']
mix_111['Sensor1'] = mix_111_sensor1['Voltage sensor1_111']
mix_111['Sensor2'] = mix_111_sensor2['Voltage_sensor2_111']
mix_111['Sensor3'] = mix_111_sensor3['Voltage _sensor3_111']
mix_111['Label'] = ['Mix_111' for i in range(len(mix_111))]
mix_111 = mix_111[['Dilution','Sensor1','Sensor2','Sensor3','Label']]


# Analytes 1,2,3 - 100, 010, 001

analyte1 = pd.read_csv('data/unsampled/Unsampled_Analyte1.csv').drop(['CFU/mL'], axis=1)
analyte1['Dilution'] = mix_111['Dilution']
analyte1['Label'] = ['A1' for i in range(len(analyte1))]
analyte1 = analyte1[['Dilution','Sensor1','Sensor2','Sensor3','Label']]

analyte2 = pd.read_csv('data/unsampled/Unsampled_Analyte2.csv').drop(['CFU/mL'], axis=1)
analyte2['Dilution'] = mix_111['Dilution'] 
analyte2['Label'] = ['A2' for i in range(len(analyte2))]
analyte2 = analyte2[['Dilution','Sensor1','Sensor2','Sensor3','Label']]

analyte3 = pd.read_csv('data/unsampled/Unsampled_Analyte3.csv').drop(['CFU/mL'], axis=1)
analyte3['Dilution'] = mix_111['Dilution']
analyte3['Label'] = ['A3' for i in range(len(analyte3))]
analyte3 = analyte3[['Dilution','Sensor1','Sensor2','Sensor3','Label']]


# Mixture 1:0:1

mix_101 = pd.read_excel('data/time_data/ratio_101/all_sensors_101.xlsx').drop(['Dilutions'],axis=1)
mix_101['Sensor1'] = mix_101['Voltage _sensor1_analyte1_analyte3(1:1)']
mix_101['Sensor2'] = mix_101['Voltage _sensor2_analyte1_analyte3(1:1)']
mix_101['Sensor3'] = mix_101['Voltage _sensor3_analyte1_analyte3(1:1)']
mix_101 = mix_101.drop(['Voltage _sensor1_analyte1_analyte3(1:1)','Voltage _sensor2_analyte1_analyte3(1:1)','Voltage _sensor3_analyte1_analyte3(1:1)'], axis=1)
mix_101['Dilution'] = mix_111['Dilution']
mix_101['Label'] = ['Mix_101' for i in range(len(mix_101))]
mix_101 = mix_101[['Dilution','Sensor1','Sensor2','Sensor3','Label']]

# Mixture 1:2:1

mix_121 = pd.DataFrame()
mix_121['Sensor1'] = all_data['Sensor 1_121']
mix_121['Sensor2'] = all_data['Sensor2_121']
mix_121['Sensor3'] = all_data['Sensor 3_121']
mix_121['Label'] = ['Mix_121' for i in range(len(mix_121))]
mix_121['Dilution'] = mix_101['Dilution']
mix_121 = mix_121[['Dilution','Sensor1','Sensor2','Sensor3','Label']]

# Mixture 2:1:1

mix_211 = pd.DataFrame()
mix_211['Sensor1'] = all_data['Sensor1_ 211']
mix_211['Sensor2'] = all_data['Sensor2_ 211']
mix_211['Sensor3'] = all_data['Sensor3_ 211']
mix_211['Label'] = ['Mix_211' for i in range(len(mix_211))]
mix_211['Dilution'] = mix_101['Dilution']
mix_211 = mix_211[['Dilution','Sensor1','Sensor2','Sensor3','Label']]

# Mixture 1:1:2 

mix_112 = pd.DataFrame()
mix_112['Sensor1'] = all_data['Sensor1_ 112']
mix_112['Sensor2'] = all_data['Sensor2_ 112']
mix_112['Sensor3'] = all_data['Sensor3_ 112']
mix_112['Label'] = ['Mix_112' for i in range(len(mix_112))]
mix_112['Dilution'] = mix_101['Dilution']
mix_112 = mix_112[['Dilution','Sensor1','Sensor2','Sensor3','Label']]

all_data = pd.concat([analyte1, analyte2, analyte3, mix_101, mix_111, mix_112, mix_121, mix_211]).reset_index(drop=True)

all_data.to_csv('data/mixture/8 solutions/total_new_data(8 mixtures).csv', index=False)
all_data.to_excel('data/mixture/8 solutions/total_new_data(8 mixtures).xlsx', index=False)