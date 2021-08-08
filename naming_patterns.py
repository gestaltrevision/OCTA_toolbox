# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:38:47 2021

@author: u0090621
"""


#%%

from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg
from octa.measurements import Complexity
import random

# Test Polygon shapes with n_sides as input 

stimulus = Grid(6,6, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_boundingbox"

stimulus.shapes = GridPattern.RepeatAcrossRows([RegularPolygon(4), RegularPolygon(5), RegularPolygon(6, "Hexagon"), Polygon(6, "Hexagon")])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

colors_1 = [["radial", "white", "red"], "green", "blue"]
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(colors_1)
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(Pattern(colors_1).RepeatElements(int(stimulus.n_rows/len(colors_1))))
                                    


#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")