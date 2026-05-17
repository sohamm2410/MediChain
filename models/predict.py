from utils import predict_disease

# Sample clinical note
sample_note = "Patient reports chest pain and shortness of breath"

# Get prediction
prediction, confidence = predict_disease(sample_note)

# Display result
print("\nClinical Note:")
print(sample_note)

print("\nPredicted Disease Category:")
print(prediction)

print(f"\nConfidence Score: {confidence:.2f}%")