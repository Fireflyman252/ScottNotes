#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 22:51:53 2021

@author: firefly
"""

import json 

class Note():
    
    done = False
    item = ""
    position = 0
    time = None
    tag = ""
    
    def __init__(self,done = False, item = "", position = 0, time = None, tag = "", foregroundColor = None, backgroundColor = None):
        self.done = done
        self.item = item
        self.position = position
        self.time = time
        self.tag = tag
    
    def toJSON(self):
        return json.dumps(self.toDict())
    
    def toDict(self):
        timestring = ""
        if(self.time != None):
            timestring = self.time.toString()
        return {'done': self.done, 'item': self.item , 'position': self.position, 'time': timestring, 'tag': self.tag}
    
    def fromDict(self, itemdict):
        self.done = itemdict['done']
        self.item = itemdict['item']
        self.position = itemdict['position']
        self.time = itemdict['time']
        if "tag" in itemdict:
            self.tag = itemdict['tag']