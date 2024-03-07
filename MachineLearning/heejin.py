from sklearn.metrics import mean_absolute_error,r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
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

def print_hist(nrows, ncols, featureDF):

    n = 1
    for col in featureDF.columns:
        plt.subplot(nrows, ncols, n)
        plt.hist(featureDF[col],edgecolor='k', color = 'yellow')
        plt.title(f'{col}')
        plt.ylabel(col)
        n += 1
    plt.tight_layout()
    plt.show()

def print_box(nrows, ncols,targetSR, featureDF):
    n = 1
    for i in featureDF.columns:
        plt.subplot(nrows, ncols, n)
        plt.boxplot(featureDF[i])
        plt.xlabel(targetSR.name)
        plt.title(f'{i}')
        n += 1
    plt.tight_layout()
    plt.show()

def find_outlier_z(df, hold = 1):
    for i in df.columns:
        mean = df[i].mean()
        std = df[i].std()
        z_score = (df[i] - mean) / std
        mask = z_score.abs() > hold
        print(f'z - {i}의 이상치 개수 : {z_score[mask].count()}')

def fill_outliers_z(sr, hold, fill_value):

    valid_value = ['mean', 'median']
    if fill_value not in valid_value:
        raise ValueError(f"score_standard must be one of {valid_value}")

    mean = sr.mean()
    std = sr.std()
    z_score = (sr - mean) / std
    mask = z_score.abs() <= hold

    sr_copy = sr.copy()

    if fill_value == 'mean':
        sr_copy[mask] = sr_copy.mean()
    elif fill_value == 'median':
        sr_copy[mask] = sr_copy.median()

    return sr_copy

def find_outlier_iqr(df,threshold = 1.5):
    for i in df.columns:
        q1 = df[i].quantile(0.25)
        q3 = df[i].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - iqr * threshold
        upper = q3 + iqr * threshold

        print(f'iqr - {i}의 이상치 개수 : {df[(df[i] < lower)&(df[i] > upper)].count()}')

def fill_outliers_iqr(sr, threshold, fill_value):

    valid_value = ['mean', 'median']
    if fill_value not in valid_value:
        raise ValueError(f"score_standard must be one of {valid_value}")

    q1 = sr.quantile(0.25)
    q3 = sr.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - iqr
    upper = q3 + iqr

    sr_copy = sr.copy()

    if fill_value == 'mean':
        sr_copy[(sr_copy < lower) & (sr_copy > upper)] = sr_copy.mean()
    elif fill_value == 'median':
        sr_copy[(sr_copy < lower) & (sr_copy > upper)] = sr_copy.median()

    return sr_copy


def find_random_state(featureDF,targetSR):
    # 최적 random_state 값
    random_state_list = []
    for i in range(1,51):
        xtrain,xtest,ytrain,ytest = train_test_split(featureDF,targetSR,test_size=0.2,random_state=i)
        scaler = StandardScaler() # scaler 종류에 따른 큰 차이 없음
        scaler.fit(xtrain)
        xtrain_scaled = scaler.transform(xtrain)
        xtest_scaled = scaler.transform(xtest)
        model = LinearRegression() # model 종류에 따라 차이남
        model.fit(xtrain_scaled,ytrain)
        model.score(xtest_scaled,ytest)
        random_state_list.append(model.score(xtest_scaled,ytest))
    max_score = max(random_state_list)
    print(f'radom_state = {random_state_list.index(max_score)+1}\nscore : {max_score}')

    max_random_state = random_state_list.index(max_score)+1
    return max_random_state

def find_maxK_re(xtrain,ytrain,xtest,ytest):
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
    return K

def find_maxK_cl(xtrain,ytrain,xtest,ytest):
    max_k = xtrain.shape[0]
    test_scoreList = []
    train_scoreList = []

    for k in range(1, max_k + 1):
        knn_model = KNeighborsClassifier(n_neighbors=k)
        knn_model.fit(xtrain, ytrain)
        train_scoreList.append(knn_model.score(xtrain, ytrain))
        test_scoreList.append(knn_model.score(xtest, ytest))
    max_idx = test_scoreList.index(max(test_scoreList)) + 1
    K = max_idx
    return K

