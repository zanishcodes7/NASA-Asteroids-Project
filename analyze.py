import pandas as pd 
from scipy import stats 
df = pd.read_csv("asteroid_clean.csv")
df["avg_diameter"] = (df["diameter_min_m"]+ df["diameter_max_m"])/2  
hazardous  = df[df["is_hazardous"]== True]["avg_diameter"]
not_hazardous = df [df["is_hazardous"]== False]["avg_diameter"]

print ("Count of hazardous asteroids:", len(hazardous))
print ("Count of not_hazardous asteroids:", len(not_hazardous))
print ("Average size of the (hazardous elements): ",hazardous.mean())
print ("Average size of the (non_hazardous elements): ",not_hazardous.mean())
t_stat,p_value = stats.ttest_ind(hazardous,not_hazardous,equal_var=False)
print ("T_stats : ", t_stat)
print ("P_value: ", p_value)
if p_value < 0.05:
    print ("There is a significant difference in values ")
else:
    print  ("There is no significant difference in values ")

 
 


