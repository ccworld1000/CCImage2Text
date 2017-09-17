#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CCImage2Text.py
#  
#  Created by CC on 2017/09/16.
#  Copyright 2017 youhua deng (deng you hua) <ccworld1000@gmail.com>
#  https://github.com/ccworld1000/CCImage2Text
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
length = len(ascii_char)

def image2text (name) :
	img = Image.open(name)
	(width,height) = img.size
	#img = img.resize((int(width*0.9),int(height*0.5))) 
	img = img.resize((int(width*0.5),int(height*0.4)))
	print(img.size)
	return img

def convert(img):
    img = img.convert("L")
    txt = ""
    

    for i in range(img.size[1]):
        for j in range(img.size[0]):
            gray = img.getpixel((j, i))
            unit = 256.0 / length
            txt += ascii_char[int(gray / unit)]
        txt += '\n'
    return  txt

def convert1(img):
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            r,g,b = img.getpixel((j, i)) 
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)
            unit = (256.0+1)/length
            txt += ascii_char[int(gray / unit)]
        txt += '\n'
    return txt

def write2text (imageName, textName) :
	img = image2text (imageName)
	txt = convert(img)
	
	f = open (textName, "w")
	f.write(txt)
	f.close()
	


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
