import gpxpy
import gpxpy.gpx
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

from math import sin, cos, sqrt, atan2, radians # get_distance

#code to get distance between two lat/long
# approximate radius of earth in km

def get_distance(la1, lo1, la2, lo2):
    R = 6373.0

    lat1 = radians(la1)
    lon1 = radians(lo1)
    lat2 = radians(la2)
    lon2 = radians(lo2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def get_gpx_features(filename):

    # Parsing an existing file:
    # -------------------------

    # gpx_file = open('../data/GPX/bangtail-divide-imba-epic.gpx', 'r')
    # gpx_file = open('../data/GPX/bangtail-divide-imba-epic.gpx', 'r')
    # gpx_file = open('../data/GPX/raggeds-shuttle.gpx', 'r')
    gpx_file = open(filename, 'r')
    # gpx_file = open('../data/GPX/the-whole-enchilada.gpx', 'r')
    raw_text = gpx_file.read()
    regex_id = re.search(r'https://www.mtbproject.com/trail/(\d+)',raw_text)
    trail_id = int(regex_id.group(1))
    # print(trail_id)

    gpx_file.close()
    # print(raw_text)
    # gpx_file = open('../data/GPX/bangtail-divide-imba-epic.gpx', 'r')
    gpx_file = open(filename, 'r')
    gpx = gpxpy.parse(gpx_file)

    gpx_file.close()

    data = []
    counter = 1
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                # print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))
                if counter == 1:
                    data.append([counter, point.latitude, point.longitude, point.elevation, 0, 0])
                else:
                    distance = get_distance(la1, lo1, point.latitude, point.longitude)
                    try:
                        grade = (((point.elevation - elev1)/1000) / distance)*100
                    except ZeroDivisionError:
                        grade = 0
                    data.append([counter, point.latitude, point.longitude, point.elevation, distance, grade])

                counter += 1
                la1 = point.latitude
                lo1 = point.longitude
                elev1 = point.elevation


    df = pd.DataFrame(data, columns = ['Track', 'Latitude', 'Longitude', 'Elevation', 'Distance', 'Grade'])
    df['Elevation_Ft'] = df['Elevation']*3.2808
    # df['Elevation_Ft'].plot()
    # plt.show()

    df['Dist_Miles'] = df['Distance'] *0.62137119223
    df['Elev_Rolling'] = df['Elevation_Ft'].rolling(60).mean()
    df['Elev_Prev'] = df['Elev_Rolling'].shift(1)#fillna(0)
    # df['Elev_Prev'] = df['Elevation_Ft'].shift(1).fillna(0)
    df['Elev_Diff'] = df['Elev_Rolling'] - df['Elev_Prev']
    # df['Elev_Diff'] = df['Elevation_Ft'] - df['Elev_Prev']
    df.iloc[0, df.columns.get_loc('Elev_Diff')] = 0
    # df['Elev_Rolling'] = df['Elev_Diff'].rolling(40).mean()

    # print(df.head())
    # df['Descent'] 
    max_elev = df['Elevation_Ft'].max()
    sum_dist = df['Dist_Miles'].sum()
    df['Elev_Diff'].plot()
    # plt.show()

    avg_dist = df['Dist_Miles'].mean()

    min_dist = df['Dist_Miles'].min()
    over_thresh = df['Dist_Miles']>.015
    positive = df['Grade']>0
    avg_distance = df['Dist_Miles'][over_thresh]
    max_dist = df['Dist_Miles'].max()
    max_grade = round(df['Grade'][over_thresh].max())
    avg_grade = df['Grade'][positive].mean()
    avg_dist_mean = avg_distance.mean()
    # df.to_csv('inspect.csv')
    # print(df.head())
    # print(df.tail())
    # print(gpx.tracks)
    # print(f'Max Elevation: {round(max_elev)}')
    # print(f'Total Distance: {round(sum_dist,1)}')
    # print(f'Min Distance: {round(min_dist)}')
    # print(f'Max Distance: {round(max_dist)}')
    # print(f'Avg Distance: {round(avg_dist_mean)}')
    # print(f'Max Grade: {round(max_grade)}')
    # print(f'Average Grade: {round(avg_grade)}')

    # print(avg_distance.head())
    return trail_id, max_grade

# print(get_gpx_features())
