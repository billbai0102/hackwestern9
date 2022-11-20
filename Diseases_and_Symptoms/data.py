import pandas as pd
import cohere

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
    print("name: ", name[i])
    print("desc: ", desc[i])
    print("embed: ", embeds[i])
    print()

print("done")