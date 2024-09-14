import pandas as pd
import numpy as np

input_file = "/content/Analyte1.csv"
df = pd.read_csv(input_file)

def generate_interpolated_data(start, end, num_points):
    return np.linspace(start, end, num_points + 2)[1:-1]  

all_interpolated_data = {col: [] for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']}

for index in range(len(df) - 1):  
    num_points = 2 ** (9 - index) 

    for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']:
        start = df.iloc[index][col]    
        end = df.iloc[index + 1][col]   
        interpolated_values = generate_interpolated_data(start, end, num_points)
        all_interpolated_data[col].extend(interpolated_values)

interpolated_df = pd.DataFrame(all_interpolated_data)

output_file = r"C:\Analyte1_interpolated_data.csv"
interpolated_df.to_csv(output_file, index=False)

print(f"Interpolated data saved to {output_file}")

#__________________________________________________________________________________________


input_file = "/content/Analyte2.csv"
df = pd.read_csv(input_file)

def generate_interpolated_data(start, end, num_points):
    return np.linspace(start, end, num_points + 2)[1:-1] 

all_interpolated_data = {col: [] for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']}

for index in range(len(df) - 1):  
    num_points = 2 ** (9 - index)  

    for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']:
        start = df.iloc[index][col]    
        end = df.iloc[index + 1][col] 
        interpolated_values = generate_interpolated_data(start, end, num_points)
        all_interpolated_data[col].extend(interpolated_values)


interpolated_df = pd.DataFrame(all_interpolated_data)

output_file = r"C:\Analyte2_interpolated_data.csv"
interpolated_df.to_csv(output_file, index=False)

print(f"Interpolated data saved to {output_file}")


#__________________________________________________________________________________________


input_file = "/content/Analyte3.csv"
df = pd.read_csv(input_file)

def generate_interpolated_data(start, end, num_points):
    return np.linspace(start, end, num_points + 2)[1:-1]  

all_interpolated_data = {col: [] for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']}

for index in range(len(df) - 1):  
    num_points = 2 ** (9 - index)  

    for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']:
        start = df.iloc[index][col]   
        end = df.iloc[index + 1][col]  
        interpolated_values = generate_interpolated_data(start, end, num_points)
        all_interpolated_data[col].extend(interpolated_values)

interpolated_df = pd.DataFrame(all_interpolated_data)


output_file = r"C:\Analyte3_interpolated_data.csv"
interpolated_df.to_csv(output_file, index=False)

print(f"Interpolated data saved to {output_file}")