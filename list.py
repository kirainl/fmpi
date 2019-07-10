#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

songs = ['first.mp3','fire.mp3', 'wn.mp3','firel.mp3','cron.mp3','anime1.mp3','anime2.mp3','anime3.mp3']
for song in songs:
   os.system('mpg123 -m -C -q -s /home/pi/music/'+song+' | sudo pifm - 106.3 44100')

print "finish"
