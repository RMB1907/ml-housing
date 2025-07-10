from scripts.fetch_data import load_data
from scripts.preprocess import split_data
from scripts.train_model import train
from scripts.evaluate import evaluate

# Load and process data
df = load_data()
X_train, X_test, y_train, y_test = split_data(df)

# Train model and save to models/linear_model.pkl
train(X_train, y_train)

# Evaluate model
evaluate('models/linear_model.pkl', X_test, y_test)
