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
paths, attributes = svgpathtools.svg2paths("butterfly.svg")


#path_alt = svgpathtools.parse_path("M 10 10 H 90 V 90 H 10 L 10 10")

#orilength = paths[0].length()

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


#####






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
from octa.shapes.Path import Path_

#stimsize = (288,288)
#clipshape = Path_(position = (stimsize[0]/2,stimsize[1]/2), bounding_box = (288,288), 
#                  data = ["M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z", 288,288])


# Test Polygon shapes with n_sides as input 

stimulus = Grid(20, 20, row_spacing = 25, col_spacing = 25, background_color = "none")
stimulus._autosize_method = "maximum_bounding_box"

#stimulus.shapes = GridPattern.RepeatAcrossRows([RegularPolygon(4), RegularPolygon(5), RegularPolygon(6, "Hexagon"), Polygon(6, "Hexagon")])
stimulus.shapes = GridPattern.RepeatAcrossRows([Rectangle, Ellipse, Triangle, PathSvg("butterfly.svg")])
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
#stimulus.mirror_values = GridPattern.RepeatAcrossElements(["horizontal", "vertical"])
#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['mirror_values'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['fillcolors', 'mirror_values'])

#stimulus.positions = Positions.CreateCustomPositions(xpositions_new, ypositions_new)
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(15,15)])
stimulus.fillcolors = GridPattern.RepeatAcrossElements(Pattern.CreateColorRangeList(start_color = "red", end_color = "blue", n_elements = 100))

stimulus.set_element_fillcolor(105, "red")
stimulus.set_element_shape(105, Rectangle)
stimulus.set_element_shape(105, PathSvg("img/checkmark.svg"))

stimulus.Show()
#stimulus.SavePNG("test")
stimulus.SaveJSON("test")
stimulus.SaveSVG("test")


#stim = Stimulus.LoadFromJSON("test.json")
#                  
#stim.Show()

###############"


redpath = paths[0]
redpath_attribs = attributes[0]
intersections = []
elements_to_keep = []
elements_to_remove = []

redpath = svgpathtools.parse_path("M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z")

#redpath.point(pos = 0)

pathobjects = []

objects = stimulus.positions.GetPositions()
sizes = stimulus.bounding_boxes

for i in range(len(objects[0])):
    x_position = objects[0][i]
    y_position = objects[1][i]
    x_size, y_size = sizes[i] 
        
    objectpath = svgpathtools.Path(
         svgpathtools.Line(start=(x_position + y_position * 1j), end=(float(x_position + x_size) + y_position * 1j)),
         svgpathtools.Line(start=(float(x_position + x_size) + y_position * 1j), end=(float(x_position + x_size) + float(y_position + y_size) * 1j)),
         svgpathtools.Line(start=(float(x_position + x_size) + float(y_position + y_size) * 1j), end=(x_position + float(y_position + y_size) * 1j)),
         svgpathtools.Line(start=(x_position + float(y_position + y_size) * 1j), end=(x_position + y_position * 1j)))
    paths.append(objectpath)

for i in range(len(paths[1:])):
    path = paths[i+1]
    for (T1, seg1, t1), (T2, seg2, t2) in redpath.intersect(path):
        intersections.append(redpath.point(T1))
        if i not in elements_to_keep:
            elements_to_keep.append(i)
            
# only keep elements on border (within grid structure)
for i in range(len(paths[1:])):
    if i not in elements_to_keep:
        elements_to_remove.append(i) 
        
# keep elements on and within border (within grid structure)
elements_to_keep_all = []
elements_to_remove = []
for row in range(stimulus.n_rows):
    rowelements_to_keep = []
    min_element = row * stimulus.n_cols
    max_element = (row+1) * stimulus.n_cols
    for element in elements_to_keep:
        if element in range(min_element, max_element):
            rowelements_to_keep.append(element)
    if len(rowelements_to_keep) >= 2:
        min_element_to_keep = min(rowelements_to_keep)
        max_element_to_keep = max(rowelements_to_keep)
        elements_to_keep_all.extend(range(min_element_to_keep, max_element_to_keep))
        elements_to_remove.extend(range(min_element, min_element_to_keep))
        elements_to_remove.extend(range(max_element_to_keep, max_element))
    elif len(rowelements_to_keep) == 1 :    
        elements_to_keep_all.append(min_element_to_keep)        
    else:
        elements_to_remove.extend(range(min_element, max_element))
        

#elements_to_remove = []
#if i not in elements_to_keep_all:
#    elements_to_remove.append(i)      

#Stimulus.set_element_shape(stimulus, element_id = 0, shape_value = "None")
for i in elements_to_remove:
    stimulus.remove_element(i)
stimulus.Show()
stimulus.SaveSVG("test_fullelementsclipshape")