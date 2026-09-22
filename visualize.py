import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("asteroid_clean.csv")
df["avg_diameter"] = (df["diameter_min_m"] + df["diameter_max_m"]) / 2

hazardous = df[df["is_hazardous"] == True]["avg_diameter"]
not_hazardous = df[df["is_hazardous"] == False]["avg_diameter"]

# Bar chart comparing average sizes
groups = ["Hazardous", "Not Hazardous"]
averages = [hazardous.mean(), not_hazardous.mean()]

plt.figure(figsize=(6, 5))
plt.bar(groups, averages, color=["#d62728", "#2ca02c"])
plt.ylabel("Average Diameter (meters)")
plt.title("Average Asteroid Size: Hazardous vs Non-Hazardous")

# Add the actual numbers on top of each bar so it's easy to read
for i, value in enumerate(averages):
    plt.text(i, value + 5, f"{value:.1f} m", ha="center")

plt.savefig("hazard_comparison.png")
plt.show()

print("Chart saved as hazard_comparison.png")