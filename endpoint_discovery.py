# <---------------*** import functions & macro definitions ***----------------->
import json
from math import sin, cos, atan2, sqrt, pi
from datetime import datetime, date
from flask import Flask, request, jsonify

max_distance = 1.5  # 1.5km
max_dates = 120  # 4 months
max_restaurants = 10  # max number of restaurants in a list

# <-------------------------*** setup flask ***-------------------------------->

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False


def start_process(customer_lon, customer_lat):
    # <-------------------*** load restaurants.json file ***------------------->
    with open('srcs/restaurants.json', 'r') as f:
        data = json.load(f)

    restaurant_list = data['restaurants']

    # <--------------*** calculate customer & restaurant ***------------------->

    def degree_to_radians(degrees):
        return degrees * pi / 180

    def compute_haversine_dis(lon1, lat1, lon2, lat2):
        earth_radius_km = 6371

        dis_lat = degree_to_radians(lat2 - lat1)
        dis_lon = degree_to_radians(lon2 - lon1)

        lat1 = degree_to_radians(lat1)
        lat2 = degree_to_radians(lat2)

        a = sin(dis_lat / 2) * sin(dis_lat / 2) + sin(dis_lon / 2) * \
            sin(dis_lon / 2) * cos(lat1) * cos(lat2)

        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return earth_radius_km * c

    # add 'distance' key to each restaurant
    for restaurant in restaurant_list:
        restaurant_lon = restaurant['location'][0]
        restaurant_lat = restaurant['location'][1]
        haversine_distance = compute_haversine_dis(customer_lon, customer_lat,
		restaurant_lon, restaurant_lat)
        d = {'distance': haversine_distance}
        restaurant.update(d)

    # <--------------*** create sorted by distance list ***-------------------->

    # create a list with restaurants within max_distance(1.5km)
    r_within_max_dist_list = []

    for restaurant in restaurant_list:
        if restaurant['distance'] < max_distance:
            r_within_max_dist_list.append(restaurant)

    # create a sorted by distance list & remove 'distance key'
    sorted_by_distance_list = sorted(r_within_max_dist_list, key=lambda i: i['distance'])
    for restaurant in r_within_max_dist_list and sorted_by_distance_list:
        del restaurant['distance']

    # ----------*** create sorted by date & popularity list ***---------------->

    # create a list with restaurants within max_dates(4 months)
    r_within_max_date_list = []

    for restaurant in r_within_max_dist_list:
        launch_date = datetime.strptime(restaurant['launch_date'], '%Y-%m-%d')
        today_date = datetime.strptime(str(date.today()), '%Y-%m-%d')
        delta = today_date - launch_date
        if delta.days < max_dates:
            r_within_max_date_list.append(restaurant)

    # create two sorted list
    sorted_by_date_list = sorted(r_within_max_date_list, key=lambda r: \
		datetime.strptime(r['launch_date'], '%Y-%m-%d'), reverse=True)
    sorted_by_popularity_list = sorted(r_within_max_dist_list, key=lambda i: \
		i['popularity'], reverse=True)

    # <------------*** create final lists with max 10 elements ***------------->

    # prioritise 'online' when creating final 10
    def select_final_restaurants(sorted_list, result_list):
        for r in sorted_list:
            if r['online']:
                result_list.append(r)
            if len(result_list) == max_restaurants:
                break
        while len(result_list) < max_restaurants:
            for r in sorted_list:
                if not r['online']:
                    result_list.append(r)

    # *** create the final lists
    nearby_list = []
    popularity_list = []
    new_list = []

    if len(sorted_by_distance_list):
        select_final_restaurants(sorted_by_distance_list, nearby_list)
    if len(sorted_by_popularity_list):
        select_final_restaurants(sorted_by_popularity_list, popularity_list)
    if len(sorted_by_date_list):
        select_final_restaurants(sorted_by_date_list, new_list)

    # <----------------*** create final nested dictionary ***------------------>

    return_dict = {}
    restaurants_list = []

    if len(popularity_list):
        popular_dict = {"title": "Popular Restaurants", "restaurants": popularity_list}
        restaurants_list.append(popular_dict)

    if len(new_list):
        new_dict = {"title": "New Restaurants", "restaurants": new_list}
        restaurants_list.append(new_dict)

    if len(nearby_list):
        near_dict = {"title": "Nearby Restaurants", "restaurants": new_list}
        restaurants_list.append(near_dict)

    if len(restaurants_list):
        return_dict["sections"] = restaurants_list
    return jsonify(return_dict)


# <-------------------------*** setup flask endpoint ***----------------------->

@app.route('/', methods=['GET'])
def home():
    return '<h1> Please access endpoint \'/discovery\' for data request. </h1>'


@app.route('/discovery', methods=['GET'])
def discovery():
    if 'lon' in request.args and 'lat' in request.args:
        customer_lon = float(request.args['lon'])
        customer_lat = float(request.args['lat'])
        if not customer_lon or not customer_lat or customer_lon < -180 or \
			customer_lon > 180 or customer_lat < -90 or customer_lat > 90:
            return '<h1>ERROR: [lat] & [lon] are not in the correct range.</h1>'
        return start_process(customer_lon, customer_lat)
    else:
        return '<h1>ERROR: need to provide [lat] & [lon] fields.</h1>'


# <---------------------------*** start flask ***------------------------------>

app.run()
