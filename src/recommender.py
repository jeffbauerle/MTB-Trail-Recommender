import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt

# def get_trail_recommendations(trail_name, X, n=5):
#     index = all_df.index[(all_df['id'] == trail_name)][0]
#     trail = X[index].reshape(1,-1)
#     cs = cosine_similarity(trail, X)
#     # cs = euclidean_distances(trail, X)
#     rec_index = np.argsort(cs)[0][::-1][1:]
#     ordered_df = all_df.loc[rec_index]
#     rec_df = ordered_df.head(n)
#     orig_row = all_df.loc[[index]].rename(lambda x: 'original')
#     total = pd.concat((orig_row,rec_df))
#     return total

def get_trail_recommendations(trail_name, X, n=5):
    # for region in all_df['location'].unique():
    #     print(region)

    # region = input("Enter your region: ")
    # is_region = all_df['location'] == region
    # region_df = all_df[is_region]

    index = all_df.index[(all_df['id'] == trail_name)][0]
    trail = X[index].reshape(1,-1)
    cs = cosine_similarity(trail, X)
    # cs = euclidean_distances(trail, X)
    rec_index = np.argsort(cs)[0][::-1][1:]
    ordered_df = all_df.loc[rec_index]
    rec_df = ordered_df.head(n)
    orig_row = all_df.loc[[index]].rename(lambda x: 'original')
    total = pd.concat((orig_row,rec_df))
    return total

if __name__ == "__main__":

    # load the pickled model
    with open('../data/X.pkl', 'rb') as f:
        X = pickle.load(f)

    # load the df
    all_df = pd.read_pickle('../data/df.pkl')
    trail_id = 4670265
    # print(get_trail_recommendations(trail_id,X,n=5))
    for region in all_df['location'].unique():
        print(region)

    # assign_features()
    # print(all_df.describe())
    # print(all_df.loc[all_df['id'] == 7029147])
    # plt.plot(all_df['return_start'])
    # print(all_df['location'].unique())
    # for region in all_df['location'].unique():
    #     print(region)
    # print(all_df.columns)

    #Get regional trail list 
    region = input("Enter your region: ")
    is_region = all_df['location'] == region
    region_df = all_df[is_region]
    # is_region = all_df['location']
    # trails_in_region = is_region[is_region['name']]

    # work in progress
    for trail in region_df['name'].unique():
        print(trail)
    trail_name = input("Select your trail: ")
    trail_df = region_df[region_df['name'] == trail_name]
    trail_id = trail_df.id.values[0]
    print(trail_id)

    print(get_trail_recommendations(trail_id,X,n=5))

    # List trails for dropdown
    # for trail in all_df['name'].unique():
    #     print(trail)



    # print(region_df.head())
    # plt.savefig('../images/return_start.png')
    # plt.show()





    


    