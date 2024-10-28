# BTP
ML Architecture for Classification of Biosensors Data

## Tasks

Two main tasks are to be performed:
1. Clustering of datapoints into different analyte classes
2. Seperation of various solutions - concentrated analytes, mixtures of various concentrations
3. Prediction of CFU concentration (/mL) from the sensor readings

## Approach

1. Data Cleaning and Preprocessing
2. Feature Engineering - log scale, exponential scale, PCA, LDA
3. Clustering - KMeans, DBSCAN
4. Classification - SVM, RFC
5. Addition of noisy samples - increasing robustness

## Directory Guidelines

~~~
root
|--------- .gitignore
|--------- requirements.txt
|--------- environment.yml
|--------- Makefile
|--------- LICENSE
|--------- README.md
|--------- data
|           |------- exponential
|           |------- labelled
|           |------- mixture
|           |------- raw
|           |------- sampled
|           |------- time_data
|           |------- unsampled
|--------- docs
|           |------- logs
|           |------- plots
|--------- scripts
|           |------- README.md
|           |------- 3 Analytes
|                     |------- Random Forest
|                     |------- SVM
|           |------- Clustering
|           |------- Interpolation
|           |------- Mixtures + Analytes
|                     |------- 4 Mixtures
|                     |------- 5 Mixtures
|                     |------- 8 Mixtures
|--------- utils
|           |------- README.md
|           |------- preprocess.py
|           |------- utils.py
~~~
