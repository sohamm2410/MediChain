import pickle

# Load model
with open("models/saved_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load vectorizer
with open("models/vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Prediction function
def predict_disease(text):

    text_vectorized = vectorizer.transform([text])

    prediction = model.predict(text_vectorized)

    return prediction[0]


# Test prediction
sample_note = "Persistent cough and fever"

result = predict_disease(sample_note)

print(f"Predicted Disease Category: {result}")