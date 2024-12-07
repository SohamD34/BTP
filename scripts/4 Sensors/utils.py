import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from sklearn.model_selection import train_test_split
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.metrics import accuracy_score


def add_noise(data, labels, noise_level, target_size=350):
    combined_data = data.copy()
    combined_labels = labels.copy()

    while len(combined_data) < target_size:
        noisy_data = data.copy()
        new_data_points = []

        new_data_df = pd.DataFrame()

        for sensor in data.columns:
            noise = np.random.uniform(-noise_level, noise_level, size=noisy_data.shape[0])
            new_data = noisy_data[sensor] + (noisy_data[sensor] * noise)
            new_data_points.append(new_data)
            new_data_df[sensor] = new_data

        new_labels = labels.copy()

        combined_data = pd.concat([combined_data, new_data_df], ignore_index=True)
        combined_labels = pd.concat([combined_labels, new_labels], ignore_index=True)

    combined_data = combined_data.iloc[:target_size]
    combined_labels = combined_labels.iloc[:target_size]

    return combined_data, combined_labels



def plot_pca_decision_boundary(pca, pca_data, model, label_mapping):

    fig, ax = plt.subplots(1, 2, figsize=(15, 4))
    x_min, x_max = pca_data['PC1'].min() - 50, pca_data['PC1'].max() + 50
    y_min, y_max = pca_data['PC2'].min() - 50, pca_data['PC2'].max() + 50
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))

    X = pca_data[['PC1','PC2']]
    Y = pca_data['Labels'].map({v: k for k, v in label_mapping.items()})

    Z = model.predict(np.c_[xx.ravel().astype(float), yy.ravel().astype(float)])
    Z = Z.reshape(xx.shape)

    predictions = model.predict(X)

    # PLOTTING THE DECISION BOUNDARY 

    ax[0].contourf(xx, yy, Z, alpha=0.2, cmap='viridis')
    scatter = ax[0].scatter(pca_data['PC1'], pca_data['PC2'], c=Y, cmap='viridis')
    # legend0 = ax[0].legend(*scatter.legend_elements(), title="Classes")

    handles, labels = scatter.legend_elements()
    labels = [label_mapping[int(re.search(r'\d+', label).group())] for label in labels]
    ax[0].legend(handles, labels, title="Classes")
    ax[0].set_title('True Class Labels')

    ax[1].contourf(xx, yy, Z, alpha=0.2, cmap='viridis')
    scatter = ax[1].scatter(pca_data['PC1'], pca_data['PC2'], c=predictions, cmap='viridis')
    legend1 = ax[1].legend(*scatter.legend_elements(), title="Classes")

    handles, labels = scatter.legend_elements()
    labels = [label_mapping[int(re.search(r'\d+', label).group())] for label in labels]
    ax[1].legend(handles, labels, title="Classes")
    ax[1].set_title('Predicted Class Labels and Decision Boundary')
    
    ax[1].set_xlabel(f'PCA Component 1 ({pca.explained_variance_ratio_[0] * 100:.2f}% variance)')
    ax[1].set_ylabel(f'PCA Component 2 ({pca.explained_variance_ratio_[1] * 100:.2f}% variance)')
    
    plt.show()



