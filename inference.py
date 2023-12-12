from transformers import RobertaTokenizer,RobertaForSequenceClassification
import torch 
from torch.nn.functional import softmax


def classify_pytorch(text):    
# # Load pre-trained RoBERTa tokenizer and model
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    num_labels = 3
    model = RobertaForSequenceClassification.from_pretrained('roberta-base',num_labels=num_labels)
    
    model_state_dict = torch.load('./model/pytorch_model.bin', map_location=torch.device('cpu'))  

    # Load the state dictionary into the model
    model.load_state_dict(model_state_dict,strict=False)

    inputs=tokenizer(text,padding=True, truncation=True, return_tensors='pt')

# # Set the model to evaluation mode
    model.eval()

# # Tokenize the input text and prepare it for the model
    # inputs = tokenizer.encode_plus(
    #     text,
    #     add_special_tokens=True,
    #     return_tensors="pt",
    #     max_length=512,  # Adjust the maximum sequence length as needed
    #     padding='max_length',
    #     truncation=True
    # )

# # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)
    _, predicted = torch.max(outputs.logits, 1)


# # Get the predicted probabilities and predicted class
    probs = softmax(outputs.logits, dim=1)
    predicted_class = predicted.item()
    
# # Output the predicted class and probabilities
    class_names = ['hacking','drugs','card-fraud']  # Replace with your class names
    print("Predicted class:", class_names[predicted_class])
    print("Predicted probabilities:", probs.squeeze().tolist())


if __name__ == "__main__": 
    text = "buy for free"
    classify_pytorch(text)