from pymongo import MongoClient
import csv
import os

# mongodb://localhost:27017/capstone

CONNECTION_STRING_LOCAL="mongodb://localhost:27017/capstone"
def put_data(url,label,text):
   client = MongoClient(CONNECTION_STRING_LOCAL)
   db=client['capstone']
   collection=db[label]

   data={
            "url":url,
            "class":label,
            "other":text
         }
   
   collection.insert_one(data)
   
def create_csv(text, label):
    file_path = "output.csv"
    fieldnames = ['text', 'class']

    if not os.path.exists(file_path):  
        with open(file_path, "w", newline='') as file:  
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'text': text, 'class': label})
    else:
        with open(file_path, "a", newline='') as file:  # Use 'a' to append to an existing file
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'text': text, 'class': label})

   

if __name__ == "__main__":   
   create_csv('this is a card fraud website','card-fraud')