def generate_observation(symptoms):

    if not symptoms:

        return "No major symptom pattern detected."

    cardiac = [

        "chest pain",
        "shortness of breath",
        "palpitations"

    ]

    respiratory = [

        "cough",
        "wheezing",
        "shortness of breath"

    ]

    neurological = [

        "headache",
        "memory loss",
        "tremors",
        "dizziness",
        "muscle weakness"

    ]

    if any(s in symptoms for s in cardiac):

        return (
            "Potential cardiac-related pattern detected. "
            "Further evaluation recommended."
        )

    if any(s in symptoms for s in respiratory):

        return (
            "Potential respiratory-related pattern detected."
        )

    if any(s in symptoms for s in neurological):

        return (
            "Potential neurological-related pattern detected."
        )

    return (
        "Symptoms detected but pattern is unclear."
    )