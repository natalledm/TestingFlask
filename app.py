from flask import Flask, request
from flask_restful import Resource, Api
import json
import psycopg2

app = Flask(__name__)

api = Api(app)
conn = psycopg2.connect("dbname=stardew user=nat password=admin")


# Retrieving data from postgres and returning json with only Flask
@app.route('/names')
def get_names():
    cur = conn.cursor()
    cur.execute('select * from "VillagersGifts"."VillagersGifts";')
    # cur.fetchall()
    return "{ 'names': " + str(cur.fetchall()) + " }"

# Retrieving data from postgres using flask_restful
class AllVillagers(Resource):
    def get(self):
        cur = conn.cursor()
        cur.execute('select * from "VillagersGifts"."VillagersGifts";')
        return {'All villagers and gifts': cur.fetchall()}

class Names(Resource):
    def get(self):
        cur = conn.cursor()
        cur.execute('select "Name" from "VillagersGifts"."VillagersGifts";')
        return {'Names': cur.fetchall()}


api.add_resource(AllVillagers, '/')
api.add_resource(Names, '/onlynames')

if __name__ == '__main__':
    app.run(port='5003') # testing changing the port

# Using data from a simple json file
@app.route('/villagers')
def get_villagers():
    with open('villagers-gifts.json', 'r') as json_file:
        villagers_dict = json.load(json_file)

    villagers_list = villagers_dict['villagers']

    villagers_names = []
    for villager in villagers_list:
        villagers_names.append(villager['name'])

    return str(villagers_names)
