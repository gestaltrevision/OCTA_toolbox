# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid, Stimulus
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon
from octa.measurements import LOCE

#%% Default grid
stimulus = Grid(6,6, background_color = "lightgrey")
stimulus.bounding_boxes = GridPattern.RandomPattern([(50,50)])

stimulus.shapes = GridPattern.RepeatAcrossRows([Triangle, Polygon])
stimulus.data   = GridPattern.RepeatAcrossRows(["", "3"])
stimulus.orientations = GridPattern.RepeatAcrossRows([0,0])

stimulus.Show()
