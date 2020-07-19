# SWAPI_REST

(SWAPI is a wrapper for search people using [SWAPI API](https://swapi.dev/documentation#people))

## SYSTEM Requirements:

- `python 3.8`
- `pip 20.0.2`

## Instructions:

- To create new env => `python3 -m venv venv` Or using the system libs => `python3 -m venv venv --system-site-packages`
- To activate the currnt env => `source venv/bin/activate`
- To install the requirements => `pip3 install -r requirements.txt`
- Run the app `python3 run.py`
- Goto [`http://127.0.0.1:5000/api/characters/?name=Luke`](http://127.0.0.1:5000/api/characters/?name=Luke)
- To run the test `pytest -s` (inside the venv)
