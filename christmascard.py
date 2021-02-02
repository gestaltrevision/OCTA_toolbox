# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 17:28:23 2020

@author: u0090621
"""
from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon, RegularPolygon, Path, PathSvg
from octa.measurements import Complexity
import random

#%%

# image as shape

random.seed(3)

stimulus = Grid(10,9, background_color = "white", x_margin = 0, y_margin = 0, row_spacing = 60, col_spacing = 60)
#stimulus.positions = Positions.CreateSineGrid(n_rows = 9, n_cols = 9, row_spacing = 60, col_spacing = 60, A = 25, f = .1, axis = "xy")

stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([PathSvg
                                                ])
stimulus.bounding_boxes = GridPattern.MirrorAcrossLeftDiagonal([(50,50), (40,50), (40,40), (40,50),
                                                            (40,50), (50,50), (50,50), (50,50),
                                                            (50,50)])
stimulus.data = GridPattern.MirrorAcrossLeftDiagonal(["C:/Users/u0090621/Downloads/lab/christmascard/baubles-christmas-svgrepo-com.svg",
                                                  "C:/Users/u0090621/Downloads/lab/christmascard/candy-cane-christmas-svgrepo-com.svg",
                                                  "C:/Users/u0090621/Downloads/lab/christmascard/christmas-bauble-svgrepo-com (1).svg",
                                                  "C:/Users/u0090621/Downloads/lab/christmascard/christmas-bauble-svgrepo-com.svg",
                                                  "C:/Users/u0090621/Downloads/lab/christmascard/christmas-gingerbread-man-svgrepo-com.svg",
                                                  "C:/Users/u0090621/Downloads/lab/christmascard/christmas-snow-globe-with-tree-inside-svgrepo-com.svg",
                                                  "C:/Users/u0090621/Downloads/lab/christmascard/christmas-star-svgrepo-com (1).svg",
                                                  "C:/Users/u0090621/Downloads/lab/christmascard/christmas-star-svgrepo-com.svg",
                                                  "C:/Users/u0090621/Downloads/lab/christmascard/christmas-tree-svgrepo-com (3).svg",
                                            
                                                  ])
                                                        
stimulus.fillcolors = GridPattern.GradientAcrossElements('yellowgreen', "red")
#stimulus.orientations = GridPattern.RepeatAcrossElements([0])
#orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0, std = 20)
# 
#
#stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)
#
#
stimulus.positions.SetLocationJitter(distribution = "normal", mu = 0, std = 3)
                                                             
stimulus.Show()