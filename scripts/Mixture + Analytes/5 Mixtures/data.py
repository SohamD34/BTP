import pandas as pd
import os
os.chdir('/home/soham/Desktop/GitHub/BTP/')

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


total_new_data = pd.concat([analyte1, analyte2, analyte3, mix_111, mix_101], axis=0).reset_index(drop=True)

total_new_data.to_csv('data/mixture/5 solutions/total_new_data(5 mixtures).csv', index=False)
total_new_data.to_excel('data/mixture/5 solutions/total_new_data(5 mixtures).xlsx', index=False)

del analyte1, analyte2, analyte3, mix_111, mix_101, mix_111_sensor1, mix_111_sensor2, mix_111_sensor3


#____________________________________________________________________________________________________________________________________________________________________#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#

