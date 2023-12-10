from pymongo import MongoClient
import csv


# mongodb://localhost:27017/capstone

CONNECTION_STRING_LOCAL="mongodb://localhost:27017/capstone"
def put_data(url,label,text):
   client = MongoClient(CONNECTION_STRING_LOCAL)
   db=client['capstone']
   collection=db["cardFraud"]

   data={
            "url":url,
            "class":label,
            "other":text
         }
   
   collection.insert_one(data)
   
def create_csv(text,label):
   fieldnames = ['text', 'class']
   file_path = "output.csv"
   with open(file_path, "a") as file:
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerow({'text': text, 'class': label})
    

   

if __name__ == "__main__":   
   create_csv('this is a card fraud website','card-fraud')

    
