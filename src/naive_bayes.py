import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
import os

data_path = "/datas/SMSCollection.csv"
path = os.getcwd()
fwd = os.path.abspath(os.path.join(path, ".."))
file_path = fwd + data_path

raw_data = pd.read_csv(file_path)
raw_data.head()

## 向量化後做出 BOW
vectorizer = CountVectorizer()

raw_text = []
for i in range(len(raw_data['sms'])):
    text = raw_data['sms'][i]
    raw_text.append(text)

array = vectorizer.fit_transform(raw_text) ## construct BOW

feature_array = vectorizer.get_feature_names_out() ## get feature name
feature_data = array.toarray()
feature_df = pd.DataFrame(feature_data, columns=[feature_array])
label_df = raw_data[["Class"]]

data_train, data_test, label_train, label_test = train_test_split(feature_df, label_df, test_size=0.2, random_state=24)
model = MultinomialNB()
model.fit(data_train, label_train)

label_predict = model.predict(data_test)
print(confusion_matrix(label_test, label_predict))
evaluation = precision_recall_fscore_support(label_test, label_predict, average = 'macro')
accuracy = model.score(data_test, label_test)
print(f"Accuracy: " + str(accuracy) + "\n precision: " + str(evaluation[0])
+ "\n recall: " + str(evaluation[1]) + "\n f1-score: " + str(evaluation[2]))
