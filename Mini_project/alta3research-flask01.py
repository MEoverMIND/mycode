#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   A simple Flask server. This server has the following endpoints:
   
   /success/<name> - responds with 200 + 'Welcome {name}'
   
   /
   /start          - Both endpoints respond with 200 + postmaker.html (template)
   
   /login          - a POST will have the form read for 'nm'
                   - a GET will be scanned for the query param ?nm=some_value"""

# python3 -m pip install flask
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask_restful import Resource, Api

app = Flask("AnimeAPI")
api = Api(app)

animes = {
        'anime1': {'title': 'Naruto'},
        'anime2': {'title': 'Bleach'},
        'anime3': {'title': 'HunterXHunter'}
    }
#this extends from flask restful module
class Anime(Resource):
    def get(self, anime_id):
        if anime_id == "all":
            return animes
        return animes[anime_id]


api.add_resource(Anime, '/animes/<anime_id>')


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

