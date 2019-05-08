# Behavior Map Natal

<img src="https://github.com/mrmorais/behavior-map-natal/blob/master/img/natal_monday.gif?raw=true" width="400">

I created a interactive map (using pandas, python and folium libraries) on collected data from two resources of [Google Places API][places-api]. The resources are search nearby places and get popular times for those places. In short: more than 800 places were collected using 20km radius range, 20 categories and some max results limitations chosen by hand. These raw data of places is the `data/places.csv` dataset (it contains `place_name`, `place_id`, `lat`, `lng` and `type` columns).

The `read_places.py` script was used to read those `places.csv`'s places from the API. To do this, you only need a API Key ([see here how to get one][api-key]). This script uses the [Search][api-search] of the API.

Then you will need to populate these places with popular times or "moments" using another resource from Google Places. This resource is not available through regulas Places API and also is not free, but you make 5.000 calls with the allotted monthly budget. For this reason I'm not sharing the obtained dataset of places with popular times, it may go against the use terms of the services. So, I created the `get_places_popular_moments.py` to make these calls and generate a new dataset `data/places_with_moments.csv`.

...

[places-api]: https://developers.google.com/places/web-service/intro
[api-search]: https://developers.google.com/places/web-service/search
[api-key]: https://cloud.google.com/docs/authentication/api-keys
