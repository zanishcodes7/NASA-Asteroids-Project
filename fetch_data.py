import requests 
import json 
import os 
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")
URL = "https://api.nasa.gov/neo/rest/v1/feed"
params =  {
    "start_date" : "2026-09-01",
    "end_date" : "2026-09-07",
    "api_key" : API_KEY
}
response =  requests.get(URL, params = params)
data =  response.json ()

with open ("asteroid_raw.json", "w")  as f :
    json.dump(data ,f ,indent =2 )
    print (data)

