import pandas as pd

places = pd.read_csv('data/places_with_moments.csv')
places = places[~places['monday'].isnull()]
del places['Unnamed: 0']
del places['Unnamed: 0.1']

print(places.info())
places.to_csv('data/places_cleaned.csv')
