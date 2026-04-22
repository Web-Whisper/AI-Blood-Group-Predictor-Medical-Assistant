import random

blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

def predict_blood_group(image):
    prediction = random.choice(blood_groups)
    confidence = round(random.uniform(75, 98), 2)

    return prediction, confidence
