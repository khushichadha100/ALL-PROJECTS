from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import pickle
import re
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import GradientBoostingRegressor

app = Flask(__name__)

# Load models and vectorizers


# MongoDB Setup (connecting to local MongoDB instance)
client = MongoClient('mongodb://localhost')
db = client['corporate_solutions_db']  # Database name
peer_sentiment_collection = db['peer_sentiment_analysis']  # Collection name for Peer Sentiment
employee_performance_collection = db['employee_performance']  # Collection name for Employee Performance
strategy_recommendation_collection = db['strategy_recommendation']  # Collection for Strategy Recommendation

# Home page route
@app.route("/")
def index():
    return render_template("index.html")

# Login page route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        designation = request.form["Designation"]

        hashed_password = generate_password_hash(password)

        # Insert user data into MongoDB
        users_collection = db['users']
        users_collection.insert_one({
            "username": username,
            "password": hashed_password,
            "designation": designation
        })

        return redirect(url_for("dashboard", username=username))
    return render_template("login.html")

# Dashboard page route
@app.route("/dashboard/<username>")
def dashboard(username):
    user_data = db['users'].find_one({"username": username})
    return render_template("dashboard.html", user=user_data)

# About page route
@app.route('/about')
def about():
    return render_template('about.html')

# Services page route
@app.route('/services')
def services():
    return render_template('services.html')

# Clean and preprocess the text
def clean_text(text):
    text = re.sub(r'Review collected by and hosted on G2.com', '', text)
    text = text.strip().replace('"', '')
    return text

def preprocess_text(text):
    stop_words = {"the", "and", "is", "in", "to", "a", "of", "for", "on", "that", "it", "with", "as", "this", "by", "at", "from"}
    tokens = re.findall(r'\b\w+\b', text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(tokens)

# Peer Sentiment Analysis route
@app.route('/peer_sentiment_analysis', methods=["GET", "POST"])
def peer_sentiment_analysis():
    sentiment_result = None
    if request.method == "POST":
        text = request.form['text_input']
        cleaned_text = preprocess_text(clean_text(text))
        text_tfidf = tfidf_vectorizer.transform([cleaned_text])
        prediction = model2_peer_sentiment_analysis.predict(text_tfidf)[0]
        sentiment_result = "Positive" if prediction == 1 else "Negative"
        
        # Store the input data and prediction in MongoDB
        peer_sentiment_collection.insert_one({
            "text_input": text,
            "cleaned_text": cleaned_text,
            "prediction": sentiment_result
        })
    
    return render_template('peer_sentiment_analysis.html', sentiment_result=sentiment_result)

# Employee Performance route
@app.route("/employee_performance", methods=["GET", "POST"])
def employee_performance():
    prediction = None
    if request.method == "POST":
        try:
            # Ensure the model and scaler are loaded (only once)
            global model, scaler
            if 'model' not in globals() or 'scaler' not in globals():
                with open('D:\\clg work\\5th sem\\MINOR PROJECT THINGS\\PROJECT\\models\\model4_employee_analysis.pkl', 'rb') as f:
                    model = pickle.load(f)
                
                with open('D:\\clg work\\5th sem\\MINOR PROJECT THINGS\\PROJECT\\models\\scaler.pkl', 'rb') as f:
                    scaler = pickle.load(f)

            # Get form data (with validation)
            job_involvement = float(request.form["job_involvement"])
            performance_rating = float(request.form["performance_rating"])
            work_life_balance = float(request.form["work_life_balance"])
            job_level = float(request.form["job_level"])
            monthly_income = float(request.form["monthly_income"])

            # Prepare input data for prediction
            input_data = np.array([[job_involvement, performance_rating, work_life_balance, job_level, monthly_income]])

            # Scale the input data using the pre-loaded scaler
            input_data_scaled = scaler.transform(input_data)

            # Make the prediction using the pre-trained model
            prediction = model.predict(input_data_scaled)[0]

            # Store the input data and prediction in MongoDB
            employee_performance_collection.insert_one({
                "job_involvement": job_involvement,
                "performance_rating": performance_rating,
                "work_life_balance": work_life_balance,
                "job_level": job_level,
                "monthly_income": monthly_income,
                "prediction": prediction
            })
        except ValueError as ve:
            print(f"Error: Invalid input values - {ve}")
            prediction = "Invalid input values. Please check your inputs."
        except Exception as e:
            print(f"Error: {e}")
            prediction = "An error occurred while processing your request."
    
    return render_template("employee_performance.html", prediction=prediction)


@app.route("/strategy_recommendation", methods=["GET", "POST"])
def strategy_recommendation():
    prediction = None
    if request.method == "POST":
        try:
            # Get form input values
            strength = float(request.form["strength"])
            weakness = float(request.form["weakness"])
            opportunities = float(request.form["opportunities"])
            threats = float(request.form["threats"])
            
            # Prepare the input data for prediction
            input_data = np.array([[strength, weakness, opportunities, threats]])
            
            # Predict the strategy using the model
            predicted_strategy = model.predict(input_data)
            
            # Convert prediction to a readable form (if encoded numerically)
            prediction = predicted_strategy[0]  # Extract the first prediction result
        except Exception as e:
            print(f"Error during prediction: {e}")
            prediction = "Error during prediction. Please check input values."
    
    return render_template("strategy_recommendation.html", prediction=prediction)
            
             
            
            
    
    return render_template("strategy_recommendation.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=False)
