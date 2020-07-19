# SWAPI_REST

(SWAPI is a wrapper for search people using [SWAPI API](https://swapi.dev/documentation#people))

## SYSTEM Requirements:

- `python 3.8`
- `pip 20.0.2`

## Instructions:

### Local run:

- To create new env => `python3 -m venv venv` Or using the system libs => `python3 -m venv venv --system-site-packages`
- To activate the currnt env => `source venv/bin/activate`
- To install the requirements => `pip3 install -r requirements.txt`
- Run the app `python3 run.py`
- Goto [`http://127.0.0.1:5000/api/characters/?name=Luke`](http://127.0.0.1:5000/api/characters/?name=Luke)
- To run the test `pytest -s` (inside the venv)

### Docker run:

- Build the image `docker build . --tag swapi_api`
- Run the image `docker run --name swapi_rest_web -p 5000:5000 swapi_api`
- Running the test
  1. Run to attach your terminal to the image `docker exec -it swapi_rest_web /bin/bash`
  2. Run the test `pytest -s`

### Docker(compose) run:

- Simply run `docker-compose up`
- Running the test
  1. Run to attach your terminal to the image `docker exec -it swapi_rest_web /bin/bash`
  2. Run the test `pytest -s`
