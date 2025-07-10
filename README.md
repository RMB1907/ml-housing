# Housing Price Prediction using Linear Regression

A basic ML pipeline to predict house prices from housing.csv.

---

## Setup

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## How to Run

### Train and Evaluate the Model

Train and evaluate the model using housing.csv. The trained model is saved to models/linear_model.pkl.

```bash
python run_pipeline.py
```

---

### Predict from CLI Input

After training the model, predict the house price by entering feature values manually:

```bash
python run_predict_from_cli.py
```

Example input when prompted:

```
75000, 5.5, 6.8, 3, 25000
```

Format:  
[Income, House Age, Rooms, Bedrooms, Population]

---

