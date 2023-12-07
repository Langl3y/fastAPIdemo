<p align="center" width="100%">
    <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png">
    <p style="text-align: center;">
</p>

# A FastAPI demo 

<span style="color:red;font-weight:700;font-size:100px">
    Not tested on Windows.
</span>

## Requirements
- Python 3.10
- FastAPI 1.104.1
- MySQL >= 5.8
- Uvicorn 0.20.0
- SQLAlchemy 2.0.23
- pydantic 2.5.2

## Install Python modules

```shell
./init.sh
```

## Run server for testing

```shell
uvicorn main:app --reload    
```

## Run server (no reload)

```shell
uvicorn main:app
```

## Important Note:

This demo will not work if there is no schema for it to connect to. 
Please create a schema in mySQL first, then reconfigure URL_DATABASE so It matches your schema's name.

## APIs Documentation

See: host/docs in your browser for APIs documentation.