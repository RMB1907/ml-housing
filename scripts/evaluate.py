# Evaluate metrics

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

def evaluate(model_path, X_test, y_test):
    model = joblib.load(model_path)
    preds = model.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, preds))
    print("MSE:", mean_squared_error(y_test, preds))
    print("R²:", r2_score(y_test, preds))
