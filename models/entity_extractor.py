SYMPTOMS = [

    "chest pain",
    "shortness of breath",
    "fatigue",
    "fever",
    "cough",
    "headache",
    "dizziness",
    "muscle weakness",
    "tremors",
    "memory loss",
    "high blood sugar",
    "thirst",
    "wheezing",
    "palpitations"

]

def extract_symptoms(text):

    detected = []

    text = text.lower()

    for symptom in SYMPTOMS:

        if symptom in text:

            detected.append(symptom)

    return detected