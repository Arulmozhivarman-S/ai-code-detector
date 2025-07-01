import joblib
from src.preprocess import clean_code
from src.feature_extraction import get_embedding

def classify_code(code_snippet: str, model_path="model.pkl"):
    
    clf = joblib.load(model_path)
    
    cleaned = clean_code(code_snippet)
    embedding = get_embedding(cleaned).reshape(1, -1)
    
    prediction = clf.predict(embedding)[0]
    return "Human" if prediction == 0 else "ChatGPT"