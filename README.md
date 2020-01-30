[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
# Users Retrieval Application
An API that connects to an external API resource to retrieve some users in locations.


## Highlights
- Retrieve All Users.
- Retrieve A User by ID.
- Retrieve Users by city Location e.g. 'London'
- Retrieve Users by city Location within some given mileage e.g. 50 miles


## Implementation Plan 

This is a flask app with the following features:
- Flask Boiler plate (static files such as html, css and js).
- Retrieve users (by id, by city, by city within mileage range) from external endpoint.
- Documentation.
- Pytest (hopefully at some point).


### Quick Start

1. Clone the repo:
  ```
  $ git clone https://github.com/neguskay/lokasi-pengguna.git
  $ cd lokasi-pengguna
  ```

2. Initialize and activate a virtualenv:
  ```
  Can Use Either Conda or VeirtualEnv
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  __init__.py in src
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)



