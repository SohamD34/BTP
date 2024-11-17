import os
os.chdir('/home/soham/Desktop/GitHub/BTP/')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from typing import List



def slice_datasets(data: pd.DataFrame):
    ''' Slicing data according into different analytes '''
    analyte_1, analyte_2, analyte_3 = data.iloc[1:11,:], data.iloc[11:21,:], data.iloc[21:31,:]
    return analyte_1, analyte_2, analyte_3
    


def drop_columns(dfs:List[pd.DataFrame]) -> List[pd.DataFrame]:
    ''' Dropping unnecessary columns of each analyte data '''

    analyte1 = dfs[0].drop(['Analyte2_sensor2', 'Analyte3_Sensor2', 'Unnamed: 4', 'Analyte2_sensor1','Analyte3_Sensor1', 'Unnamed: 8','Analyte2_sensor3', 'Analyte3_Sensor3'], axis=1)
    analyte2 = dfs[1].drop(['Analyte1_Sensor2', 'Analyte3_Sensor2', 'Unnamed: 4', 'Analyte1_Sensor1','Analyte3_Sensor1', 'Unnamed: 8', 'Analyte1_Sensor3','Analyte3_Sensor3'], axis=1)
    analyte3 = dfs[2].drop(['Analyte1_Sensor2', 'Analyte2_sensor2', 'Unnamed: 4', 'Analyte1_Sensor1', 'Analyte2_sensor1','Unnamed: 8', 'Analyte1_Sensor3','Analyte2_sensor3'], axis=1)

    return [analyte1, analyte2, analyte3]




def rename_columns(dfs: List[pd.DataFrame]) -> List[pd.DataFrame]:
    ''' Rename all columns for a list of DataFrames for ease of use '''
    
    new_column_names = ['CFU/mL', 'Sensor2', 'Sensor1', 'Sensor3']

    for df in dfs:
        if len(df.columns.tolist()) == len(new_column_names):
            df.columns = new_column_names
        else:
            raise ValueError("The number of new column names does not match the number of columns in the DataFrame.")
    
    return dfs



def log_transform(dfs: List[pd.DataFrame]) -> List[pd.DataFrame]:
    ''' Log transform the CFU/mL column for each analyte data '''
    
    for df in dfs:
        df['log_sensor1'] = np.log(abs(df['Sensor1']))
        df['log_sensor2'] = np.log(abs(df['Sensor2']))
        df['log_sensor3'] = np.log(abs(df['Sensor3']))
    
    return dfs


def plot_clusters(features, data, pca_features, path):

    plt.figure(figsize=(15, 6))

    plt.subplot(1, 2, 1)
    scatter = plt.scatter(pca_features[:, 0], pca_features[:, 1], c=data['label'], cmap='magma', marker='o', edgecolor='k', s=100)
    plt.title('PCA Data with True Labels')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')

    # Create a legend for the scatter plot
    legend1 = plt.legend(*scatter.legend_elements(), title="Classes")
    plt.gca().add_artist(legend1)


    plt.subplot(1, 2, 2)
    scatter = plt.scatter(pca_features[:, 0], pca_features[:, 1], c=data['Cluster_PCA'], cmap='magma', marker='o', edgecolor='k', s=100)
    plt.title('PCA Data with KMeans Clusters')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')

    legend2 = plt.legend(*scatter.legend_elements(), title="Clusters")
    plt.gca().add_artist(legend2)

    plt.savefig(path)

    plt.show()


def plot_dbscan_clusters(features, data, pca_features, path):

    plt.figure(figsize=(15, 6))

    plt.subplot(1, 2, 1)
    scatter = plt.scatter(pca_features[:, 0], pca_features[:, 1], c=data['label'], cmap='magma', marker='o', edgecolor='k', s=100)
    plt.title('PCA Data with True Labels')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')

    # Create a legend for the scatter plot
    legend1 = plt.legend(*scatter.legend_elements(), title="Classes")
    plt.gca().add_artist(legend1)


    plt.subplot(1, 2, 2)
    scatter = plt.scatter(pca_features[:, 0], pca_features[:, 1], c=data['Cluster_PCA'], cmap='magma', marker='o', edgecolor='k', s=100)
    plt.title('PCA Data with DBSCAN Clusters')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')

    legend2 = plt.legend(*scatter.legend_elements(), title="Clusters")
    plt.gca().add_artist(legend2)

    plt.savefig(path)

    plt.show()



def plot_gmm_clusters(features, data, pca_features, path):

    plt.figure(figsize=(15, 6))

    plt.subplot(1, 2, 1)
    scatter = plt.scatter(pca_features[:, 0], pca_features[:, 1], c=data['label'], cmap='magma', marker='o', edgecolor='k', s=100)
    plt.title('PCA Data with True Labels')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')

    # Create a legend for the scatter plot
    legend1 = plt.legend(*scatter.legend_elements(), title="Classes")
    plt.gca().add_artist(legend1)


    plt.subplot(1, 2, 2)
    scatter = plt.scatter(pca_features[:, 0], pca_features[:, 1], c=data['Cluster_PCA'], cmap='magma', marker='o', edgecolor='k', s=100)
    plt.title('PCA Data with GMM Clusters')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')

    legend2 = plt.legend(*scatter.legend_elements(), title="Clusters")
    plt.gca().add_artist(legend2)

    plt.savefig(path)

    plt.show()



def add_noise(data, error_percentage=0.05):
    noise = data * error_percentage * np.random.randn(*data.shape)
    return data + noise