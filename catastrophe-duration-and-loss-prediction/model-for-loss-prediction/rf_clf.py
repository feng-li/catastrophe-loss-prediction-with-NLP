def rf_clf(trial):
    params = {'random_state': 0, 
              'max_depth': trial.suggest_int('max_depth', 3, 10), 
              'max_features': trial.suggest_int('max_features', 1, 30), 
              'ccp_alpha': trial.suggest_float('ccp_alpha', 0, 0.1), }
    model = RandomForestClassifier(**params)
    model.fit(x_train, y_label_train)
    y_pred = model.predict(x_test)
    return sum(y_pred == y_label_test) / len(y_label_test)
