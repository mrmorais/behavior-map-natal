# Behavior Map Natal

[![](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TW67ytLbvg6WOGxVy8rPXpfNsie420pg)

![](https://cdn-images-1.medium.com/max/2560/1*rLbgkzYR8qw400AFqVMnHg.png)

I created a interactive map (using pandas, python and folium libraries) on collected data from two resources of [Google Places API][places-api]. The resources are search nearby places and get popular times for those places. In short: more than 800 places were collected using 20km radius range, 20 categories and some max results limitations chosen by hand. These raw data of places is the `data/places.csv` dataset (it contains `place_name`, `place_id`, `lat`, `lng` and `type` columns).

The `read_places.py` script was used to read those `places.csv`'s places from the API. To do this, you only need a API Key ([see here how to get one][api-key]). This script uses the [Search][api-search] of the API.

Then you will need to populate these places with popular times or "moments" using another resource from Google Places. This resource is not available through regulas Places API and also is not free, but you make 5.000 calls with the allotted monthly budget. For this reason I'm not sharing the obtained dataset of places with popular times, it may go against the use terms of the services. So, I created the `get_places_popular_moments.py` to make these calls and generate a new dataset `data/places_with_moments.csv`.

Now we have a bunch of places with the popular moments, just like we wanted. But, you will realise, that not every place has any values for popular moments (maybe neither Google has). This means that for our study, these places without "popular moments" data can be ignored, on that example from 800 only 300 has valid values. To use only the data we want let's clean up our dataset by running the `clear_places.py`. It will generate the final peace `data/places_cleaned.py`.

Ok! that's it. Now you can plot it all using the `creating_map_time.ipynb` notebook. Enjoy.

[places-api]: https://developers.google.com/places/web-service/intro
[api-search]: https://developers.google.com/places/web-service/search
[api-key]: https://cloud.google.com/docs/authentication/api-keys
