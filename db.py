from pymongo import MongoClient
import csv
# 256ZxCpwWcrEMe9N
# 20ankityadav02

# mongodb://localhost:27017/capstone
# CONNECTION_STRING = "mongodb+srv://20ankityadav02:256ZxCpwWcrEMe9N@clustercp.w9c49f9.mongodb.net/?retryWrites=true&w=majority"
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

    