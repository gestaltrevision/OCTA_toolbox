# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:51:11 2020

@author: eline
"""


from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern, Sequence
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon, RegularPolygon
from octa.measurements import Complexity
import random

#%%
random.seed(3)
stimulus = Grid(10,10, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0, row_spacing = 30, col_spacing = 30)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns([(30,30)])
#stimulus.orientations = GridPattern.RepeatAcrossColumns(Pattern.CreateNumberRangeList( -60, 60, n_elements = 10))
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 10))
                                                             
stimulus.Show()

#%%
# gradient in xy direction bounding box
#stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns([(30,30), (27.5, 27.5), (25,25), (22.5,22.5), (20,20), (17.5, 17.5), (15,15), (12.5,12.5), (10,10), (7.5,7.5) ])
stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns(Pattern.Create2DGradient(Sequence(30, -2.5), Sequence(30, -2.5), 10))
stimulus.Show()

#%%
# gradient in x direction bounding box
stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns([(30,30), (27.5, 30), (25,30), (22.5,30), (20,30), (17.5, 30), (15,30), (12.5,30), (10,30), (7.5,30) ])
stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns(Pattern.Create2DGradient(Sequence(30, -2.5), 30, 10))
stimulus.Show()

#%%
# gradient in y direction bounding box
stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns([(30,30), (30, 27.5), (30,25), (30,22.5), (30,20), (30, 17.5), (30,15), (30,12.5), (30,10), (30, 7.5) ])
stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns(Pattern.Create2DGradient(30, Sequence(30, -2.5), 10))
stimulus.Show()

