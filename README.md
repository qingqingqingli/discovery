# Discovery Endpoint Development
***This project is a completed BACKEND assignment for [Wolt Summer 2021 Internship](https://github.com/woltapp/summer2021-internship).***

## Backend assignment overview

The task is to create an **API endpoint** */discovery* that takes coordinates of the customer as an input and then **returns a page (JSON response)** containing *most popular, newest and nearby* restaurants (based on given coordinates).

More details please refer to the [detailed assignment](https://github.com/woltapp/summer2021-internship).

## My process

Before working on this assignment, I did not know how to work with `Python`, `Flask` and `JSON` for backend development. During the last 3 days, I started with understanding the problem, drawing down the process flow and tackling each technical element along the way. I really enjoyed the process to learn and develop something at the same time. 

## Disclaimer before testing

`Python` is required for this project. If you don't have it, please follow [this link](https://www.python.org/downloads/) to download it first. This demonstration is done on a Linux distribution (```Pop!_OS 20.04 LTS```).

## Step 1: Clone the project & run setup.sh script

The `setup.sh` script automates the process to install `pip`, `required Python packages` for this project, and the `python script` to start the endpoint.

```shell

cd Desktop && git clone https://github.com/qingqingqingli/discovery.git

cd discovery && ls

sh setup.sh

```

> Demo of starting the project

[![setup_1](https://github.com/qingqingqingli/discovery/blob/main/images/setup_1.png)](https://github.com/qingqingqingli/discovery)

> A Flask app will start running, providing the access to test '/discovery' endpoint

[![setup_2](https://github.com/qingqingqingli/discovery/blob/main/images/setup_2.png)](https://github.com/qingqingqingli/discovery)

## Step 2: Open browser and enter your requests

Location of a customer needs to be provided as **request parameters** *lat* (latitude) and *lon* (longitude), e.g. */discovery?lat=60.1709&lon=24.941*. Both parameters accept float values.

Some examples:
- [http://127.0.0.1:5000/](http://127.0.0.1:5000/). It will remind the user to access endpoint `/discovery` for data requests
- [http://127.0.0.1:5000/discovery?lon=24.9](http://127.0.0.1:5000/discovery?lon=24.9). `lat` is not provided, hence an error message will be shown. The same goes for `invalid data type or range`
- [http://127.0.0.1:5000/discovery?lat=60.1709&lon=24.941](http://127.0.0.1:5000/discovery?lat=60.1709&lon=24.941). It will return a JSON response, containing *most popular, newest and nearby* restaurants.

> Example of JSON response. There is an option to download the JSON file (left corner)

[![json_response](https://github.com/qingqingqingli/discovery/blob/main/images/json_response.png)](https://github.com/qingqingqingli/discovery)

## To do

Due to the time limit, I did not develop everything that I wanted. I intend to continue developing the following:

- [ ] Unit tests
- [ ] A Docker Container for easier testing
