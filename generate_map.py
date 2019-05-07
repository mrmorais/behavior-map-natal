import folium
from folium.plugins import HeatMap
import pandas as pd
import json
from math import ceil

WEEK_DAY = 'monday'

# morning (6, 7, 8, 9, 10, 11)
# afternoon (12, 13, 14, 15, 16, 17)
# evening (18, 19, 20, 21)
# night (22, 23, 0, 1, 2, 3, 4, 5)
PERIOD = 'night'

def place_to_hints(place):
    moments = json.loads(place[WEEK_DAY])
    hints = 0
    if PERIOD == 'morning':
        hints = sum(moments[6:12])
    elif PERIOD == 'afternoon':
        hints = sum(moments[12:18])
    elif PERIOD == 'evening':
        hints = sum(moments[18:22])
    else:
        hints = moments[23] + sum(moments[0:6])
    return ceil(hints/40)

def place_hints_per_hour(place, hour):
    moments = json.loads(place[WEEK_DAY])
    hints = moments[hour]
    return ceil(hints/40)

natal = folium.Map(location=[-5.8313086,-35.2047059], zoom_start=13)

places = pd.read_csv('data/places_cleaned.csv')

heat_dots = []

for index, row in places.iterrows():
    place_dots = place_hints_per_hour(row, 7) * [[row.lat, row.lng]]
    heat_dots += place_dots
    # folium.CircleMarker([row.lat, row.lng], popup=row.place_name, radius=2).add_to(natal)

HeatMap(heat_dots).add_to(natal)

natal.save('natal.html')
