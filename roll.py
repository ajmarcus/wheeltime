#!/usr/local/bin/python

import math, redis, time, json
from itertools import count

r = redis.StrictRedis(host='localhost', port=6379, db=0)

# App

# From http://zacharydenton.com/generate-audio-with-python/
def sine_wave(frequency=440.0, framerate=44100, amplitude=0.5):
  '''
  Generate a sine wave at a given frequency of infinite length.
  '''
  period = int(framerate / frequency)
  if amplitude > 1.0: amplitude = 1.0
  if amplitude < 0.0: amplitude = 0.0
  lookup_table = [float(amplitude) * math.sin(2.0*math.pi*float(frequency)*(float(i%period)/float(framerate))) for i in xrange(period)]
  return (lookup_table[i%period]+1 for i in count(0))

wagon = sine_wave(amplitude=0.6)
bus = sine_wave()
train = sine_wave(frequency=400.0)

now = int(time.time()) / 10

while True:
  time.sleep(10)
  now = now + 1
  r.lpush('roll', json.dumps({
    'time': now,
    'wagon': wagon.next(),
    'bus': bus.next(),
    'train': train.next()
  }))
  r.ltrim('roll', 0, 1000)