from transformers import pipeline,RobertaTokenizer,RobertaForSequenceClassification
import torch 
from torch.nn.functional import softmax


def classify_pytorch(text):    
# # Load pre-trained RoBERTa tokenizer and model
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    model = RobertaForSequenceClassification.from_pretrained('roberta-base')

# # Set the model to evaluation mode
    model.eval()

# # Tokenize the input text and prepare it for the model
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        return_tensors="pt",
        max_length=512,  # Adjust the maximum sequence length as needed
        padding='max_length',
        truncation=True
    )

# # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)

# # Get the predicted probabilities and predicted class
    probs = softmax(outputs.logits, dim=1)
    predicted_class = torch.argmax(probs, dim=1).item()
    print(predicted_class)
# # Output the predicted class and probabilities
    class_names = ['Sports', 'Politcs', 'Entertainment']  # Replace with your class names
    print("Predicted class:", class_names[predicted_class])
    print("Predicted probabilities:", probs.squeeze().tolist())



def classify(text):
    classifier = pipeline("text-classification", model="roberta-base")
    result = classifier(text)
    return result

if __name__ == "__main__": 
    text = "we are going to arrange an elections for upcomming prime minister!"
    print(classify(text))
    classify_pytorch(text)