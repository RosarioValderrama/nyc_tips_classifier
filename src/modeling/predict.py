import joblib
from sklearn.metrics import f1_score

def load_model(model_path: str = "models/random_forest_model.joblib"):
    return joblib.load(model_path)

def evaluate_model(model, X, y):
    y_pred = model.predict(X)
    return f1_score(y, y_pred)
