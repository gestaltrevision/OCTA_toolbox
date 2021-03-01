# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 18:24:51 2021

@author: u0090621
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg
from octa.measurements import Complexity
import random


# Test Polygon shapes with n_sides as input 

stimulus = Grid(10,10, row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

#stimulus.shapes = GridPattern.RepeatAcrossRows([RegularPolygon(4), RegularPolygon(5), RegularPolygon(6, "Hexagon"), Polygon(6, "Hexagon")])
stimulus.shapes = GridPattern.RepeatAcrossRows([Rectangle, Text('OCTA')])
#, Rectangle, Image("img/checkmark.svg"), Text("OCTA"), PathSvg("img/checkmark.svg"), 
#                                                Path("M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z", 288,288)])

stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])
stimulus.opacities = GridPattern.RepeatAcrossColumns([0.5,1])
#stimulus.mirror_values = GridPattern.RepeatAcrossElements(["horizontal", "vertical"])
#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['mirror_values'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['fillcolors', 'mirror_values'])

stimulus.Show()
#stimulus.SavePNG("test")
stimulus.SaveJSON("test")
#stimulus.SaveSVG("test")

#%%
stim = Stimulus.LoadFromJSON("test.json")
                  
stim.Show()