
# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import os

# Load data
fake_df = pd.read_csv("data/Fake.csv")
true_df = pd.read_csv("data/True.csv")

fake_df["label"] = 0  # Fake = 0
true_df["label"] = 1  # Real = 1

df = pd.concat([fake_df, true_df])
df = df[["title", "text", "label"]].dropna()

# Combine title and text
df["content"] = df["title"] + " " + df["text"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    df["content"], df["label"], test_size=0.2, random_state=42)

# Vectorize text
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Accuracy
pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, pred))

# Save model and vectorizer
os.makedirs("model", exist_ok=True)
with open("model/fake_news_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)
