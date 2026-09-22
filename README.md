# NASA Asteroid Hazard Analysis

A data analysis project examining whether NASA-classified "potentially hazardous" 
asteroids are actually larger than non-hazardous ones, built end-to-end in Python 
and presented through an interactive Flask dashboard.

## Live Demo

<img width="1350" height="640" alt="image" src="https://github.com/user-attachments/assets/220fb0b0-4f92-41db-9db2-323bc42de9b6" />
<img width="1341" height="630" alt="image" src="https://github.com/user-attachments/assets/700f4989-989a-4da6-8cc1-b540af4b0516" />


<img width="1354" height="630" alt="image" src="https://github.com/user-attachments/assets/bce07cd0-2785-4e7d-877c-c345ac70900b" />
<img width="1352" height="629" alt="image" src="https://github.com/user-attachments/assets/9b1053c6-5a18-4dcc-904c-beade29c0241" />



## The Question
NASA flags an asteroid as "potentially hazardous" based on its proximity to Earth 
and its estimated size. This project asks: **do hazardous asteroids actually tend 
to be measurably larger, or is that pattern too weak to trust in a small sample?**

## Approach
1. **Collect** — Pulled a week of near-Earth object data from NASA's NeoWs API
2. **Clean** — Flattened the nested JSON response into a structured table using pandas
3. **Analyze** — Ran a Welch's t-test comparing average diameter between hazardous 
   and non-hazardous asteroids
4. **Visualize** — Built an interactive dashboard (Flask + Chart.js) displaying the 
   comparison, statistical results, and full asteroid list

## Key Finding
Hazardous asteroids averaged **334.2m** in diameter vs. **174.9m** for non-hazardous 
ones — nearly double. However, the difference did **not reach statistical 
significance** (p = 0.071), likely due to the small sample size (only 4 hazardous 
asteroids in the one-week window analyzed). This highlights an important lesson: 
a visually striking difference in a small sample isn't automatically reliable 
evidence of a real pattern.

## Tech Stack
- **Python**: pandas, scipy, Flask
- **Frontend**: HTML, CSS, Chart.js
- **Data Source**: [NASA NeoWs API](https://api.nasa.gov/)

## Running Locally
```bash
git clone https://github.com/zanishcodes7/nasa-asteroid-hazard-analysis.git
cd nasa-asteroid-hazard-analysis
pip install -r requirements.txt

# Create a .env file with your own NASA API key:
# NASA_API_KEY=your_key_here

python fetch_data.py
python clean_data.py
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

## Project Structure
```
├── fetch_data.py      # Pulls raw data from NASA's API
├── clean_data.py       # Cleans/flattens JSON into a CSV
├── analyze.py           # Statistical analysis (t-test)
├── visualize.py         # Generates static comparison chart
├── app.py                # Flask dashboard
└── templates/
    └── index.html        # Dashboard UI
```
