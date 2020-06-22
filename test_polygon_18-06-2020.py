# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 19:15:37 2020

@author: u0090621
"""
from octa.Stimulus import Grid, Stimulus
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon
#%% Adjusting grid structure dynamically
stimulus = Grid(6, 6, x_offset = 40, y_offset = 40, row_spacing = 50, col_spacing = 50)
stimulus.shapes = GridPattern.MirrorAcrossRows([Rectangle, Polygon, Triangle])
stimulus.data = GridPattern.RepeatAcrossElements([3,4,5,6,7,8])
stimulus.bounding_boxes = GridPattern.MirrorAcrossRows([(45,45)])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0, 90, 0, 0, 0, 0])
stimulus.fillcolours = GridPattern.MirrorAcrossColumns(["red", "green","blue","orange"])
stimulus.Show()
