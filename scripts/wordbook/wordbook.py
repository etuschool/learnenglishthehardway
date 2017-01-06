#!/usr/bin/env python
# coding:utf-8

import pysrt
import os
import datetime
import sys
import subprocess
import re

reload(sys)
sys.setdefaultencoding('utf-8')


# duplicate func compare to medict.py, need refactoring
def playWord(word):
    path = os.path.expanduser(
        "~") + '/.learnenglishthehardway/word_mp3/' + word + '.mp3'
    if os.path.isfile(path):
        subprocess.call(["afplay", path])
    else:
        print 'No word mp3 found.'


def getWordbookPath(_date):
    dateStr = _date.strftime('%Y_%m_%d')
    return os.path.expanduser("~") + '/.learnenglishthehardway/wordbook/' + dateStr + '.txt'

if len(sys.argv) != 3:
    print 'Usage: wordbook today play'
    exit()

date = sys.argv[1]
action = sys.argv[2]

if date == 'today' and action == 'play':
    path = getWordbookPath(datetime.date.today())
    f = open(path)
    for wordDef in f.read().split('\n\n'):

        print wordDef
        print '\n'

        parts = wordDef.split('\n')
        word = parts[0]
        defination = re.compile(r'[a-zA-Z.&]*').sub("", '\n'.join(parts[1:]))

        playWord(word)
        subprocess.call(["say", defination])

    f.close()
