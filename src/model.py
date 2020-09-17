import json
import pandas as pd
import numpy as np
from pandas import json_normalize
import pickle
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from sklearn.preprocessing import StandardScaler
import warnings
from gpx_process import get_gpx_features
import os
warnings.filterwarnings('ignore')


def load_trail_df_from_file(filename, location_name):
    with open(filename) as data_file:
        data = json.load(data_file)
    data_trails = data['trails']
    data_df = json_normalize(data_trails)
    data_df["location"] = location_name
    return data_df


def get_trail_recommendations(trail_name, X, n=5):
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


    

    # Denver
    denver_file = '../data/denver.json'
    denver_df = load_trail_df_from_file(denver_file, "denver")

    # Park City
    park_city_file = '../data/parkcity.json'
    park_city_df = load_trail_df_from_file(park_city_file, "park_city")

    # Moab
    moab_file = '../data/moab.json'
    moab_df = load_trail_df_from_file(moab_file, "moab")

    # Sedona
    sedona_file = '../data/sedona.json'
    sedona_df = load_trail_df_from_file(sedona_file, "sedona")

    # Marin County
    marin_county_file = '../data/marincounty.json'
    marin_county_df = load_trail_df_from_file(marin_county_file,
                                              "marin_county")

    # Crested Butte
    crested_butte_file = '../data/crestedbutte.json'
    crested_butte_df = load_trail_df_from_file(crested_butte_file,
                                               "crested_butte")

    loc_dict = {"denver": "Denver",
                "crested_butte": "Crested Butte",
                "marin_county": "Marin County",
                "sedona": "Sedona",
                "park_city": "Park City",
                "moab": "Moab"}

    color_dict = {"Green": ["green", "green"],
                  "Green Blue": ["greenBlue", "#0d98ba"],
                  "Blue": ["blue", "blue"],
                  "Blue Black": ["blueBlack", "#003366"],
                  "Black": ["black", "black"]}

    # MTB_Trail_Data_EDA

    all_df = pd.concat([crested_butte_df, marin_county_df,
                       denver_df, park_city_df, sedona_df, moab_df])

    all_df['max_grade'] = 0
    cb_ids = set(crested_butte_df['id'])

    mc_ids = set(marin_county_df['id'])
    den_ids = set(denver_df['id'])
    pc_ids = set(park_city_df['id'])
    sed_ids = set(sedona_df['id'])
    moab_ids = set(moab_df['id'])


    print(all_df.head())

    # (['id', 'name', 'type', 'summary', 'difficulty', 'stars', 'starVotes',
    #    'location', 'url', 'imgSqSmall', 'imgSmall', 'imgSmallMed', 'imgMedium',
    #    'length', 'ascent', 'descent', 'high', 'low', 'longitude', 'latitude',
    #    'conditionStatus', 'conditionDetails', 'conditionDate'],
    #   dtype='object')

    drop_list = ['imgSqSmall', 'imgSmall', 'imgSmallMed', 'imgMedium', 'conditionStatus', 'conditionDetails', 'conditionDate']
    all_df = all_df.drop(drop_list, axis=1)


    keep_list = ['length', 'difficulty', 'ascent', 'descent', 'high', 'low']
    features = all_df[keep_list]
    all_df = all_df[all_df.type != 'Connector']
    all_df = all_df[all_df.difficulty != 'missing']
    diff_colors = ['green', 'greenBlue', 'blue', 'blueBlack', 'black', 'dblack']
    diff_vals = [1,2,3,4,5,6]
    all_df['difficulty'] = all_df['difficulty'].replace(diff_colors, diff_vals)
    print(all_df['difficulty'].unique())
    print(features.head())


    print(all_df.head())

    all_df = all_df.reset_index(drop=True)

    X = all_df[keep_list].values

    ss = StandardScaler()
    X = ss.fit_transform(X)
    print(X)
    print(all_df.info())


        
    # print(get_trail_recommendations('The Whole Enchilada',X,n=5))
    print(get_trail_recommendations(4670265,X,n=5))


    def assign_features(filename):
        trail_id, max_grade = get_gpx_features(filename)
        all_df.loc[all_df['id'] == trail_id, 'max_grade'] = max_grade
    
    directory = "../data/GPX/all/"
    df_list = []
    for filename in os.listdir(directory):
        if filename.endswith(".gpx"):
            print("../data/all/"+filename)
            assign_features("../data/GPX/all/"+filename)
            continue
        else:
            continue
    # assign_features()

    print(all_df.describe())

    print(all_df.loc[all_df['id'] == 7029147])





    


    