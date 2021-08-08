# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:02:14 2021

@author: u0090621
"""

# place items on boundary shape (path) in equally spaced way

width = 500
height = 500

from IPython.display import SVG, display
import svgpathtools
import svgwrite

topleft = (100 - width/2 , 100 - height/2)
paths, attributes = svgpathtools.svg2paths("img/checkmark.svg")

orilength = paths[0].length()

n_paths = len(paths)
allpaths = []

for i in range(0,n_paths):
    mypath = paths[i]
    xmin, xmax, ymin, ymax = mypath.bbox()
    xsize = xmax - xmin
    ysize = ymax - ymin
    allpaths.append([xsize, ysize])
    
max_xsize = max([item[0] for item in allpaths])
max_ysize = max([item[1] for item in allpaths])
scale_x_parameter = width / max_xsize
scale_y_parameter = height / max_ysize

d = " ".join([item["d"] for item in attributes])


#############
paths[0].length()

n_elements = 100
step_size = float(1 / n_elements)

xpositions = []
ypositions = []

for n in range(n_elements):
    coords = paths[0].point(step_size * n)
    x,y = str(coords).replace("(", "").replace(")", "").replace("j", "").split("+")
    xpositions.append(float(x))
    ypositions.append(float(y))
    
    
xpositions_new = [xposition*scale_x_parameter for xposition in xpositions]
ypositions_new = [yposition*scale_y_parameter for yposition in ypositions]


####
from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg
from octa.measurements import Complexity
import random


# Test Polygon shapes with n_sides as input 

stimulus = Grid(10, 10, row_spacing = 60, col_spacing = 60, background_color = "none")
stimulus._autosize_method = "maximum_boundingbox"

#stimulus.shapes = GridPattern.RepeatAcrossRows([RegularPolygon(4), RegularPolygon(5), RegularPolygon(6, "Hexagon"), Polygon(6, "Hexagon")])
stimulus.shapes = GridPattern.RepeatAcrossRows([Rectangle, Ellipse, Triangle, PathSvg("img/checkmark.svg")])
#                                                Image("img/optotypes/butterfly.svg"),
#                                                , 
#                                                PathSvg("img/optotypes/butterfly.svg"),
#                                                Path("M35.67,19.72a22.05,22.05,0,0,0,3-11.26c-.19-2.92-1.79-6-5.13-6-3.7,0-7.09,3.3-8.48,6.26-1.17,2.5-.41,6.67-4.46,6.8-4-.13-3.29-4.3-4.46-6.8-1.38-3-4.77-6.21-8.47-6.26-3.35,0-4.95,3-5.13,6a22.05,22.05,0,0,0,3,11.26c2.38,4-1.87,6.79-1.06,10.85.6,3,3.47,7.74,6.87,8.05s4.85-6.63,6.17-8.87a3.91,3.91,0,0,1,6.24,0C25,32,26.32,39,29.86,38.63s6.27-5.07,6.87-8.05C37.54,26.51,33.29,23.76,35.67,19.72Z", 41.15, 41.14)])
#, Rectangle, Image("img/checkmark.svg"), Text("OCTA"), PathSvg("img/checkmark.svg"), 
#                                                Path("M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z", 288,288)])

#stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
##stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])
#stimulus.opacities = GridPattern.RepeatAcrossColumns([0.5,1])
#stimulus.borderwidths = GridPattern.RepeatAcrossElements([5])
#stimulus.bordercolors = GridPattern.RepeatAcrossElements(["black"])
#stimulus.mirrorvalues = GridPattern.RepeatAcrossElements(["horizontal", "vertical"])
#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['mirrorvalues'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['fillcolors', 'mirrorvalues'])

stimulus.positions = Positions.CreateCustomPositions(xpositions_new, ypositions_new)
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([(25,25)])
stimulus.fillcolors = GridPattern.RepeatAcrossElements(Pattern.CreateColorRangeList(start_color = "red", end_color = "blue", n_elements = 100))

stimulus.Show()
#stimulus.SavePNG("test")
stimulus.SaveJSON("test")
stimulus.SaveSVG("test")

#%%
stim = Stimulus.LoadFromJSON("test.json")
                  
stim.Show()