#!/usr/bin/env python
# coding:utf-8

import pysrt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) != 2:
    print 'Usage: srt2txt <srt_path>'
    exit()

srtName = sys.argv[1]
subs = pysrt.open(srtName)

f = open(srtName.replace('.srt', '.txt'), "w")
for i in range(len(subs)):
    f.write('[{}] {}\n\n'.format(i, subs[i].text.replace('\n', ' ')))
f.close()
