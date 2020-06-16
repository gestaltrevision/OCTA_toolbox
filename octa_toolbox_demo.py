# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon



stimulus = Grid(9, 9, x_offset = 40, y_offset = 40, row_spacing = 50, col_spacing = 50)
stimulus.shapes = GridPattern.MirrorAcrossRows([Ellipse, Rectangle, Triangle])
stimulus.fillcolours = GridPattern.MirrorAcrossColumns(["red", "green","blue","orange"])
stimulus.swap_elements(5)
stimulus.Show()
stimulus.SaveJSON("mystim", r"C:\Users\Christophe\Desktop\todo\octa\OCTA_toolbox\output")

stim = Stimulus.LoadFromJSON( r"C:\Users\Christophe\Desktop\todo\octa\OCTA_toolbox\output\mystim.json")
stim.Show()