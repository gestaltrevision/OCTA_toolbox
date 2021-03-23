# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 15:52:04 2021

@author: u0090621
"""

import svgwrite 

path = [(100,100),(100,200),(200,200),(200,100)]

image = svgwrite.Drawing('test.svg',size=(300,300))

rectangle = image.add(image.polygon(path,id ='polygon',stroke="black",fill="white"))
rectangle.add(image.animateTransform("scale","transform",id="polygon", from_="0", to="1",dur="4s",begin="0s",repeatCount="indefinite", additive = "sum"))    
rectangle.add(image.animateTransform("rotate","transform",id="polygon", from_="0 150 150", to="360 150 150",dur="4s",begin="0s", additive = "sum", repeatCount="indefinite"))

image.save()

