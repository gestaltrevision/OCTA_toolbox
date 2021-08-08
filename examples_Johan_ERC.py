# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 12:20:56 2020

@author: u0090621
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
stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRightDiagonal([RegularPolygon(4), RegularPolygon(5), RegularPolygon(6)])
stimulus.boundingboxes = GridPattern.RepeatAcrossRightDiagonal([(40,40)])
stimulus.fillcolors = GridPattern.RepeatAcrossRightDiagonal(['#6dd6ff', '#1b9fd8', '#006ca1'])  
#stimulus.bordercolors = GridPattern.RandomPattern(['#6dd6ff', '#1b9fd8', '#006ca1'])  
#stimulus.borderwidths = GridPattern.RandomPattern([5])

stimulus.Show()
filename = "1"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePDF(filename = "output/test")
#stimulus.SaveSVG(filename = "output/test")

#%%

random.seed(2)
stimulus.positions.SetPositionJitter(distribution = "uniform", min_val = 0, max_val = 30)

stimulus.Show()
filename = "2"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

random.seed(2)
stimulus._fillcolors.pattern = ["yellowgreen", "purple", "deepskyblue"]

stimulus.Show()
filename = "3"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")


#%%

stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.boundingboxes = GridPattern.RepeatAcrossRows([(40,40)])
stimulus.fillcolors = GridPattern.RepeatAcrossRows(['#6dd6ff', '#1b9fd8', '#006ca1'])  
                                                             
random.seed(2)
stimulus.positions = Positions.CreateSineGrid(n_rows = 6, n_cols = 6, row_spacing = 50, col_spacing = 50, A = 25, f = .2, axis = "x")

stimulus.Show()
filename = "4"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.boundingboxes = GridPattern.RepeatAcrossRows([(40,40)])
stimulus.fillcolors = GridPattern.RepeatAcrossRows(['#6dd6ff', '#1b9fd8', '#006ca1'])  
                                                             
random.seed(2)
stimulus.positions = Positions.CreateSineGrid(n_rows = 6, n_cols = 6, row_spacing = 50, col_spacing = 50, A = 25, f = .2, axis = "y")

stimulus.Show()
filename = "5"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")


#%% Default grid + change in values after initialization
stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRightDiagonal([Ellipse])
stimulus.boundingboxes = GridPattern.RepeatAcrossRightDiagonal([(40,40)])
stimulus.fillcolors = GridPattern.RepeatAcrossRightDiagonal(['#6dd6ff', '#1b9fd8', '#006ca1'])  
#stimulus.bordercolors = GridPattern.RandomPattern(['#6dd6ff', '#1b9fd8', '#006ca1'])  
#stimulus.borderwidths = GridPattern.RandomPattern([5])

stimulus.Show()
filename = "6"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePDF(filename = "output/test")
#stimulus.SaveSVG(filename = "output/test")

#%%

random.seed(2)
stimulus.positions.SetPositionJitter(distribution = "uniform", min_val = 0, max_val = 30)

stimulus.Show()
filename = "7"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

random.seed(2)
stimulus._fillcolors.pattern = ["yellowgreen", "purple", "deepskyblue"]

stimulus.Show()
filename = "8"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%% Default grid + change in values after initialization
stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRightDiagonal([Ellipse])
stimulus.boundingboxes = GridPattern.RepeatAcrossRightDiagonal([(40,40), (30,30),(20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossRightDiagonal(['#6dd6ff', '#1b9fd8', '#006ca1'])  
#stimulus.bordercolors = GridPattern.RandomPattern(['#6dd6ff', '#1b9fd8', '#006ca1'])  
#stimulus.borderwidths = GridPattern.RandomPattern([5])

stimulus.Show()
filename = "9"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePDF(filename = "output/test")
#stimulus.SaveSVG(filename = "output/test")

#%%

random.seed(2)
stimulus.positions.SetPositionJitter(distribution = "uniform", min_val = 0, max_val = 30)

stimulus.Show()
filename = "10"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

random.seed(2)
stimulus._fillcolors.pattern = ["yellowgreen", "purple", "deepskyblue"]

stimulus.Show()
filename = "11"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%
stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossColumns([Triangle])
stimulus.boundingboxes = GridPattern.RepeatAcrossColumns([(40,40), (30,30),(20,20)])
stimulus.orientations = GridPattern.RandomPattern([0,30,60])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])  
                                                             
random.seed(2)
stimulus.swap_elements(1)

stimulus.Show()
filename = "12"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

                                                             
#%%
#stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
#stimulus._autosize_method = "maximum_boundingbox"
#stimulus.shapes = GridPattern.RepeatAcrossRows([Triangle])
#stimulus.boundingboxes = GridPattern.RandomPattern([(40,40), (30,30),(20,20)])
#stimulus.orientations = GridPattern.RandomPattern([0,30,60,90,45,135])
#stimulus.fillcolors = GridPattern.RandomPattern(['#6dd6ff', '#1b9fd8', '#006ca1'])  
#                                                             
#random.seed(2)
#stimulus.orientations = Pattern(stimulus.orientations).AddNormalJitter(mu = 0, std = 10)
#
#stimulus.Show()
#filename = "13"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

stimulus = Grid(6,3, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.boundingboxes = GridPattern.RepeatAcrossRows([(30,20)])
stimulus.orientations = GridPattern.RepeatAcrossColumns([45,0,90])
stimulus.fillcolors = GridPattern.RepeatAcrossRows(['#6dd6ff', '#1b9fd8', '#006ca1'])  
                                                             
random.seed(2)
stimulus.positions = Positions.CreateCircle(radius = 150, n_elements = 18 )

stimulus.Show()
filename = "13"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")


#%%

stimulus = Grid(6,3, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.boundingboxes = GridPattern.RepeatAcrossRows([(30,20)])
stimulus.orientations = GridPattern.RepeatAcrossColumns([90])
stimulus.fillcolors = GridPattern.RepeatAcrossRows(['#6dd6ff', '#1b9fd8', '#006ca1'])  
                                                             
random.seed(2)
stimulus.positions = Positions.CreateCircle(radius = 150, n_elements = 18)
stimulus.set_element_orientation(element_id = 14, orientation_value = 0)
stimulus.set_element_orientation(element_id = 2, orientation_value = 0)
stimulus.set_element_orientation(element_id = 9, orientation_value = 0)

stimulus.Show()
filename = "14"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Rectangle])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([(30,20)])
stimulus.orientations = GridPattern.GradientAcrossElements(0, 360)
colorlist = Pattern.CreateColorRangeList('#6dd6ff', '#1b9fd8', n_elements = 36)
stimulus.fillcolors = GridPattern.RepeatAcrossElements(Pattern.CreateColorRangeList('yellowgreen', "purple", n_elements = 36))
                                                             
random.seed(2)
stimulus.positions = Positions.CreateCircle(radius = 150, n_elements = 36)

stimulus.Show()
filename = "15"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Rectangle])
stimulus.boundingboxes = GridPattern.RepeatAcrossElements([(20,30)])
stimulus.orientations = GridPattern.GradientAcrossColumns(-30, 30)
colorlist = Pattern.CreateColorRangeList('#6dd6ff', '#1b9fd8', n_elements = 36)
stimulus.fillcolors = GridPattern.RepeatAcrossRows(Pattern.CreateColorRangeList('#6dd6ff', '#006ca1', n_elements = 6))
                                                             
