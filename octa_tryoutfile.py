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

#%%

# Test Polygon shapes with n_sides as input 

stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([RegularPolygon(4), RegularPolygon(5), RegularPolygon(6, "Hexagon"), Polygon(6, "Hexagon")])
stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")


#%%

# Test Text shape with text to use as input 
stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([Text("OCTA"), Rectangle, Text("O3"), Text("Hola\nPola", name = "stopexpression"), Polygon(8)])
#stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")

#%%

# Test Image shape with source to use as input 
stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([Image("img/checkmark.svg", name = "Checkmark"), Image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg"), FitImage("img/w3c_home.png", name = "W3C_png")])
#stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")

#%%

# Test Path shape with path and size of path to use as input 
stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows(
        [Path(name = "Arrow", path = "M12 22A10 10 0 1 0 2 12a10 10 0 0 0 10 10zM8.31 10.14l3-2.86a.49.49 0 0 1 .15-.1.54.54 0 0 1 .16-.1.94.94 0 0 1 .76 0 1 1 0 0 1 .33.21l3 3a1 1 0 0 1-1.42 1.42L13 10.41V16a1 1 0 0 1-2 0v-5.66l-1.31 1.25a1 1 0 0 1-1.38-1.45z", xsize = 24, ysize = 24),
         Path(name = "Checkmark", path = "M 256.00,0.00C 114.615,0.00,0.00,114.615,0.00,256.00s 114.615,256.00, 256.00,256.00s 256.00-114.615, 256.00-256.00S 397.385,0.00, 256.00,0.00z M 208.00,416.00L 102.00,278.00l 47.00-49.00l 59.00,75.00 l 185.00-151.00l 23.00,23.00L 208.00,416.00z", xsize = 512, ysize = 512)])
#stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")


#%%

# Test PathSvg shape with path and size of path to use as input 
stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows(
        [PathSvg("img/checkmark.svg", name = "Checkmark"),
         PathSvg("img/arrow-circle-up-svgrepo-com.svg", name = "Arrow")])
#stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")