import pandas as pd
from imblearn.over_sampling import RandomOverSampler

analyte1 = pd.read_csv('../data/Analyte1.csv')
analyte2 = pd.read_csv('../data/Analyte2.csv')
analyte3 = pd.read_csv('../data/Analyte3.csv')

ros = RandomOverSampler()

analyte1_oversampled, _ = ros.fit_resample(analyte1, analyte1['CFU/mL'])
analyte1_oversampled.to_csv('../data/Analyte1_oversampled.csv', index=False)

analyte2_oversampled, _ = ros.fit_resample(analyte2, analyte2['CFU/mL'])
analyte2_oversampled.to_csv('../data/Analyte2_oversampled.csv', index=False)

analyte3_oversampled, _ = ros.fit_resample(analyte3, analyte3['CFU/mL'])
analyte3_oversampled.to_csv('../data/Analyte3_oversampled.csv', index=False)

print('Oversampling complete')