def find_model(xtrain, ytrain, xtest, ytest):
    models = [LinearRegression()]
    scalers = [StandardScaler(), MinMaxScaler(), RobustScaler()]

    acDict = {}
    for model in models:
        for scaler in scalers:
            scaler.fit(xtrain)
            scaled_xtrain = scaler.transform(xtrain)
            scaled_xtest = scaler.transform(xtest)

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

            acDict[(model, scaler)] = [r2, mae, mse, rmse]

    max_ac = max(acDict, key=lambda k: acDict[k][0])
    print(
        f'[최적의 모델] :{max_ac}\n R2 : {acDict[max_ac][0]}\n MAE : {acDict[max_ac][1]}\n MSE : {acDict[max_ac][2]}\n RMSE : {acDict[max_ac][3]}')
# %%

