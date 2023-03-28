# catastrophe-loss-prediction-with-NLP
Catastrophe loss prediction with NLP

# Introduction
In this paper, we predict the duration and loss of catastrophes using textual information from online news articles. This new approach is informative in providing timely warnings of the severity of a catastrophe, which can aid decision-making and support appropriate responses.

`\color{Blue}{get_text.py}`: Build a web crawler to extract its news contents.

`\color{Blue}{get_url.py}`: Obtain news title, news source, published time.

`\color{Blue}{vector-embedded-by-BERT.py}` & `\color{Blue}{vector-embedded-by-Word2Vec.py}`:Construct the document vector.

`\color{Blue}{keywords.txt}`: Select 300 words as our keyword database.

`\color{Blue}{rf_clf.py}` & `\color{Blue}{xgb_clf.py}` & `\color{Blue}{lgb_clf.py}`: Predict the losses of each catastrophe-affected country by machine learning models such as Random Forest, XGBoost, and LightGBM.

`\color{Blue}{rf_reg.py}` & `\color{Blue}{xgb_reg.py}` & `\color{Blue}{lgb_reg.py}`: Predict the duration days of each catastrophe-affected country by machine learning models such as Random Forest, XGBoost, and LightGBM.



