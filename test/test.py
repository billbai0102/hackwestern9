import cohere
from scipy.spatial.distance import cosine
import pandas as pd

if __name__ == '__main__':
    ds = pd.read_csv("../Diseases_and_Symptoms/archive/symptoms_reports.csv")
    print(ds['Disease'])
    print(ds['Description'])
    # co = cohere.Client("JuqpapPUIT9dRAH5a06D4rIj7tTnbWVwY59dY4eC")
    # texts = ["hello", "world", "my", "name", "is", "bill bai", "name", "label", "green", "taylor swift"]
    #
    # response = co.embed(
    #     model='large',
    #     texts=texts)
    # print('Embeddings: {}'.format(response.embeddings))
    #
    # embedding1 = response.embeddings[0]
    #
    # for i, embedding in enumerate(response.embeddings):
    #     print(f'Word1: {texts[0]}, Word2: {texts[i]}, Similarity: {cosine(embedding1, embedding)}')


