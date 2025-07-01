import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from preprocess import clean_code
from feature_extraction import get_embedding

def load_data(folder, label):
    samples = []
    for file in os.listdir(folder):
        with open(os.path.join(folder, file)) as f:
            code = clean_code(f.read())
            emb = get_embedding(code)
            samples.append((emb, label))
    return samples

human_data = load_data("data/human", 0)
chatgpt_data = load_data("data/chatgpt", 1)

X, y = zip(*(human_data + chatgpt_data))
X = np.array(X)
y = np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = RandomForestClassifier()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred, target_names=["Human", "ChatGPT"]))

import joblib
joblib.dump(clf, "model.pkl")
