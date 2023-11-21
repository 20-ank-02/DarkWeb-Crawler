from transformers import pipeline
import torch 
# Example text with a masked token
text = "This is a great movie!"

classifier = pipeline("text-classification", model="roberta-base")
result = classifier(text)

print("Predicted label:", result[0]['label'])