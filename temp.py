import pandas as pd
import csv
df=pd.read_csv("./Output CSVs/output_card_fixed.csv")

print(df["class"])

# fieldnames = ['text', 'class']
# with open("./Output CSVs/output_card_fixed.csv", 'w', newline='',encoding='utf-8') as file_out:
    
#     writer = csv.DictWriter(file_out, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in df["text"]:
#         writer.writerow({'text': row, 'class': "card-fraud"})