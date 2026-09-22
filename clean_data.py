import pandas as pd 
import json 

with open ("asteroid_raw.json", "r") as f :
    data = json.load(f)
rows= [] 
for date, asteroids in data ["near_earth_objects"].items():
    for asteroid in asteroids :
        row = {
            "name" : asteroid["name"],
            "date" :date ,
            "diameter_min_m" : asteroid["estimated_diameter"]["meters"]["estimated_diameter_min"],
            "diameter_max_m": asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"],
            "is_hazardous" : asteroid["is_potentially_hazardous_asteroid"],
            "miss_distance_km": asteroid ["close_approach_data"][0]["miss_distance"]["kilometers"],
            "velocity_kph" : asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"],
        } 
        rows.append(row)
        df = pd.DataFrame(rows)

        df.to_csv("asteroid_clean.csv", index = False)
        print (df.head())
        print ("Total asteroids",len (df))

