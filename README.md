# Testing Flask and Data

This is just a simple API, done with Python and Flask, that retrieves data from Postgresql and a simple json file.

There are three ways in this app:

1. Retrieving data from postgres and returning json with only Flask:
    - Flask only return strings and texts, it's not completely RESTful. The way to turn around it and return a json was "to do it myself", adding string to each other so they can resemble a json response.
2. Retrieving data from postgres using flask_restful:
    - This is the way to a RESTful response using a full database. It's important for a big project with a big database.
3. Retrieving data from a simple json file using flask_restful:
    - If the API is a simple one, just a json file (or a sqlite one) is enough. 