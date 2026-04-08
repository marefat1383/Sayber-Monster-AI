import time
import random

def predict_deepfake(file_path: str, filename: str) -> dict:
    time.sleep(1.5)
    
    filename_lower = filename.lower()
    if 'fake' in filename_lower or 'scam' in filename_lower:
        score = random.uniform(75.0, 98.0)
    elif 'real' in filename_lower or 'authentic' in filename_lower:
        score = random.uniform(2.0, 15.0)
    else:
        score = random.uniform(10.0, 90.0) 
        
    if score < 30:
        label_key = "Likely Authentic"
    elif score < 70:
        label_key = "Suspicious"
    else:
        label_key = "Likely AI-Generated"
        
    return {
        "confidence_fake": round(score, 2),
        "label_key": label_key
    }

def get_security_recommendation_keys(label_key: str) -> list:
    if label_key == "Likely Authentic":
        return ["rec_auth_1", "rec_auth_2", "rec_auth_3"]
    elif label_key == "Suspicious":
        return ["rec_susp_1", "rec_susp_2", "rec_susp_3"]
    else:
        return ["rec_fake_1", "rec_fake_2", "rec_fake_3", "rec_fake_4"]
