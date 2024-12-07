import pandas as pd
import numpy as np
import pickle
import sklearn
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import warnings
warnings.filterwarnings('ignore')

def test_3_analytes():

    print('\nTesting 3 analytes dataset...')

    data = pd.read_excel('/home/soham/Desktop/GitHub/BTP/data/validation_data/analyte3_validation_data.xlsx')
    X = data.iloc[:, :-2].values
    Y = data.iloc[:, -1].values

    pca = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/3 solutions/pca.pkl', 'rb'))
    lda = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/3 solutions/lda.pkl', 'rb'))

    X_pca = pca.transform(X)
    X_lda = lda.transform(X)

    print('Accuracy: ')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/3 solutions/lda_rfc.pkl', 'rb'))
    Y_pred = model.predict(X_lda)
    accuracy = np.mean(Y == Y_pred)
    print(f'LDA_RFC: {accuracy}')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/3 solutions/lda_svm.pkl', 'rb'))
    Y_pred = model.predict(X_lda)
    accuracy = np.mean(Y == Y_pred)
    print(f'LDA_SVM: {accuracy}')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/3 solutions/pca_rfc.pkl', 'rb'))
    Y_pred = model.predict(X_pca)
    accuracy = np.mean(Y == Y_pred)
    print(f'PCA_RFC: {accuracy}')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/3 solutions/pca_svm.pkl', 'rb'))
    Y_pred = model.predict(X_pca)
    accuracy = np.mean(Y == Y_pred)
    print(f'PCA_SVM: {accuracy}')




def test_4_solutions():

    print('\nTesting 4 solutions dataset...')

    data = pd.read_excel('/home/soham/Desktop/GitHub/BTP/data/validation_data/analyte3_validation_data.xlsx')
    X = data.iloc[:, :-2].values
    Y = data.iloc[:, -1].values

    pca = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/4 solutions/pca.pkl', 'rb'))
    lda = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/4 solutions/lda.pkl', 'rb'))

    X_pca = pca.transform(X)
    X_lda = lda.transform(X)

    print('Accuracy: ')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/4 solutions/lda_rfc.pkl', 'rb'))
    Y_pred = model.predict(X_lda)
    accuracy = np.mean(Y == Y_pred)
    print(f'LDA_RFC: {accuracy}')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/4 solutions/lda_svm.pkl', 'rb'))
    Y_pred = model.predict(X_lda)
    accuracy = np.mean(Y == Y_pred)
    print(f'LDA_SVM: {accuracy}')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/4 solutions/pca_rfc.pkl', 'rb'))
    Y_pred = model.predict(X_pca)
    accuracy = np.mean(Y == Y_pred)
    print(f'PCA_RFC: {accuracy}')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/4 solutions/pca_svm.pkl', 'rb'))
    Y_pred = model.predict(X_pca)
    accuracy = np.mean(Y == Y_pred)
    print(f'PCA_SVM: {accuracy}')




def test_5_solutions():

    print('\nTesting 5 solutions dataset...')

    data = pd.read_excel('/home/soham/Desktop/GitHub/BTP/data/validation_data/analyte3_validation_data.xlsx')
    X = data.iloc[:, :-2].values
    Y = data.iloc[:, -1].values

    pca = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/5 solutions/pca.pkl', 'rb'))
    lda = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/5 solutions/lda.pkl', 'rb'))

    X_pca = pca.transform(X)
    X_lda = lda.transform(X)

    print('Accuracy: ')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/5 solutions/lda_rfc.pkl', 'rb'))
    Y_pred = model.predict(X_lda)
    accuracy = np.mean(Y == Y_pred)
    print(f'LDA_RFC: {accuracy}')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/5 solutions/lda_svm.pkl', 'rb'))
    Y_pred = model.predict(X_lda)
    accuracy = np.mean(Y == Y_pred)
    print(f'LDA_SVM: {accuracy}')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/5 solutions/pca_rfc.pkl', 'rb'))
    Y_pred = model.predict(X_pca)
    accuracy = np.mean(Y == Y_pred)
    print(f'PCA_RFC: {accuracy}')

    model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/5 solutions/pca_svm.pkl', 'rb'))
    Y_pred = model.predict(X_pca)
    accuracy = np.mean(Y == Y_pred)
    print(f'PCA_SVM: {accuracy}')



# def test_8_solutions():

#     print('Testing 8 solutions dataset...')

#     data = pd.read_excel('/home/soham/Desktop/GitHub/BTP/data/validation_data/analyte3_validation_data.xlsx')
#     X = data.iloc[:, :-2].values
#     Y = data.iloc[:, -1].values

#     pca = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/8 solutions/pca.pkl', 'rb'))
#     lda = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/8 solutions/lda.pkl', 'rb'))

#     X_pca = pca.transform(X)
#     X_lda = lda.transform(X)

#     print('Accuracy: ')

#     model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/8 solutions/lda_rfc.pkl', 'rb'))
#     Y_pred = model.predict(X_lda)
#     accuracy = np.mean(Y == Y_pred)
#     print(f'LDA_RFC: {accuracy}')

#     model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/8 solutions/lda_svm.pkl', 'rb'))
#     Y_pred = model.predict(X_lda)
#     accuracy = np.mean(Y == Y_pred)
#     print(f'LDA_SVM: {accuracy}')

#     model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/8 solutions/pca_rfc.pkl', 'rb'))
#     Y_pred = model.predict(X_pca)
#     accuracy = np.mean(Y == Y_pred)
#     print(f'PCA_RFC: {accuracy}')

#     model = pickle.load(open('/home/soham/Desktop/GitHub/BTP/models/8 solutions/pca_svm.pkl', 'rb'))
#     Y_pred = model.predict(X_pca)
#     accuracy = np.mean(Y == Y_pred)
#     print(f'PCA_SVM: {accuracy}')
    


if __name__ == '__main__':
    test_3_analytes()
    test_4_solutions()
    test_5_solutions()
    # test_8_solutions()