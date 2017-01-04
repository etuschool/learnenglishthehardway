#! /usr/local/bin/python
#coding:utf-8

import sys
import requests
import subprocess

def requestWordDefination(word):
  url = "http://dict-co.iciba.com/api/dictionary.php"
  params = {'w': word, 'key': '6E5CF28FEBD10AAADAE0B6DB21579AB2', 'type': 'json'}
  r = requests.get(url, params = params)
  return r.json()

def playMp3(audioFile):
  # only work on Mac
  code = subprocess.call(["afplay", audioFile])
  return code

if len(sys.argv) != 2:
  print 'Usage: medict <word>'
  exit()

# Get word defination
# Ref: http://dict-co.iciba.com/api/dictionary.php?w=go&key=6E5CF28FEBD10AAADAE0B6DB21579AB2&type=json
word = sys.argv[1]
content = requestWordDefination(word)
firstSymbol = content['symbols'][0]
phonicMp3 = firstSymbol['ph_am_mp3'] or firstSymbol['ph_en_mp3'] or firstSymbol['ph_tts_mp3']
parts = firstSymbol['parts']
defination = '\n'.join([ p['part']+','.join(p['means'])+';' for p in parts ])

print word
print defination

# Download phonic mp3
mp3Body = requests.get(phonicMp3)
with open("/tmp/word.mp3", "wb") as f:
    f.write(mp3Body.content)
    playMp3('/tmp/word.mp3')
