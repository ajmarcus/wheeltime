#!/usr/local/bin/python

import redis, simplejson as json
from flask import Flask, jsonify, render_template
app = Flask(__name__)
app.config.from_object('config')

r = redis.StrictRedis(host='localhost', port=6379, db=0)


# Routes

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/start')
def start():
  return jsonify(results=[ json.loads(item) for item in r.lrange('roll', 0, 200) ])

@app.route('/roll')
def roll():
  return jsonify(results=json.loads(r.lindex('roll', 0)))

if __name__ == '__main__':
  app.run()
