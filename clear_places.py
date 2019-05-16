import pandas as pd

places = pd.read_csv('data/places_with_moments.csv', index_col=0)
places = places[~places['monday'].isnull()]

places = places.reset_index(drop=True)
places.to_csv('data/places_cleaned.csv', index=False)
