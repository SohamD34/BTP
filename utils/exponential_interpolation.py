import pandas as pd
import numpy as np


def exponential_interpolation():


    def generate_interpolated_data(start, end, num_points):
        return np.linspace(start, end, num_points + 2)[1:-1] 

    input_file = "/content/Analyte1.csv"
    df = pd.read_csv(input_file)
    all_interpolated_data = {col: [] for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']}

    for index in range(len(df) - 1):  
        num_points = 2 ** (9 - index) 
        for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']:
            start = df.iloc[index][col]    
            end = df.iloc[index + 1][col]   
            interpolated_values = generate_interpolated_data(start, end, num_points)
            all_interpolated_data[col].extend(interpolated_values)

    interpolated_df = pd.DataFrame(all_interpolated_data)
    output_file = r'data/exponential/Exponential_Analyte1.csv'
    interpolated_df.to_csv(output_file, index=False)
    print(f"Interpolated data saved to {output_file}")


    input_file = "/content/Analyte2.csv"
    df = pd.read_csv(input_file)
    all_interpolated_data = {col: [] for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']}

    for index in range(len(df) - 1):  
        num_points = 2 ** (9 - index)  
        for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']:
            start = df.iloc[index][col]    
            end = df.iloc[index + 1][col] 
            interpolated_values = generate_interpolated_data(start, end, num_points)
            all_interpolated_data[col].extend(interpolated_values)


    interpolated_df = pd.DataFrame(all_interpolated_data)
    output_file = r'data/exponential/Exponential_Analyte2.csv'
    interpolated_df.to_csv(output_file, index=False)
    print(f"Interpolated data saved to {output_file}")



    input_file = "/content/Analyte3.csv"
    df = pd.read_csv(input_file)
    all_interpolated_data = {col: [] for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']}

    for index in range(len(df) - 1):  
        num_points = 2 ** (9 - index)  
        for col in ['CFU/mL', 'Sensor1', 'Sensor2', 'Sensor3']:
            start = df.iloc[index][col]   
            end = df.iloc[index + 1][col]  
            interpolated_values = generate_interpolated_data(start, end, num_points)
            all_interpolated_data[col].extend(interpolated_values)

    interpolated_df = pd.DataFrame(all_interpolated_data)
    output_file = r'data/exponential/Exponential_Analyte3.csv'
    interpolated_df.to_csv(output_file, index=False)
    print(f"Interpolated data saved to {output_file}")



if __name__ == '__main__':
    exponential_interpolation()
    print('Exponential Interpolation complete')