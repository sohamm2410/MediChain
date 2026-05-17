from models.utils import predict_disease

test_notes = [

    "Chest pain and dizziness",
    "Persistent cough and fever",
    "Muscle weakness and tremors",
    "Frequent urination and high glucose",
    "Joint inflammation and stiffness"

]

for note in test_notes:

    prediction, confidence = predict_disease(note)

    print("\n-----------------------------------")
    print(f"Clinical Note: {note}")
    print(f"Prediction: {prediction}")
    print(f"Confidence: {confidence:.2f}%")