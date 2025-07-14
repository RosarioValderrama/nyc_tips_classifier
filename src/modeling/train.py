import joblib
from sklearn.ensemble import RandomForestClassifier

def train_model(X, y, model_path: str = "models/random_forest_model.joblib"):
    model = RandomForestClassifier(n_estimators=100, max_depth=10)
    model.fit(X, y)
    joblib.dump(model, model_path)
    return model
