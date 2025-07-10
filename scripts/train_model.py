# Train Linear Regression model

from sklearn.linear_model import LinearRegression
import joblib

def train(X_train, y_train, model_path='models/linear_model.pkl'):
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
