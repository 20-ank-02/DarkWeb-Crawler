from transformers import pipeline
import csv
import torch 

# Example text 


def classify(url,text):
    classifier = pipeline("text-classification", model="roberta-base")
    result = classifier(text)
    myDict={'url':url,'class':result[0]['label']}
    print(myDict)
    
    columns=['url','class']
    filename='output.csv'
    with open(filename, 'w',newline='') as csvfile:  
        # creating a csv dict writer object  
        writer = csv.DictWriter(csvfile, fieldnames = columns)  
            
        # writing headers (field names)  
        writer.writeheader()  
            
        # writing data rows  
        writer.writerow(myDict)  

if __name__ == "__main__": 
    text = "This is a card fraud site!"
    classify('xyz.onion',text)