random.seed(2)

stimulus.Show()
filename = "16"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

stimulus = Grid(6,10, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.boundingboxes = GridPattern.RepeatAcrossRows([(20,30)])
stimulus.orientations = GridPattern.GradientAcrossColumns(-30, 30)
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
                                                             
random.seed(2)
stimulus.positions = Positions.CreateSineGrid(n_rows = 6, n_cols = 10, row_spacing = 50, col_spacing = 30, A = 25, f = .1, axis = "x")

stimulus.Show()
filename = "17"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.boundingboxes = GridPattern.RepeatAcrossRows([(40,40)])
stimulus.orientations = GridPattern.GradientAcrossColumns(-30, 30)
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
                                                             
random.seed(3)
stimulus.positions = Positions.CreateSineGrid(n_rows = 6, n_cols = 6, row_spacing = 40, col_spacing = 40, A = 25, f = .1, axis = "x")
stimulus.positions.SetLocationJitter(distribution = "normal", mu = 0, std = 8)

stimulus.Show()
filename = "18"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.boundingboxes = GridPattern.RepeatAcrossRows([(40,40)])
stimulus.orientations = GridPattern.GradientAcrossColumns(-30, 30)
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
                                                             
random.seed(3)
stimulus.positions = Positions.CreateSineGrid(n_rows = 6, n_cols = 6, row_spacing = 40, col_spacing = 40, A = 25, f = .1, axis = "x")


stimulus.Show()
filename = "19"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

stimulus = Grid(10,10, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.boundingboxes = GridPattern.RepeatAcrossRows([(30,30)])
stimulus.orientations = GridPattern.GradientAcrossColumns(-30, 30)
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
                                                             
random.seed(3)
stimulus.positions = Positions.CreateSineGrid(n_rows = 10, n_cols = 10, row_spacing = 30, col_spacing = 30, A = 25, f = .1, axis = "x")


stimulus.Show()
filename = "20"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%
random.seed(3)
stimulus = Grid(10,10, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0, row_spacing = 30, col_spacing = 30)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.boundingboxes = GridPattern.RandomPattern([(30,30), (25,25), (35,35)])
stimulus.orientations = GridPattern.GradientAcrossColumns(-30, 30)
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
                                                             

stimulus.Show()
filename = "21"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")

#%%

stimulus = Grid(10,10, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0, row_spacing = 30, col_spacing = 30)
stimulus._autosize_method = "maximum_boundingbox"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.boundingboxes = GridPattern.RandomPattern([(30,30), (25,25), (35,35)])
stimulus.orientations = GridPattern.GradientAcrossColumns(-30, 30)
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
                                                             
random.seed(3)
#stimulus.positions = Positions.CreateSineGrid(n_rows = 10, n_cols = 10, row_spacing = 30, col_spacing = 30, A = 25, f = .1, axis = "x")
stimulus.positions.SetPositionJitter(distribution = "normal", mu = 0, std = 5)


stimulus.Show()
filename = "22"
#stimulus.SaveSVG(filename, folder = "octa_examples_johan_ERC")
#stimulus.SavePNG(filename, folder = "octa_examples_johan_ERC/PNG")
#stimulus.SaveJSON(filename, folder = "octa_examples_johan_ERC")