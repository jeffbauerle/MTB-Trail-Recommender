import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
# load the pickled model
with open('../data/X.pkl', 'rb') as f:
    X = pickle.load(f)

# load the df
all_df = pd.read_pickle('../data/df.pkl')

# with open('../data/df.pkl','rb') as f:
#     df = pickle.load(f)    
    
# with open('../data/mtn_df.pkl','rb') as f:
#     mtn_df = pickle.load(f)
    
 
def get_regions():    
    regions = {"denver": "Denver", "moab": "Moab","crested_butte": "Crested Butte", "marin_county": "Marin County", "sedona":"Sedona","park_city":"Park City"}
    return regions

def get_trails_by_region(region):
    # use region to get trails
    is_region = all_df['location'] == region
    region_df = all_df[is_region]
    trails = []
    for name in region_df['name'].unique():        
        trail_df = region_df[region_df['name'] == name]
        trail_id = trail_df.id.values[0]
        trails.append({"id":trail_id, "name": name})
    return trails

def get_recommended_trails_by_trail(source_trail):
    trails = [{"id": "1", "name": "Trail Rec 1"},{"id": "2", "name": "Trail Rec 2"}]
    return trails

def get_recommended_trails_by_region_and_trail(dst_region, source_trail_id, n):
    return get_trail_recommendations(source_trail_id, X, n)    

def get_trail_recommendations(trail_id, X, n=5):
    print(trail_id)
    print(X)
    # for region in all_df['location'].unique():
    #     print(region)
    # region = input("Enter your region: ")
    # is_region = all_df['location'] == region
    # region_df = all_df[is_region]    
    
    index = all_df.index[(all_df['id'] == int(trail_id))][0]
    trail = X[index].reshape(1,-1)
    cs = cosine_similarity(trail, X)
    
    # cs = euclidean_distances(trail, X)
    rec_index = np.argsort(cs)[0][::-1][1:]
    ordered_df = all_df.loc[rec_index]
    rec_df = ordered_df.head(n)
    orig_row = all_df.loc[[index]].rename(lambda x: 'original')
    total = pd.concat((orig_row,rec_df))
    print(total.head(5))    
    print(total.columns)    

    
    return convert_data(total)

def convert_data(df):
    trails = []
    for _, row in df.iterrows():        
        trails.append({"id":row['id'],"name":row['name'],"type":row['type'],"summary":row['summary'],"difficulty":row['difficulty'],"stars":row['stars'],"starVotes":row['starVotes'],"location":row['location'],"url":row['url'],"length":row['length'],"ascent":row['ascent'],"descent":row['descent'],"high":row['high'],"low":row['low'],"longitude":row['longitude'],"latitude":row['latitude'],"max_grade":row['max_grade'],"climb_desc":row['climb_desc'],"return_start":row['return_start']})
    return trails