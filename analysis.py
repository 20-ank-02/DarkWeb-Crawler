from transformers import RobertaTokenizer,RobertaForSequenceClassification
import torch 
from torch.nn.functional import softmax
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix 
  
df = pd.read_csv('dataset.csv')

text = df['text'].tolist()
labels = df['class'].tolist()

# Assuming y_test contains text labels
# label_map = {label: i for i, label in enumerate(set(labels))}
# labels = [label_map[label] for label in labels]

label_encoder = LabelEncoder()
y_test_encoded = label_encoder.fit_transform(labels)

y_test_encoded=list(np.where(y_test_encoded==2,0,y_test_encoded))

for i in range(0,21):
    y_test_encoded[i]=2

# # Load pre-trained RoBERTa tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
num_labels = 3
model = RobertaForSequenceClassification.from_pretrained('roberta-base',num_labels=num_labels)

# model_state_dict = torch.load('./model/pytorch_model.bin', map_location=torch.device('cpu'))  

# # Load the state dictionary into the model
# model.load_state_dict(model_state_dict,strict=False)

inputs=tokenizer(text,padding=True, truncation=True, return_tensors='pt')

# # Set the model to evaluation mode
model.eval()

# # Perform inference
with torch.no_grad():
    outputs = model(**inputs)
_, predicted = torch.max(outputs.logits, 1)

predicted_labels = predicted.numpy()

# Calculate accuracy
accuracy = accuracy_score(y_test_encoded, predicted_labels)
print(f'Accuracy: {accuracy}')

# Calculate F1-score
f1 = f1_score(y_test_encoded, predicted_labels, average='weighted')
print(f'F1-score: {f1}')

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_test_encoded, predicted_labels)
print('Confusion Matrix:')
print(conf_matrix)

