import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the data
data = pd.read_csv('C:\\Users\\lenovo 2020\\strategy using SWOT.csv')

# Check for any missing values (you can handle them if needed)
if data.isnull().sum().any():
    print("Missing values found. Handle them before proceeding.")
    data = data.dropna()  # or use a filling method like data.fillna(...)

# Split into features (X) and target (y)
X = data[['Strength', 'Weakness', 'Opportunities', 'Threats']] # These are numerical features
y = data['Strategy']  # Target variable (strategy) which is also numeric

# Split data into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
train = RandomForestClassifier(random_state=42)
train.fit(X_train, y_train)

# Save the trained model to a file
model_filename = 'D:\\clg work\\5th sem\\MINOR PROJECT THINGS\\PROJECT\\models\\model3_strategy_recommendation_model.pkl'
with open(model_filename, 'wb') as model_file:
    pickle.dump(train, model_file)

# Save the target encoder (if needed) to a file (but in this case, it's not needed because Strategy is numeric)
# encoder_filename = 'D:\\clg work\\5th sem\\MINOR PROJECT THINGS\\PROJECT\\models\\for_strategy_label_encoder.pkl'
# with open(encoder_filename, 'wb') as encoder_file:
#     pickle.dump(label_encoder, encoder_file)

print("Model saved successfully.")

 

