import joblib

def load_model():
    model_path = 'static/firstModelForMusicPred'  # Update with the actual path
    loaded_model = joblib.load(model_path)
    return loaded_model

def make_predictions(model, input_data):
    predictions = model.predict(input_data)
    return predictions