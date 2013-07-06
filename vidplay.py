#!/usr/bin/python

"""Vidplay: python wrapper for omxplayer on raspi
    By Jonathan Foote <jtf at rotormind.com> 7/13"""

import subprocess
import time
import sys

class Vidplay(object):
    """wrapper for omxplayer on raspi"""

    def __init__(self):
        self.videoplayer = 'omxplayer'
        """ paths to video files"""
        self.vidfiles = ['heman.mp4',
                         'Page_1_3.mp4']
        self.vidpipe = None

    def stop(self):
        """"Stop whatever video is currently playing"""
        if self.vidpipe is not None: 
            self.send_cmd('q')
            #self.vidpipe.terminate()
            self.vidpipe = None

    def pause(self):
        """"pause/restart whatever video is currently playing"""
        self.send_cmd('p')

    def play(self,vn):
        """ play the video file whose index is vn"""
        if self.vidpipe is not None:
            self.stop()
        self.commands = [self.videoplayer]
        vn -= 1 # start from 1
        if vn > len(self.vidfiles):
            print "no such video file"
            return

        vidfile = self.vidfiles[vn]
        try:
            with open(vidfile): 
                pass
        except IOError:
            print "Can't find file " + vidfile
            return

        self.commands.append(vidfile)
        #print repr(self.commands)
        self.vidpipe = subprocess.Popen(self.commands,
                           stdin = subprocess.PIPE, 
                           stdout = subprocess.PIPE)

    def is_playing(self):
        """ test if player process exists,
        does not know if paused (returns True)"""
        if self.vidpipe is None:
            return False
        else:
            if self.vidpipe.poll() == 0:
                self.vidpipe = None
                return False
        return True

    def send_cmd(self,cmd):
        """ send a command to the stdin of video player.
        check process exists and is still playing"""
        if self.vidpipe is None:
            print "no video obect"
            return
        if self.vidpipe.poll() == 0:
            self.vidpipe = None
            print "video object finished"
            return
        #print "send command " + cmd
        self.vidpipe.stdin.write(cmd)

if __name__ == '__main__':

    print """usage: python vidplay.py <arg>
where <arg> is:

1 -- play video 1
2 -- play video 2
s -- stop video
p -- pause video
t -- test if there is a video playing
x -- stop videoplayer and exit """

    
    """ make a vidplay object """
    vidplayer = Vidplay()

    
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
