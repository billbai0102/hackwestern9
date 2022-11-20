import json

import cohere
from scipy.spatial.distance import cosine
from annoy import AnnoyIndex
import pandas as pd


class CohereFuncs:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.co = cohere.Client(apiKey)

    def get_embedding_from_report(self, report):
        response = self.co.embed(model='large', texts=[report])
        return response.embeddings[0]

    def get_similar_disease(self, report):
        data = self.get_data_from_mongo()
        embeds = [d['embed'] for d in data]
        report_embed = self.get_embedding_from_report(report)
        search_index = AnnoyIndex(len(report_embed), 'angular')
        for i in range(len(embeds)):
            search_index.add_item(i, embeds[i])
        search_index.build(10)

        similar_item_ids = search_index.get_nns_by_vector(report_embed, 2, include_distances=True)

        for i in similar_item_ids[0]:
            print(data[i]['name'])
            print(data[i]['desc'])

        return similar_item_ids

    def get_data_from_mongo(self):
        # mongo.getData("lucy-wang-instance-v2")
        descriptions = pd.read_csv("./Diseases_and_Symptoms/archive/symptoms_reports.csv")
        name = descriptions['Disease'].tolist()
        desc = descriptions['Description'].tolist()
        embeds = self.co.embed(model='large', texts=desc).embeddings
        list = []
        for i in range(len(name)):
            list.append({
                "name": name[i],
                "desc": desc[i],
                "embed": embeds[i]
            })

        return list


if __name__ == '__main__':
    cf = CohereFuncs("JuqpapPUIT9dRAH5a06D4rIj7tTnbWVwY59dY4eC")
    print(cf.get_similar_disease("the patient has itchy blisters all over the body. we have medicated them with topical cream!"))

