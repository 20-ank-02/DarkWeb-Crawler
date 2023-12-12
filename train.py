import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('dataset.csv')

texts = df['text'].tolist()
labels = df['class'].tolist()
# print(type(texts[1528]),texts[1528])
# i=1
# for text in texts:
#     print(i,type(text))
#     i+=1

model_name = 'roberta-base'
tokenizer = RobertaTokenizer.from_pretrained(model_name)
model = RobertaForSequenceClassification.from_pretrained(model_name, num_labels=len(set(labels)))

# Tokenize the texts
tokenized_texts = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

# Convert labels to integers
label_map = {label: i for i, label in enumerate(set(labels))}
labels = [label_map[label] for label in labels]

# Split the dataset into train and validation sets
train_texts, val_texts, train_labels, val_labels = train_test_split(
    tokenized_texts.input_ids, labels, test_size=0.2, random_state=42
)

# Convert the data to PyTorch tensors
train_dataset = torch.utils.data.TensorDataset(train_texts, torch.tensor(train_labels))
val_dataset = torch.utils.data.TensorDataset(val_texts, torch.tensor(val_labels))

# Define training parameters and optimizer
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
batch_size = 16
epochs = 3

# Create data loaders for training and validation
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=batch_size)

# Training loop
model.train()
for epoch in range(epochs):
    for batch in train_loader:
        optimizer.zero_grad()
        input_ids, labels = batch
        outputs = model(input_ids, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

# Save the model
output_model_dir = './model/'
model.save_pretrained(output_model_dir)
tokenizer.save_pretrained(output_model_dir)

# Validation loop
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for batch in val_loader:
        input_ids, labels = batch
        outputs = model(input_ids)
        _, predicted = torch.max(outputs.logits, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = correct / total
print(f'Validation accuracy: {accuracy}')

