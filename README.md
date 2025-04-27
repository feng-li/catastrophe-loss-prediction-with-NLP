# Catastrophe loss prediction with NLP

This repository provides the code implementation for our paper

Han Wang, Wen Wang, Feng Li, Yanfei Kang and Han Li (2025). [“Catastrophe Duration and Loss Prediction via Natural Language Processing”](https://variancejournal.org/article/133589-catastrophe-duration-and-loss-prediction-via-natural-language-processing). Variance, Vol. 18

## Disclaimer

This code is provided **AS IS**, with no further updates or maintenance. If you have any questions, please contact [Feng Li](https://feng.li/) via email `feng.li@gsm.pku.edu.cn`.


# Introduction
In this project, we predict the duration and loss of catastrophes using textual information from online news articles. This new approach is informative in providing timely warnings of the severity of a catastrophe, which can aid decision-making and support appropriate responses.

- `get_text.py`: Build a web crawler to extract its news contents.

- `get_url.py`: Obtain news title, news source, published time.

- `vector-embedded-by-BERT.py` & `vector-embedded-by-Word2Vec.py`: Construct the document vector.

- `keywords.txt`: Select 300 words as our keyword database.

- `rf_clf.py` & `xgb_clf.py` & `lgb_clf.py`: Predict the losses of each catastrophe-affected country by machine learning models such as Random Forest, XGBoost, and LightGBM.

- `rf_reg.py` & `xgb_reg.py` & `lgb_reg.py`: Predict the duration days of each catastrophe-affected country by machine learning models such as Random Forest, XGBoost, and LightGBM.




