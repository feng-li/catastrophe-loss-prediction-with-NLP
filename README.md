# catastrophe-loss-prediction-with-NLP
Catastrophe loss prediction with NLP

# Introduction
In this paper, we predict the duration and loss of catastrophes using textual information from online news articles. This new approach is informative in providing timely warnings of the severity of a catastrophe, which can aid decision-making and support appropriate responses.

`get_text.py`: Build a web crawler to extract its news contents.

`get_url.py`: Obtain news title, news source, published time.

`rf_clf.py` & `xgb_clf.py` & `lgb_clf.py`: Predict the losses of each catastrophe-affected country by machine learning models such as Random Forest, XGBoost, and LightGBM.

`rf_reg.py` & `xgb_reg.py` & `lgb_reg.py`: Predict the duration days of each catastrophe-affected country by machine learning models such as Random Forest, XGBoost, and LightGBM.

