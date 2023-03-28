def lgb_clf(trial):
    params = {'objective': 'binary', 'random_state': 0, 
              'max_depth': trial.suggest_int('max_depth', 3, 10), 
              'learning_rate': trial.suggest_float('learning_rate', 0.001, 1), 
              'reg_alpha': trial.suggest_float('reg_alpha', 0, 1.0), 
              'reg_lambda': trial.suggest_float('reg_lambda', 0, 1.0), }
    model = lgb.LGBMClassifier(**params)
    model.fit(x_train, y_label_train)
    y_pred = model.predict(x_test)
    return sum(y_pred == y_label_test) / len(y_label_test)
