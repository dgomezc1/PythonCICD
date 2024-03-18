# PythonCICD

**Install project dependecies**

`pip install -r requirements.txt`

**Run the prject**

`uvicorn functions.crud_function:app --host 0.0.0.0 --port 3006 --reload`

**Run the test coverage**

`pytest --cov-report term-missing --cov=app `

