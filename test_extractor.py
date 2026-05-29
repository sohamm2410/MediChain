from models.entity_extractor import extract_symptoms

note = """
Patient reports chest pain and shortness of breath
"""

print(extract_symptoms(note))