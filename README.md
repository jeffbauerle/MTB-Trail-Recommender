# Mountain Biking (MTB) Trail Recommender: 
## Find Your New Favorite Trail

## Motivation and Background

I like to mountain bike. I enjoy looking at the "Top Rides" section of MTB Project's website to see what the most highly rated trails are, see if there's any new ones on the list, and target them for trips. Outside of that, I don't have a good process for finding new mountain biking trails. Therefore, the goal of this project is to come up with a better process for finding new MTB trails, based on trails that you like.

![alt text](https://raw.githubusercontent.com/jeffbauerle/MTB-Trail-EDA/master/images/top_rated.png)

## What is a content-based recommender?

Recommends content based on other content you like  by evaluating the similarity of the content's attributes.


## Data

![alt text](https://holimont.com/wp-content/uploads/2020/03/mtb_project.png)


"MTB Project provides an API for developers to access it's data. MTB Project provides a simple API with access to certain limited data. All of the data returned by the API is already available on publicly available pages on the MTB Project site. Returned data is json."

[MTB Project Data API](https://www.mtbproject.com/data)

Method: getTrails

<img src="https://raw.githubusercontent.com/jeffbauerle/MTB-Trail-EDA/master/images/raw_data_example.png">

|#  | column   | Non-null count  | DType  | 
|---|---|---|---|
| 0  | id  |  1200 non-null | int64  |
|  1 | name  | 1200 non-null  |  object |
|  2 | type  |  1200 non-null | object  |
|  3 | ***summary***  |  1200 non-null | object  |
|  4 | ***difficulty***  | 1200 non-null  | object  |
|  5 | ***stars***  | 1200 non-null  | float64  |
|   6| starVotes  |  1200 non-null | int64  |
|   7| location  | 1200 non-null  | object  |
|   8| url  | 1200 non-null  | object  |
|   9|  imgSqSmall | 1200 non-null  | object  |
|   10| imgSmall  | 1200 non-null  | object  |
|   11| imgSmallMed  | 1200 non-null  | object  |
|   12| imgMedium  | 1200 non-null  | object  |
|   13| ***length***  | 1200 non-null  | float64  |
|   14| ***ascent***  | 1200 non-null  | int64  |
|   15| descent  | 1200 non-null  | int64  |
|   16| high  | 1200 non-null  | int64  |
|   17| low  |  1200 non-null | int64  |
|   18| ***longitude***  | 1200 non-null  | float64  |
|   19| ***latitude***  | 1200 non-null  | float64  |
|   20| conditionStatus  | 1200 non-null  | object  |
|   21| conditionDetails  | 868 non-null  | object  |
|   22| conditionDate  | 1200 non-null  | object  |



Regions considered: Denver, Crested Butte, Moab, Park City, Marin County, Sedona

I pulled trails within 60 miles of the epicenter of each region (googled location latitude/longitude) with a max result of 200 trails per query.

Selected locations from this Singletracks.com list, plus local (Denver) and alleged birthplace of MTB: Marin County; contested with Crested Butte.

[The Top 10 Best Mountain Bike Destinations in the USA](https://www.singletracks.com/mtb-trails/the-top-10-best-mountain-bike-destinations-in-the-usa/)

### Data Workflow

I started with data from MTBProject’s API, associated the region from where I pulled it, scraped GPS data for each trail, and from it engineed the features max grade, climb then descend, and return to starting elevation.

## Exploratory Data Analysis

<img src="https://github.com/jeffbauerle/MTB-Trail-Recommender/blob/master/images/MTB%20Trail%20Recommender%20Presentation%20(3).png">
<img src="https://github.com/jeffbauerle/MTB-Trail-Recommender/blob/master/images/MTB%20Trail%20Recommender%20Presentation%20(4).png">
<img src="https://github.com/jeffbauerle/MTB-Trail-Recommender/blob/master/images/MTB%20Trail%20Recommender%20Presentation%20(5).png">
<img src="https://github.com/jeffbauerle/MTB-Trail-Recommender/blob/master/images/MTB%20Trail%20Recommender%20Presentation%20(6).png">
<img src="https://github.com/jeffbauerle/MTB-Trail-Recommender/blob/master/images/MTB%20Trail%20Recommender%20Presentation%20(7).png">
<img src="https://github.com/jeffbauerle/MTB-Trail-Recommender/blob/master/images/MTB%20Trail%20Recommender%20Presentation%20(8).png">
<img src="https://github.com/jeffbauerle/MTB-Trail-Recommender/blob/master/images/MTB%20Trail%20Recommender%20Presentation%20(9).png">
<img src="https://github.com/jeffbauerle/MTB-Trail-Recommender/blob/master/images/MTB%20Trail%20Recommender%20Presentation%20(10).png">
<img src="https://github.com/jeffbauerle/MTB-Trail-Recommender/blob/master/images/MTB%20Trail%20Recommender%20Presentation%20(11).png">
<img src="https://github.com/jeffbauerle/MTB-Trail-Recommender/blob/master/images/MTB%20Trail%20Recommender%20Presentation%20(12).png">
<img src="https://github.com/jeffbauerle/MTB-Trail-Recommender/blob/master/images/MTB%20Trail%20Recommender%20Presentation%20(13).png">
