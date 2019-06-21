import time
import pandas as pd
from config import api_key
import json
import requests 

csv_path = "output/miami_dade_schools.csv"
schools_df = pd.read_csv(csv_path)

schools_df.head()


url = 'http://www.mapquestapi.com/geocoding/v1/address?key='+api_key+'&location='

for index, row in schools_df.iterrows():
    new_url = url+row['address']
    print(new_url)
    response = requests.get(new_url)
    response_json = response.json()
    lat = response_json["results"][0]["locations"][0]["latLng"]['lat']
    lng = response_json["results"][0]["locations"][0]["latLng"]['lng']
    print(row["address"], lat, lng)

    int_number = float(lat)
    if (int_number > 0):
        str_lat = str(lat)+'N'
    else:
        int_number= -int_number
        str_lat = str(int_number)+'S'

    int_number = float(lng)
    if (int_number > 0):
        str_lng = str(lng)+'E'
    else:
        int_number= -int_number
        str_lng = str(int_number)+'W'
    print(lat,lng,str_lat, str_lng, index)
    schools_df.loc[index, "latitude"] = lat
    schools_df.loc[index, "longitude"] = lng
    schools_df.loc[index, "lat_dir"] = str_lat
    schools_df.loc[index, "lng_dir"] = str_lng
                                 
                             
schools_df.head()


schools_df.to_csv('output/dadeschools_lat_lng.csv')
print('done')



