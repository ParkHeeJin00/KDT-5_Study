from sklearn.metrics import mean_absolute_error,r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
import matplotlib.pyplot as plt
import numpy as np

def print_scatter(nrows, ncols, targetSR, featureDF):

    n = 1
    for col in featureDF.columns:
        plt.subplot(nrows, ncols, n)
        plt.scatter(targetSR, featureDF[col], label=f'corr = {targetSR.corr(featureDF[col]):.4f}')
        plt.xlabel(targetSR.name)
        plt.title(f'{col}')
        plt.ylabel(col)
        plt.xticks([])
        plt.legend()
        n += 1
    plt.tight_layout()
    plt.show()


def find_re_model(xtrain, ytrain, xtest, ytest):

    models = [KNeighborsRegressor(),LinearRegression()]
    scalers = [StandardScaler(), MinMaxScaler(), RobustScaler()]

    acDict = {}
    for scaler in scalers:
        scaler.fit(xtrain)
        scaled_xtrain = scaler.transform(xtrain)
        scaled_xtest = scaler.transform(xtest)

        for model in models:
            if isinstance(model, KNeighborsRegressor):
                print('----------------탐색중------------------')
                max_k = xtrain.shape[0]
                test_scoreList = []
                train_scoreList = []

                for k in range(1, max_k + 1):
                    knn_model = KNeighborsRegressor(n_neighbors=k)
                    knn_model.fit(xtrain, ytrain)
                    train_scoreList.append(knn_model.score(xtrain, ytrain))
                    test_scoreList.append(knn_model.score(xtest, ytest))
                max_idx = test_scoreList.index(max(test_scoreList)) + 1
                K = max_idx
                model = KNeighborsRegressor(n_neighbors = K)

            # KNN 모델이 아닐 때, 바로 아래 코드 수행
            model.fit(scaled_xtrain, ytrain)
            print(f'model : {model}')

            train_score = model.score(scaled_xtrain, ytrain)
            test_score = model.score(scaled_xtest, ytest)
            print(f'scaler : {scaler}\nTrain score : {train_score}\nTest score : {test_score}')

            y_pre = model.predict(scaled_xtest)
            r2 = r2_score(ytest, y_pre)
            mse = mean_squared_error(ytest, y_pre)
            mae = mean_absolute_error(ytest, y_pre)
            rmse = mean_squared_error(ytest, y_pre, squared=False)
            print(f'''
    [모델 설명도]\nR2 : {r2}\n[에러]\nMAE : {mae}\nMSE : {mse}\nRMSE : {rmse}\n--------------------------------------
    ''')

            acDict[(model, scaler)] = [train_score,test_score, r2, mae, mse, rmse]

    max_ac = max(acDict, key=lambda k: acDict[k][2])
    print(
        f'[최적의 모델] :{max_ac}\nTrain score : {acDict[max_ac][0]}\nTest score : {acDict[max_ac][1]} \nR2 : {acDict[max_ac][2]}'
        f'\nMAE : {acDict[max_ac][3]}\nMSE : {acDict[max_ac][4]}\nRMSE : {acDict[max_ac][5]}')
    return max_ac[0],max_ac[1],acDict[max_ac][2] # model,scaler,score

def find_scaler(xtrain, ytrain, xtest, ytest, model):
    scalers = [StandardScaler(), MinMaxScaler(), RobustScaler()]

    train_scores = []
    test_scores = []
    for scaler in scalers:
        scaler.fit(xtrain)
        scaled_xtrain = scaler.transform(xtrain)
        scaled_xtest = scaler.transform(xtest)

        model.fit(scaled_xtrain, ytrain)
        print(f'model : {model}')

        train_score = model.score(scaled_xtrain, ytrain)
        test_score = model.score(scaled_xtest, ytest)
        train_scores.append(train_score)
        test_scores.append(test_score)
        print(f'scaler : {scaler}\nTrain score : {train_score}\nTest score : {test_score}')

        y_pre = model.predict(scaled_xtest)
        r2 = r2_score(ytest, y_pre)
        mse = mean_squared_error(ytest, y_pre)
        mae = mean_absolute_error(ytest, y_pre)
        rmse = mean_squared_error(ytest, y_pre, squared=False)
        print(f'''
[모델 설명도]\nR2 : {r2}\n[에러]\nMAE : {mae}\nMSE : {mse}\nRMSE : {rmse}\n\n--------------------------------------
''')