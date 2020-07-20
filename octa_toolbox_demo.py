# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid, Stimulus
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon, RegularPolygon
from octa.measurements import LOCE

#%%
def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(round(r*255),round(g*255),round(b*255))

#%% Default grid
stimulus = Grid(6,6, background_color = "lightgrey", x_margin = 50, y_margin = 50)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (40,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
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

#%% Default grid with size (this should autocenter on the middle of the figure)
stimulus = Grid(6,6, background_color = "lightgrey", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (40,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ["fillcolors"])
stimulus.Show()
#print(stimulus.CalculateCenter())
