# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 13:18:08 2021

@author: Eline Van Geert
"""

from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, Text, Polygon, RegularPolygon, Path, PathSvg
from octa.measurements import Complexity
import random

#%%

# Jitter size relative to bounding box size

random.seed(3)

x_jitterratio = 0
y_jitterratio = 0.5

stimulus = Grid(6,6, background_color = "gainsboro", size = (350,350), row_spacing = 50, col_spacing = 50)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,30),(20,10)])

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([(20,20), (36,36)], 2 , 2),3)
stimulus.bounding_boxes = tiled_grid_1

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([Rectangle, Ellipse], 2 , 2),3)
stimulus.shapes = tiled_grid_1

stimulus.Show()
x_boundingboxes =  [i[0] for i in stimulus.bounding_boxes]
x_maxjitter = [i*x_jitterratio for i in x_boundingboxes]
y_boundingboxes =  [i[1] for i in stimulus.bounding_boxes]
y_maxjitter = [i*y_jitterratio for i in y_boundingboxes]
x_jitter = [random.uniform(-x_maxjitter[_], x_maxjitter[_]) for _ in range(len(stimulus.positions.x))]
y_jitter = [random.uniform(-y_maxjitter[_], y_maxjitter[_]) for _ in range(len(stimulus.positions.y))]
new_x = [stimulus.positions.x[i] + x_jitter[i] for i in range(len(stimulus.positions.x))]
new_y = [stimulus.positions.y[i] + y_jitter[i] for i in range(len(stimulus.positions.y))]
stimulus.positions = Positions.CreateCustomPositions(x = new_x, y = new_y)
                                
stimulus.Show()