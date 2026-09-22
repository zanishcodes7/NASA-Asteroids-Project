from flask import Flask, render_template
import pandas as pd 
from scipy import stats
app = Flask(__name__) 
def get_data():
    df = pd.read_csv("asteroid_clean.csv")
    df["avg_diameter"] = (df["diameter_min_m"]+ df["diameter_max_m"])/2  
    hazardous  = df[df["is_hazardous"]== True]["avg_diameter"]
    not_hazardous = df [df["is_hazardous"]== False]["avg_diameter"]
    t_stat,p_value = stats.ttest_ind(hazardous,not_hazardous,equal_var=False)
    return{
         "total_count" : len(df),
         "hazardous_count" : len(hazardous),
         "not_hazardous_count" : len(not_hazardous),
         "hazardous_avg": round (hazardous.mean(),1),
         "not_hazardous_avg": round (not_hazardous.mean(),1) ,
         "t_stat": round(t_stat,3 ),
         "p_value": round(p_value,3 ),
         "significant": p_value < 0.05,
         "asteroids": df.sort_values("avg_diameter", ascending= False ).to_dict(orient="records")
    }
@app.route ("/")
def home():
    data = get_data()
    return render_template ("index.html", data= data)
if __name__ == "__main__":
    app.run (debug = True) 



