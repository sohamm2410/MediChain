import pickle

# Load trained model
with open("models/saved_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Load vectorizer
with open("models/vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


def predict_disease(text):

    # Convert input text
    text_vectorized = vectorizer.transform([text])

    # Predict disease
    prediction = model.predict(text_vectorized)[0]

    # Predict probabilities
    probabilities = model.predict_proba(text_vectorized)

    # Confidence score
    confidence = max(probabilities[0]) * 100

    return prediction, confidence