import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load data
data = pd.read_csv('C:\\Users\\lenovo 2020\\Reviews.csv')

# Clean text function
def clean_text(text):
    text = re.sub(r'Review collected by and hosted on G2.com', '', text)
    text = text.strip().replace('"', '')
    return text

# Apply text cleaning
data['Cleaned_Content'] = data['Content'].apply(clean_text)

# Assign sentiment based on keywords
def assign_sentiment(text):
    positive_words = ["best", "great", "love", "fantastic", "excellent", "game-changer", "perfect", "good"]
    negative_words = ["difficult", "lack", "problem", "bad", "poor", "issue", "hard", "dislike"]
    text_tokens = re.findall(r'\b\w+\b', text.lower())
    
    pos_count = sum(1 for word in text_tokens if word in positive_words)
    neg_count = sum(1 for word in text_tokens if word in negative_words)
    
    return 1 if pos_count > neg_count else 0

# Apply sentiment assignment
data['Sentiment'] = data['Cleaned_Content'].apply(assign_sentiment)

# Preprocess text without using NLTK stopwords or tokenizers
def preprocess_text(text):
    # Lowercase, remove non-alphabetic characters and stop words
    stop_words = {"the", "and", "is", "in", "to", "a", "of", "for", "on", "that", "it", "with", "as", "this", "by", "at", "from"}
    tokens = re.findall(r'\b\w+\b', text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(tokens)

# Apply text preprocessing
data['Processed_Content'] = data['Cleaned_Content'].apply(preprocess_text)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    data['Processed_Content'], data['Sentiment'], test_size=0.2, random_state=42)

# Vectorize text
tfidf = TfidfVectorizer(max_features=1000)
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Prediction function
def predict_sentiment(new_text):
    cleaned_text = preprocess_text(clean_text(new_text))
    text_tfidf = tfidf.transform([cleaned_text])
    return "Positive" if model.predict(text_tfidf)[0] == 1 else "Negative"

# Save the model and vectorizer
with open('D:\\clg work\\5th sem\\MINOR PROJECT THINGS\\PROJECT\\models\\model2_peer_sentiment_analysis.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
with open('D:\\clg work\\5th sem\\MINOR PROJECT THINGS\\PROJECT\\models\\for peer_sentiment - tfidf_vectorizer.pkl', 'wb') as vectorizer_file:
    pickle.dump(tfidf, vectorizer_file)

