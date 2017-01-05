#! /usr/local/bin/python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def readFile(filename):
  return file(filename, 'r').readlines()

if len(sys.argv) != 2:
  print 'Usage: mistakes [today/yesterday/(number)/top]'
  exit()

cmd = sys.argv[1]
lines = readFile('~/.learnenglishthehardway/.mistakes')
for line in lines:
  print line
