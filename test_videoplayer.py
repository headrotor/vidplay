#!/usr/bin/python

"""test_videoplayer: test vidplay class"""

import subprocess
import time
import sys

# local video player class, must be in same directory
import vidplay

usage = """usage: python test_videoplayer.py <arg>
where <arg> is:

1 -- play video 1
2 -- play video 2
s -- stop video
p -- pause video
t -- test if there is a video playing
x -- stop videoplayer and exit """

print usage
    
# make a vidplay object
vidplayer = vidplay.Vidplay()


done = False
while not done:
    #print repr(vidpipe.poll())
    user_in = raw_input()
    if user_in == 's':
        print "stopping"
        vidplayer.stop()
    elif user_in == 'p':
        print "pause/play"
        vidplayer.pause()
    elif user_in == 't':

        if vidplayer.is_playing():
            print "video playing"
        else:
            print "video stopped"

    elif user_in == '1':
        vidplayer.play(1)

    elif user_in == '2':
        vidplayer.play(2)

    elif user_in == 'x':
        vidplayer.stop()
        done = True

    else:
        print "unknown command '%s'" % user_in
        print usage
