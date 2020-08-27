# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon, RegularPolygon
from octa.measurements import Complexity
import random

#%%
def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(round(r*255),round(g*255),round(b*255))

#%% Default grid + change in values after initialization
stimulus = Grid(6,6, background_color = "white", x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RandomPattern([(50,50), (40,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RandomPattern(['#6dd6ff', '#1b9fd8', '#006ca1'])  
#stimulus.bordercolors = GridPattern.RandomPattern(['#6dd6ff', '#1b9fd8', '#006ca1'])  
#stimulus.borderwidths = GridPattern.RandomPattern([5])

stimulus.Show()
stimulus.SavePNG(filename = "output/test")
stimulus.SavePDF(filename = "output/test")
stimulus.SaveSVG(filename = "output/test")

random.seed(2)
stimulus.positions.SetLocationJitter(distribution = "uniform", min_val = 5, max_val = 40)

stimulus.Show()

random.seed(2)
stimulus._fillcolors.pattern = ["red", "green", "blue"]

stimulus.Show()
#stimulus.CalculateCenter()

#%% Default grid with size (this should autocenter on the middle of the figure)
stimulus = Grid(6,6, background_color = "lightgrey", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (40,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.Show()
#print(stimulus.CalculateCenter())

#%% Example swap_distinct_features
stimulus = Grid(6,6, background_color = "lightgrey", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (40,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ["fillcolors"])
stimulus.Show()
#print(stimulus.CalculateCenter())

#%% Image
stimulus = Grid(6,6, background_color = "white", x_margin = 50, y_margin = 50)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.shapes = GridPattern.RepeatAcrossElements([Image, Text])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,30), (10,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.data = GridPattern.RepeatAcrossElements(["img/test.jpg", "TEXT"])
stimulus.Show()
#stimulus.CalculateCenter()
stimulus._fillcolors.pattern
stimulus._fillcolors.patterntype
stimulus._fillcolors.patternorientation

#%% Order and complexity measures
stimulus = Grid(6,6, background_color = "lightgrey", x_margin = 50, y_margin = 50)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (40,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.Show()
print("LOCE = ", Complexity.CalculateElementsLOCE(stimulus, distinction_features = ["bounding_boxes", "fillcolors", "shapes"]))
print("LOC = ", Complexity.CalculateElementsLOC(stimulus, distinction_features = ["bounding_boxes", "fillcolors", "shapes"]))
print("LOCI = ", Complexity.CalculateElementsLOCI(stimulus, distinction_features = ["bounding_boxes", "fillcolors", "shapes"]))

#%% Output files
stimulus = Grid(6,6, background_color = "lightgrey", size =(300,300))
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (40,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.Show()
stimulus.SaveSVG(filename = "output/testoutput")
stimulus.SaveJSON(folder = "output", filename = "testoutput")

#%% Apply jitter to feature (e.g. orientation)

#%%
random.seed(3)

stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(20,40)])
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
                                                                                   
stimulus.orientations = GridPattern.RepeatAcrossElements([30])
#orientationjitter = Pattern(stimulus.orientations).AddUniformJitter(min_val = -20, max_val = 20)
orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0 , std = 30)
stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)
                                                             
stimulus.Show()

#%%

# remove an element

random.seed(3)

stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(20,40)])
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
                                                                                   
stimulus.orientations = GridPattern.RepeatAcrossElements([30])
#orientationjitter = Pattern(stimulus.orientations).AddUniformJitter(min_val = -20, max_val = 20)
orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0 , std = 30)
stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)
                                                             
stimulus.Show()

stimulus.remove_element(2)

stimulus.Show()

#%%

# image as shape

random.seed(3)

stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Image])
stimulus.data = GridPattern.RepeatAcrossElements(["img/checkmark.svg"])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,40)])
                                                        
stimulus.orientations = GridPattern.RepeatAcrossElements([30])
#orientationjitter = Pattern(stimulus.orientations).AddUniformJitter(min_val = -20, max_val = 20)
orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0 , std = 30)
stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)
                                                             
stimulus.Show()

stimulus.remove_element(2)

stimulus.Show()