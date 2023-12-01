from pymongo import MongoClient
def get_database():

   CONNECTION_STRING = "mongodb://localhost:27017/capstone"

   client = MongoClient(CONNECTION_STRING)
 

   return client['capstone']
  
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
   collection_name = dbname["cardFraud"]
   item_details = collection_name.find()
   
   for item in item_details:
    # This does not give a very readable output
        print(item)
    