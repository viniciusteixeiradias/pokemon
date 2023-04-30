# Purpose of this API

This API was developed in order to improve my knowledge in python and also to understand how FastApi, sqlachemy and alembic libs/frameworks work.

## What I used in this api

- [python 3.10.11](https://www.python.org/downloads/release/python-31011/)
- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)
- [requests](https://pypi.org/project/requests/)
- [sqlalchemy](https://www.sqlalchemy.org/)
- [alembic](https://alembic.sqlalchemy.org/en/latest/)
- [sqlite](https://pysqlite.readthedocs.io/en/latest/sqlite3.html)

## Summary of some of the tools used

- **Fastapi** is a fast (high-performance) framework for creating APIs with Python 3.7+
<br>
- **Uvicorn** is an **ASGI** web server implementation for Python.
  - **ASGI** ([Asynchronous Server Gateway Interface](https://asgi.readthedocs.io/en/latest/introduction.html)) is a specification for asynchronous web interfaces in Python to "handle multiple requests concurrently and more efficiently".

  - **WSGI** ([Web Server Gateway Interface](https://wsgi.readthedocs.io/en/latest/learn.html)) is a specification for synchronous web server interfaces in Python. WSGI allowed different web servers and application frameworks to work together in an easier and more standardized way.

  - **Difference between ASGI and WSGI**
    The main difference between ASGI and WSGI is that ASGI is capable of handling asynchronous requests whereas WSGI is limited to handling synchronous requests only. This means that ASGI is more efficient for handling web applications that require multiple tasks to run at the same time, such as real-time chat applications or streaming media, websocket, while WSGI is better suited for more traditional web applications that handle individual requests synchronously.
<br>
- **SQLAlchemy** is the Python SQL toolkit and **Object Relational Mapper** that gives application developers the full power and flexibility of SQL.
  - **ORM** (Object Relational Mapper) is a piece of software designed to translate between the data representations used by databases and those used in object-oriented programming.
<br>
- **Alembic** is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python.

## Setps to run the app

- Install [pyenv](https://github.com/pyenv/pyenv#homebrew-in-macos), after installation:

    ```bash
    pyenv install <python_version> # example pyenv install 3.10.11
    pyenv global <python_version> # example pyenv global 3.10.11
    ```

- Install [pipenv](https://pipenv.pypa.io/en/latest/installation/#installing-pipenv), after installation:

    ```bash
    pipenv -h # see the commands
    ```

    Create new pipenv project:

    ```bash
    pipenv --python <python_version> # example pipenv --python 3.10.11
    ```

    Install dependencies:

    ```bash
    cd api/
    pipenv shell
    pipenv install
    ```

    Run API:

    ```bash
    uvicorn src.main:app
    ```
