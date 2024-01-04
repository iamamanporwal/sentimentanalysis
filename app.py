from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('twittermodel.joblib')

from sklearn.feature_extraction.text import TfidfVectorizer

# Sample function to preprocess and vectorize the tweet
def preprocess_and_vectorize(tweet):
    # Perform any necessary preprocessing on the input data
    cleaned_tweet = preprocess(tweet)
    
    # Use TF-IDF vectorizer to convert text data to numerical features
    vectorizer = TfidfVectorizer()
    cleaned_tweet_vectorized = vectorizer.fit_transform([cleaned_tweet])
    
    return cleaned_tweet_vectorized

# Sample function to predict sentiment
def predict_sentiment(tweet):
    # Convert text data to numerical features
    cleaned_tweet_vectorized = preprocess_and_vectorize(tweet)
    
    # Make predictions using the loaded model
    prediction = model.predict(cleaned_tweet_vectorized)
    
    return prediction[0]

# Sample function for tweet preprocessing
def preprocess(tweet):
    # Implement your tweet cleaning and processing logic here
    # Example: Remove special characters, convert to lowercase, etc.
    return tweet

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for handling predictions
@app.route('/predict', methods=['POST'])
def predict():
    tweet = request.form['tweet']
    sentiment = predict_sentiment(tweet)
    return render_template('result.html', sentiment=sentiment, tweet=tweet)

if __name__ == '__main__':
    app.run(debug=True)

