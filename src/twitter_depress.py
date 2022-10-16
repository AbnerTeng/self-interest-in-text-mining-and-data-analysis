# %%
import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support

# %%
path = os.getcwd()
fwd = os.path.abspath(os.path.join(path, ".."))
data_path = fwd + "/datas/sentiment_tweets3.csv"
raw_data = pd.read_csv(data_path)
##print(raw_data.head())
raw_data.columns = ['index', 'tweet', 'label']

# %%
raw_text = []
for i in range(len(raw_data["tweet"])):
    text = raw_data['tweet'][i]
    raw_text.append(text)

vectorizer = TfidfVectorizer()
vectorized_text = vectorizer.fit_transform(raw_text)

print(vectorizer.idf_[0:5])
# %%
feature_array = vectorizer.get_feature_names_out()
feature_data = vectorizer.transform(raw_text)
feature_data_array = feature_data.toarray()
feature_df = pd.DataFrame(feature_data_array, columns=[feature_array])
label_df = raw_data[['label']]
# %%
data_train, data_test, label_train, label_test = train_test_split(feature_df, label_df, test_size=0.2, random_state=88)
model = LogisticRegression().fit(data_train, label_train)
label_predict = model.predict(data_test)
print(label_predict[:10])  ##  0 = non-depressed, 1 = depressed
label_predict_proba = model.predict_proba(data_test)
print(label_predict_proba[:10])  ## column[0]: non-depressed, column[1]: depressed
# %%
print(confusion_matrix(label_test, label_predict))
evaluation = precision_recall_fscore_support(label_test, label_predict, average='macro')
accuarcy = model.score(data_test, label_test)
print(f"accuracy: {accuarcy}", f"\n precision: {evaluation[0]}", f"\n recall: {evaluation[1]}", f"\n f1-score: {evaluation[2]}")
# %%
