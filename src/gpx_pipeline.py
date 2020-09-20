import json
import pandas as pd
import numpy as np
from pandas import json_normalize
from PIL import Image
import scipy.stats as stats
import time
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from random import random


def load_trail_df_from_file(filename, location_name):
    with open(filename) as data_file:
        data = json.load(data_file)
    data_trails = data['trails']
    data_df = json_normalize(data_trails)
    data_df["location"] = location_name
    return data_df

def get_gpx(link):
        # ds = DirectoryAssistor()
        driver = webdriver.Chrome()
        driver.get(link)

        # driver.get('https://www.mtbproject.com/trail/4670265/')
        time.sleep(random()*3+2)
        if len(driver.find_elements_by_xpath('//*[@id="user"]/a'))==0:
            driver.quit()
        driver.find_element_by_xpath('//*[@id="user"]/a').click()
        time.sleep(1)
        elem = driver.find_element_by_xpath('//input[@placeholder="Log in with email"]')
        elem.click()
        elem.clear()
        elem.send_keys("jeffbauerle@gmail.com")
        pw = driver.find_element_by_xpath('//input[@placeholder="Password"]')
        pw.click()
        pw.clear()
        pw.send_keys("1L0v3mtb!")
        pw.send_keys(Keys.RETURN)
        time.sleep(1)
        if len(driver.find_elements_by_xpath('//*[@id="toolbox"]/a[3]'))==0:
            dl_alt = driver.find_element_by_xpath('//*[@id="segment-page"]/div[2]/div/div[2]/a[1]').click()
        else:
            dl = driver.find_element_by_xpath('//*[@id="toolbox"]/a[3]').click() 
        time.sleep(1)
        driver.quit()



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


    cb_ids = list(park_city_df['id'])
    cb_two_index = cb_ids.index(7039037)
    cb_starttwo = cb_ids[cb_two_index:]
    del cb_starttwo[0]
    print(cb_starttwo)
    mc_ids = list(marin_county_df['id'])
    den_ids = list(denver_df['id'])
    pc_ids = list(park_city_df['id'])
    sed_ids = list(sedona_df['id'])
    moab_ids = list(moab_df['id'])

    for val in cb_starttwo:
        # print(f'https://www.mtbproject.com/trail/{val}')
        index = cb_starttwo.index(val)
        print('**********************************************')
        print(cb_starttwo[index:])
        domain = 'https://www.mtbproject.com/trail/'
        link = domain+str(val)
        get_gpx(link)

    
    
    # lst = ['338027']

    # get_docs(lst)








    


