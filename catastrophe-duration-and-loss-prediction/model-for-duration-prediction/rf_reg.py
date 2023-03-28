def rf_reg(trial):
    params = {'random_state': 0, 
              'max_depth': trial.suggest_int('max_depth', 3, 10), 
              'max_features': trial.suggest_int('max_features', 1, 30), 
              'ccp_alpha': trial.suggest_float('ccp_alpha', 0, 0.1), }
    model = RandomForestRegressor(**params)
    model.fit(x_train_1, y_train_1)
    y_pred = model.predict(x_test_1)
    return np.sqrt(sum((y_test_1 - y_pred)**2) / len(y_test_1))
