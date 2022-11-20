from getDatabase import get_database
import pandas as pd
import cohere

dbname = get_database()
collection_name = dbname["hackwestern"]


descriptions = pd.read_csv("./archive/symptom_Description.csv")

co = cohere.Client("JuqpapPUIT9dRAH5a06D4rIj7tTnbWVwY59dY4eC")
texts = descriptions['Description'].tolist()
response = co.embed(
    model='large',
    texts=texts)

name = descriptions['Disease'].tolist()
desc = descriptions['Description'].tolist()
embeds = response.embeddings


for i in range(len(name)):
    item = {
        "name" : name[i],
        "desc" : desc[i],
        "embed" : embeds[i]
    }
    collection_name.insert_one(item)
