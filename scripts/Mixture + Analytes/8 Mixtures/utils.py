import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import re

def plot_pca_classes(pca, pca_data, labels, title, colors, label_mapping):

    scatter = plt.scatter(pca_data['PC1'], pca_data['PC2'], c=labels, cmap=ListedColormap(colors))
    handles, labels = scatter.legend_elements()
    labels = [label_mapping[int(re.search(r'\d+', str(label)).group())] for label in labels]

    plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.2f}%)')
    plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.2f}%)')
    plt.title(title)
    plt.legend(handles, labels, title="Classes")

    plt.show()



def plot_lda_classes(lda, lda_data, labels, title, colors, label_mapping):

    scatter = plt.scatter(lda_data['LD1'], lda_data['LD2'], c=labels, cmap=ListedColormap(colors))

    handles, labels = scatter.legend_elements()
    labels = [label_mapping[int(re.search(r'\d+', str(label)).group())] for label in labels]
    plt.legend(handles, labels, title="Classes", fontsize='small', title_fontsize='small')

    explained_variance = lda.explained_variance_ratio_
    plt.xlabel(f'LD1 ({explained_variance[0]*100:.2f}%)')
    plt.ylabel(f'LD2 ({explained_variance[1]*100:.2f}%)')
    plt.title(title)

    plt.show()