def find_re_model(xtrain, ytrain, xtest, ytest, score_standard ):

    valid_scores = ['r2', 'mae', 'mse', 'rmse']
    if score_standard not in valid_scores:
        raise ValueError(f"score_standard must be one of {valid_scores}")

    models = [KNeighborsRegressor(),LinearRegression(),Ridge(),Lasso()]
    scalers = [StandardScaler(), MinMaxScaler(), RobustScaler()]

    acDict = {}
    model_score = {'model': [], 'scaler': [], 'train_score': [], 'test_score': [], 'r2': [], 'mae': [], 'mse': [],
                   'rmse': []}

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
            elif isinstance(model, Ridge):
                alphas = np.arange(0.1, 30., 0.1).tolist()
                scorelist = [[], []]
                for a in alphas:
                    model = Ridge(alpha=a, max_iter=30000)

                    model.fit(xtrain, ytrain)

                    scorelist[0].append(model.score(xtrain, ytrain))
                    scorelist[1].append(model.score(xtest, ytest))
                best_alpha = alphas[scorelist[1].index(max(scorelist[1]))]
                model = Ridge(alpha=best_alpha, max_iter=30000)
            elif isinstance(model, Lasso):
                alphas = np.arange(0.1, 30., 0.1).tolist()
                scorelist = [[], []]
                for a in alphas:
                    model = Lasso(alpha=a, max_iter=30000)

                    model.fit(xtrain, ytrain)

                    scorelist[0].append(model.score(xtrain, ytrain))
                    scorelist[1].append(model.score(xtest, ytest))
                best_alpha = alphas[scorelist[1].index(max(scorelist[1]))]
                model = Lasso(alpha=best_alpha, max_iter=30000)

            # KNN,Ridge,Laaso 모델이 아닐 때, 바로 아래 코드 수행
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

            model_score['model'].append(model)
            model_score['scaler'].append(scaler)
            model_score['train_score'].append(train_score)
            model_score['test_score'].append(test_score)
            model_score['r2'].append(r2)
            model_score['mae'].append(mae)
            model_score['mse'].append(mse)
            model_score['rmse'].append(rmse)

    if score_standard == 'r2':
        max_ac = max(acDict, key=lambda k: acDict[k][2])
    elif score_standard == 'mae':
        max_ac = min(acDict, key=lambda k: acDict[k][3])
    elif score_standard == 'mse':
        max_ac = min(acDict, key=lambda k: acDict[k][4])
    elif score_standard == 'rmse':
        max_ac = min(acDict, key=lambda k: acDict[k][5])
    else:
        pass

    print(
        f'[최적의 모델] :{max_ac}\nTrain score : {acDict[max_ac][0]}\nTest score : {acDict[max_ac][1]} \nR2 : {acDict[max_ac][2]}'
        f'\nMAE : {acDict[max_ac][3]}\nMSE : {acDict[max_ac][4]}\nRMSE : {acDict[max_ac][5]}')
    return model_score

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


def find_poly_p(xtrain, ytrain, xtest, ytest):
    # poly 최적의 파라미터 값 찾기
    max_score = []
    for b in [True, False]:
        for d in range(1, 6):
            poly = PolynomialFeatures(interaction_only=b, degree=d)
            poly.fit(xtrain)
            xtrain_transformed = poly.transform(xtrain)
            xtest_transformed = poly.transform(xtest)

            model = LinearRegression()
            model.fit(xtrain_transformed, ytrain)
            score = model.score(xtest_transformed, ytest)
            print(b, d, score)
            max_score.append([b, d, score])

    max_element = max(max_score, key=lambda x: x[2])

    b_max, d_max, score_max = max_element[0], max_element[1], max_element[2]

    print(f'max score =>\ninteraction_only = {b_max}, degree = {d_max}, score = {score_max}')
    return b_max, d_max

def find_alpha(xtrain, ytrain, xtest, ytest):
    alphas = np.arange(0.1,30.,0.1).tolist()
    scorelist = [[], []]
    for a in alphas:
        model = Ridge(alpha=a, max_iter=30000)

        model.fit(xtrain, ytrain)

        scorelist[0].append(model.score(xtrain, ytrain))
        scorelist[1].append(model.score(xtest, ytest))
    best_alpha = alphas[scorelist[1].index(max(scorelist[1]))]
    return best_alpha

def print_alpha_plot(alphas,best_alpha,scorelist):
    plt.plot(alphas, scorelist[0], label='Train')
    plt.plot(alphas, scorelist[1], label='Test')
    plt.axvline(best_alpha, color='red', linestyle=':', label=f'alpha ={best_alpha}')
    plt.text(best_alpha + 1, 0.984, f'Best_alpha ={best_alpha}')
    plt.legend()
    plt.title('[Train & Test]')