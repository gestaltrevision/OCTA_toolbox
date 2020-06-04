# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid, Circles
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text



stimulus = Grid(5, 5, x_offset = 40, y_offset = 40, row_spacing = 100, col_spacing = 100)
stimulus.bounding_boxes = GridPattern.RepeatElements([(40, 40)])
stimulus.shapes         = GridPattern.RepeatElements([Text, None, Image])
stimulus.orientation    = GridPattern.RepeatElements([45])
stimulus.borderwidths   = GridPattern.RepeatElements([1])
stimulus.bordercolours  = GridPattern.RepeatElements(["red", "green", "blue"])
stimulus.fillcolours    = GridPattern.RepeatElements(["green", "blue", "red"])
stimulus.data           = GridPattern.RepeatElements(["hello everybody in the houses tonight how","",r"C:\Users\Christophe\Documents\My Dropbox\personal_projects\100twh\web\assets\images\iconfinder_1_social_2609541.png"])

stimulus.Show()

