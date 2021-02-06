# Discovery Endpoint Development
***This project develops an API endpoint based on restaurant data.***

## Overview

The **API endpoint** `/discovery` takes coordinates of the customer as an input, and **returns a page (JSON response)** containing *most popular, newest and nearby* restaurants (based on given coordinates).

> Restaurant data example

```json
{
   "blurhash":"UAPp-JsCNbr[UQagn*V^p-bYjIjtL?kSo]bG",
   "location":[
      24.933257,
      60.171263
   ],
   "name":"Charming Cherry House",
   "online": true,
   "launch_date":"2020-09-20",
   "popularity":0.665082352909038
}
```

**Fields**:

- `blurhash`: image representation (type: string)
- `location`: Restaurant's location as latitude and longitude coordinates. First element in the list is the longitude (type: a list containing two decimal elements)
- name: The name of the restaurant (type: string)
- `launch_date`: the date when the restaurant was added to Wolt app (type: string, ISO 8601 date)
- `online`: if true, the restaurant is accepting orders. If false, the restaurant is closed (type: boolean)
- `popularity`: the higher the number, the more popular the restaurant is in Wolt app (type: a float between 0-1, where 1 is the - most popular restaurant)

**List requirements**:

- For each restaurants-list you need to add `maximum 10` restaurant objects.
- All restaurants returned by the endpoint must be `closer than 1.5 kilometers` from given coordinates.
- `Open restaurants` (online=true) are more important than closed ones.

**Sorting rules for each list**:

- `“Popular Restaurants”`: highest popularity value first (descending order)
- `“New Restaurants”`: Newest launch_date first (descending). This list has also a special rule: launch_date must be no older than 4 months.
- `“Nearby Restaurants”`: Closest to the given location first (ascending).


## How to test

- Step 1: The `setup.sh` script automates the process to install `pip`, `required Python packages` for this project, and the `python script` to start the endpoint.

> Run the following codes:

```shell

cd Desktop && git clone https://github.com/qingqingqingli/discovery.git

cd discovery && ls

sh setup.sh

```

> A Flask app will start running, providing the access to test '/discovery' endpoint

[![setup_2](https://github.com/qingqingqingli/readme_images/blob/master/discovery_setup_2.png)](https://github.com/qingqingqingli/discovery)

- Step 2: Open browser and enter your requests.

Location of a customer needs to be provided as **request parameters** *lat* (latitude) and *lon* (longitude), e.g. */discovery?lat=60.1709&lon=24.941*. Both parameters accept float values.

**Some example requests**:
- [http://127.0.0.1:5000/](http://127.0.0.1:5000/). It will remind the user to access endpoint `/discovery` for data requests
- [http://127.0.0.1:5000/discovery?lon=24.9](http://127.0.0.1:5000/discovery?lon=24.9). `lat` is not provided, hence an error message will be shown. The same goes for `invalid data type or range`
- [http://127.0.0.1:5000/discovery?lat=60.1709&lon=24.941](http://127.0.0.1:5000/discovery?lat=60.1709&lon=24.941). It will return a JSON response, containing *most popular, newest and nearby* restaurants.

> Example of JSON response. There is an option to download the JSON file (left corner)

[![json_response](https://github.com/qingqingqingli/readme_images/blob/master/discovery_json.png)](https://github.com/qingqingqingli/discovery)
