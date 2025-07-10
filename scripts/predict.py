# Predict on new input

import joblib
import numpy as np

def predict(new_data, model_path='models/linear_model.pkl'):
    model = joblib.load(model_path)
    return model.predict(np.array(new_data).reshape(1, -1))
