import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import GradientBoostingRegressor
import pickle

data=pd.read_csv('C:\\Users\\lenovo 2020\\employee analysis.csv')
data.head()

new_dataset=data.copy()

Q1=data['MonthlyIncome'].quantile(0.25)
Q3=data['MonthlyIncome'].quantile(0.75)
IQR=Q3-Q1
min_range=Q1-(1.5*IQR)
max_range=Q3+(1.5*IQR)
new_dataset['MonthlyIncome']=data['MonthlyIncome']<=max_range

data=new_dataset

data['final_score'] =   np.where(
    data['Attrition'] == 'No',
    np.round(
        (0.3 * data['JobInvolvement'] / data['JobInvolvement'].max() +
         0.3 * data['PerformanceRating'] / data['PerformanceRating'].max() +
         0.2 * data['WorkLifeBalance'] / data['WorkLifeBalance'].max() +
         0.1 * data['JobLevel'] / data['JobLevel'].max() +
         0.1 * data['MonthlyIncome'] / data['MonthlyIncome'].max()) * 10
    ).astype(int),  # Round and convert to integer
    np.nan  # For employees with Attrition = "Yes", keep it as NaN
)

data.dropna(subset=['final_score'], inplace=True)
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

data.info()

# Example: Select the 5 features
features = ['JobInvolvement', 'PerformanceRating', 'WorkLifeBalance', 'JobLevel', 'MonthlyIncome']

# Assuming 'df' is your dataset, select the features and target
X = data[features]  # Select only the 5 features
y = data['final_score']  # Assuming 'PerformanceScore' is the target variable

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the model (e.g., GradientBoostingRegressor)
model = GradientBoostingRegressor()
model.fit(X_scaled, y)

# Save the model and scaler for later use
import pickle
with open('D:\\clg work\\5th sem\\MINOR PROJECT THINGS\\PROJECT\\models\\model4_employee_analysis.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('D:\\clg work\\5th sem\\MINOR PROJECT THINGS\\PROJECT\\models\\scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)


 

