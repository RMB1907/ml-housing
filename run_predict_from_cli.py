from scripts.predict import predict

# Prompt user for input with example
user_input = input(
    "Enter values for [Income, House Age, Rooms, Bedrooms, Population]\n"
    "Example: 75000, 5.5, 6.8, 3, 25000\n> "
)

# Convert to float list
try:
    features = [float(x.strip()) for x in user_input.split(",")]
    if len(features) != 5:
        raise ValueError("Expected 5 values.")

    # Predict
    predicted_price = predict(features)
    print(f"Predicted House Price: ₹{predicted_price[0]:,.2f}")

except ValueError as e:
    print("Invalid input:", e)
