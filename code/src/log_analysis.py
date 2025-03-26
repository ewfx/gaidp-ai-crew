import pandas as pd
import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load Banking Logs dataset
def load_logs():
    dataset = load_dataset("Daniel-ML/sentiment-analysis-for-financial-news-v2", 
                           split="train")
    df = pd.DataFrame(dataset)
    #df['timestamp'] = pd.to_datetime(df['timestamp'])  # Convert to timestamp
    return df

# Load Pre-trained Anomaly Detection Model
model_name = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", 
                                                           num_labels=2)


# Predict anomalies
def detect_anomalies(logs):
    inputs = tokenizer(logs, 
                       return_tensors="pt", 
                       truncation=True, 
                       padding=True)
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1).tolist()
    return ["Anomaly" if pred == 1 else "Normal" for pred in predictions]