def plot_lda_decision_boundary(lda, lda_data, model, label_mapping):

    fig, ax = plt.subplots(1, 2, figsize=(15, 4))
    x_min, x_max = lda_data['LD1'].min() - 5, lda_data['LD1'].max() + 5
    y_min, y_max = lda_data['LD2'].min() - 5, lda_data['LD2'].max() + 5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))

    X = lda_data[['LD1','LD2']]
    Y = lda_data['Labels'].map({v: k for k, v in label_mapping.items()})

    Z = model.predict(np.c_[xx.ravel().astype(float), yy.ravel().astype(float)])
    Z = Z.reshape(xx.shape)

    predictions = model.predict(X)

    # PLOTTING THE DECISION BOUNDARY 

    ax[0].contourf(xx, yy, Z, alpha=0.2, cmap='viridis')
    scatter = ax[0].scatter(lda_data['LD1'], lda_data['LD2'], c=Y, cmap='viridis')
    # legend0 = ax[0].legend(*scatter.legend_elements(), title="Classes")

    handles, labels = scatter.legend_elements()
    labels = [label_mapping[int(re.search(r'\d+', label).group())] for label in labels]
    ax[0].legend(handles, labels, title="Classes")
    ax[0].set_title('True Class Labels')

    ax[1].contourf(xx, yy, Z, alpha=0.2, cmap='viridis')
    scatter = ax[1].scatter(lda_data['LD1'], lda_data['LD2'], c=predictions, cmap='viridis')
    legend1 = ax[1].legend(*scatter.legend_elements(), title="Classes")

    handles, labels = scatter.legend_elements()
    labels = [label_mapping[int(re.search(r'\d+', label).group())] for label in labels]
    ax[1].legend(handles, labels, title="Classes")
    ax[1].set_title('Predicted Class Labels and Decision Boundary')

    ax[1].set_xlabel(f'LD1 ({lda.explained_variance_ratio_[0] * 100:.2f}% variance)')
    ax[1].set_ylabel(f'LD2 ({lda.explained_variance_ratio_[1] * 100:.2f}% variance)')


    plt.show()



def error_decision_boundaries(model, model_name, X, Y, label_mapping):

    for p in [0.05, 0.10, 0.15, 0.2, 0.25]:

        # Adding noise to the data

        print(f'Noise Level: {p}')
        data_noisy, noisy_labels = add_noise(X, Y.map(label_mapping), p)


        lda = LDA(n_components=2)
        lda_data = lda.fit_transform(data_noisy, noisy_labels)
        lda_data = pd.DataFrame(lda_data, columns=['LD1','LD2'])
        lda_data['Label'] = noisy_labels


        # Split into training and testing data

        Y = lda_data['Label'].map({'A1': 1, 'A2': 2, 'A3': 3})
        X_lda = lda_data.drop(['Label'], axis=1)

        X_train, X_test, Y_train, Y_test = train_test_split(X_lda, Y, test_size=0.2, random_state=np.random.randint(0,100))

        model.fit(X_train, Y_train)
        print('Training accuracy = ', model.score(X_train, Y_train))

        pred = model.predict(X_test)
        print('Testing accuracy = ', accuracy_score(Y_test, pred))

        # Plotting

        predictions = model.predict(X_lda)

        x_min, x_max = lda_data['LD1'].min() - 5, lda_data['LD1'].max() + 5
        y_min, y_max = lda_data['LD2'].min() - 5, lda_data['LD2'].max() + 5
        xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))

        Z = model.predict(np.c_[xx.ravel().astype(float), yy.ravel().astype(float)])
        Z = Z.reshape(xx.shape)

        # PLOTTING THE DECISION BOUNDARY 

        fig, ax = plt.subplots(1, 2, figsize=(15, 4))

        ax[0].contourf(xx, yy, Z, alpha=0.2, cmap='viridis')
        scatter = ax[0].scatter(lda_data['LD1'], lda_data['LD2'], c=Y, cmap='viridis')
        legend0 = ax[0].legend(*scatter.legend_elements(), title="Classes")

        handles, labels = scatter.legend_elements()
        labels = [label_mapping[int(re.search(r'\d+', label).group())] for label in labels]
        ax[0].legend(handles, labels, title="Classes")
        ax[0].set_title('True Class Labels')

        ax[1].contourf(xx, yy, Z, alpha=0.2, cmap='viridis')
        scatter = ax[1].scatter(lda_data['LD1'], lda_data['LD2'], c=predictions, cmap='viridis')
        legend1 = ax[1].legend(*scatter.legend_elements(), title="Classes")

        handles, labels = scatter.legend_elements()
        labels = [label_mapping[int(re.search(r'\d+', label).group())] for label in labels]
        ax[1].legend(handles, labels, title="Classes")
        ax[1].set_title(f'{model_name} Predicted Class Labels and Decision Boundary')

        plt.show()