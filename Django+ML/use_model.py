# use_model.py
import joblib

# Load the saved model
model = joblib.load('iris_model.pkl')

# Example input (4 features of an iris flower)
# sample_input = [[5.1, 3.5, 1.4, 0.2]]  # This should predict class 0 (Setosa)
# sample_input = [[6.0, 2.9, 4.5, 1.5]]  # → Predicts 1 (Versicolor)
sample_input = [[6.9, 3.1, 5.4, 2.1]]  # → Predicts 2 (Virginica)

# Predict
prediction = model.predict(sample_input)

print(f"Predicted class: {prediction[0]}")