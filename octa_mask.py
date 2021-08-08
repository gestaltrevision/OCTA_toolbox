# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 08:30:12 2021

@author: Eline Van Geert
"""

from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg
from octa.measurements import Complexity
import random
from octa.shapes.Polygon import Polygon_
from octa.shapes.RegularPolygon import RegularPolygon_
from octa.shapes.Image import Image_
from octa.shapes.FitImage import FitImage_
from octa.shapes.Path import Path_
from octa.shapes.PathSvg import PathSvg_

#%%

stimulus = Grid(4,4, stim_classlabel = "leftstim", stim_idlabel = "blue_octagons")
stimulus1.SaveSVG("output/blue_oc")
#%%

# Test Polygon shapes with n_sides as input 
stimsize = (600,600)
clipshape = Ellipse(position = (stimsize[0]/2,stimsize[1]/2), boundingbox = (500,500))
shapemask = Rectangle(position = (stimsize[0]/2,stimsize[1]/2), boundingbox = (600,600))
#clipshape = RegularPolygon_(position = (stimsize[0]/2,stimsize[1]/2), boundingbox = (500,500), data = 8)
shapemask = FitImage_(position = (stimsize[0]/2,stimsize[1]/2), boundingbox = (500,500), data = "img/checkmark.svg")
#clipshape = Path_(position = (stimsize[0]/2,stimsize[1]/2), boundingbox = (500,500), 
#                  data = ["M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z", 288,288])
shapemask = PathSvg_(position = (stimsize[0]/2,stimsize[1]/2), boundingbox = (500,500), 
                  data = "img/checkmark.svg")
gradientmask =  Rectangle(position = (stimsize[0]/2,stimsize[1]/2), boundingbox = (600,600),
                          fillcolor = ["radial", "white",  "black"])

# imagemask = Image(src = "img/checkmark.svg")

stimulus = Grid(10,10, background_color = "lightgrey", row_spacing = 60, col_spacing = 60, size = stimsize,
                background_shape = clipshape , stim_mask = gradientmask)
stimulus._autosize_method = "maximum_boundingbox"

# #stimulus.shapes = GridPattern.RepeatAcrossRows([RegularPolygon(4), RegularPolygon(5), RegularPolygon(6, "Hexagon"), Polygon(6, "Hexagon")])
# stimulus.shapes = GridPattern.RepeatAcrossRows([RegularPolygon(8)]) #Polygon(8)
# #, Rectangle, Image("img/checkmark.svg"), Text("OCTA"), PathSvg("img/checkmark.svg"), 
# #                                                Path("M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z", 288,288)])

# # stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
# stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

# stimulus.opacities = GridPattern.RepeatAcrossColumns([0.1,0.5,1])

# #stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
# #stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

# stimulus.set_element_fillcolor(25, "red")
# stimulus.set_element_shape(25, Rectangle)
# stimulus.set_element_shape(25, PathSvg("img/checkmark.svg"))

stimulus.Show()
stimulus.SaveSVG("test_mask")
# stimulus.SaveJSON("test_mask")

# import svgwrite
# from IPython.display import SVG, display

# dwg = svgwrite.Drawing(size = (600,600)) 

# dwg.add(dwg.rect((0, 0), (600,600), fill = 'lightgrey'))


# clip_path = dwg.defs.add(dwg.clipPath(id='my_clip_path1')) #name the clip path
# clip_path.add(dwg.ellipse((300, 300), (50,50))) #things inside this shape will be drawn
       
# testCircle = dwg.add(dwg.g(id='test', fill_opacity=1, clip_path="url(#my_clip_path1)"))
# testCircle.add(dwg.rect((200, 200), (200,200), fill = 'blue'))

# dwg.saveas("test.svg")