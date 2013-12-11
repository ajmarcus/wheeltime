#!/usr/local/bin/python

from flask import Flask, jsonify
import math
from itertools import count
app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/roll')
def roll():
	result = {
		'finserv':finserv.next(),
		'tech':tech.next()
		}
	return jsonify(result)


# From http://zacharydenton.com/generate-audio-with-python/
def sine_wave(frequency=440.0, framerate=44100, amplitude=0.5):
	'''
	Generate a sine wave at a given frequency of infinite length.
	'''
	period = int(framerate / frequency)
	if amplitude > 1.0: amplitude = 1.0
	if amplitude < 0.0: amplitude = 0.0
	lookup_table = [float(amplitude) * math.sin(2.0*math.pi*float(frequency)*(float(i%period)/float(framerate))) for i in xrange(period)]
	return (lookup_table[i%period] for i in count(0))

finserv = sine_wave(amplitude=0.6)
tech = sine_wave()

if __name__ == '__main__':
	app.run()
