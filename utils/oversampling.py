import pandas as pd
from imblearn.over_sampling import RandomOverSampler

for i in range(1,4):
    
    analyte = pd.read_csv(f'data/Analyte{i}.csv')

    ros = RandomOverSampler()

    analyte_oversampled, _ = ros.fit_resample(analyte, analyte['CFU/mL'])
    analyte_oversampled.to_csv(f'data/Analyte{i}_oversampled.csv', index=False)

print('Oversampling complete')