import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

def process_user_input_and_predict(age, gender, csv_file):    # Load the trained model
    model = joblib.load("static/firstModelForMusicPred")  # Replace with the correct model file path
    
    # Process the CSV file
    df = pd.read_csv(csv_file)
    
    # Create a DataFrame with user input
    user_data = pd.DataFrame({'age': [age], 'gender': [gender]})
    
    # Use the loaded model to make predictions
    predictions = model.predict(user_data)
    
    return predictions
