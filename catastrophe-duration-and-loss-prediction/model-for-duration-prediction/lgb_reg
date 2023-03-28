def lgb_reg(trial):
    params = {'objective': 'regression', 'random_state': 0, 
              'max_depth': trial.suggest_int('max_depth', 3, 10), 
              'learning_rate': trial.suggest_float('learning_rate', 0.001, 1), 
              'reg_alpha': trial.suggest_float('reg_alpha', 0, 1.0), 
              'reg_lambda': trial.suggest_float('reg_lambda', 0, 1.0), }
    model = lgb.LGBMRegressor(**params)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    return np.sqrt(sum((y_test - y_pred)**2) / len(y_test))
