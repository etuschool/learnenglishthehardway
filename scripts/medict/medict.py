#!/usr/bin/env python
# coding:utf-8

import os
import sys
import datetime
import requests
import subprocess

reload(sys)
sys.setdefaultencoding('utf-8')


def requestWordDefination(word):
    url = "http://dict-co.iciba.com/api/dictionary.php"
    params = {
        'w': word, 'key': '6E5CF28FEBD10AAADAE0B6DB21579AB2', 'type': 'json'}
    r = requests.get(url, params=params)
    return r.json()


def downloadPhonicMp3(word, audioUrl):
    # Download phonic mp3
    path = ensurePath('~/.learnenglishthehardway/word_mp3/' + word + '.mp3')
    if os.path.isfile(path):
        return

    mp3Body = requests.get(audioUrl)
    with open(path, "wb") as f:
        f.write(mp3Body.content)


def playWord(word):
    # only work on Mac
    path = ensurePath('~/.learnenglishthehardway/word_mp3/' + word + '.mp3')
    if os.path.isfile(path):
        subprocess.call(["afplay", path])
    else:
        print 'No word mp3 found.'


def ensurePath(f):
    home = os.path.expanduser("~")
    absolutePath = f.replace('~', home)

    d = os.path.dirname(absolutePath)
    if not os.path.exists(d):
        os.makedirs(d)

    return absolutePath


def saveHistory(word):
    path = ensurePath('~/.learnenglishthehardway/history.txt')

    with open(path, "a") as f:
        f.write(word + '\n')


def saveDailyWordDefs(word, defination):
    dateStr = datetime.date.today().strftime('%Y_%m_%d')
    path = ensurePath('~/.learnenglishthehardway/wordbook/' + dateStr + '.txt')

    with open(path, "a") as f:
        f.write(word + '\n' + defination + '\n\n')

if len(sys.argv) != 2:
    print 'Usage: medict <word>'
    exit()

# Get word defination
# Ref:
# http://dict-co.iciba.com/api/dictionary.php?w=go&key=6E5CF28FEBD10AAADAE0B6DB21579AB2&type=json
word = sys.argv[1]

content = requestWordDefination(word)

phonicMp3 = None
symbolStrList = []

for symbol in content['symbols']:
    phonic = symbol['ph_am'] or symbol['ph_en'] or symbol['ph_other']
    phonicMp3 = phonicMp3 or symbol['ph_am_mp3'] or symbol[
        'ph_en_mp3'] or symbol['ph_tts_mp3']
    parts = symbol['parts']
    symbolStr = '[' + phonic + ']\n' + '\n'.join(
        [p['part'] + ','.join(p['means']) + ';' for p in parts])
    symbolStrList.append(symbolStr)

defination = '\n---\n'.join(symbolStrList)

print word
print defination

saveHistory(word)
saveDailyWordDefs(word, defination)

downloadPhonicMp3(word, phonicMp3)
playWord(word)
