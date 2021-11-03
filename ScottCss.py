#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 06:39:37 2021

@author: firefly
"""
from PyQt5 import QtGui
from PyQt5.QtGui import QColor


class ScottCss():
    
    def loadCssFromFile(filename):
        
        rv = {}
        out = []
        header = True
        reading = True
        headString = ""
        bodyString = ""
        with open (filename, "r") as file:

            # Read list of lines
            headbuffer = ""
            bodybuffer = ""
            out = [] # list to save lines
            while reading:
                # Read next line
                line = file.readline()
                if header:
                    headbuffer = headbuffer + line
                    if line.find("{") != -1:
                        pos = headbuffer.find("{")
                        headString = headbuffer[:pos].strip()
                        #print("head", headString)
                        header = False
                        bodybuffer = headbuffer[pos+1:]
                else:
                    bodybuffer = bodybuffer + line
                    if line.find("}") != -1:
                        pos = bodybuffer.find("}")
                        bodystring = bodybuffer[:pos].strip()
                        #print(bodystring)
                        header = True
                        headbuffer = ""
                        bodyarray = bodystring.split(";")
                        dict = {}
                        for i in bodyarray:
                            colonarray = i.split(":")
                            if(len(colonarray) > 1):
                                dict[colonarray[0].strip()] = colonarray[1].strip()
                        rv[headString] = dict
                        #print(bodyarray)
                        
                # If line is blank, then you struck the EOF
                if not line :
                    reading = False;
                
                #print("rv")
                #print(rv)
             
        #print(rv)
        return rv

    def value(css, dictname, key):
        rv = None
        if(dictname in css):
            if(key in css[dictname]):
                rv = css[dictname][key]
        return rv            

    def convertToRGB(inputstring):
        return QtGui.QColor(int(inputstring[1:3],16),int(inputstring[3:5],16),int(inputstring[5:],16))
    
    def writeCssToFile(filename, css):
        with open (filename, "w") as file:
            for key in css:
                file.write(key + " {\n")
                for item in css[key]:
                    file.write("\t" + item + " : " + css[key][item] + ";\n")
                file.write("}\n\n")

def main():
    ScottCss.loadCssFromFile("scottnotes.css")

if __name__ == '__main__':
    main()