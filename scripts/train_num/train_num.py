#!/usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def readFile(filename):
    return file(filename, 'r').readlines()

if len(sys.argv) != 2:
    print 'Usage: num_trainer <list_path>'
    exit()

path = sys.argv[1]
lines = readFile(path)
for line in lines:
    print line
