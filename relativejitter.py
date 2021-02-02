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
import numpy as np

#%%

# stimulus without jitter 
random.seed(3)

x_jitterratio = 0.3
y_jitterratio = 0.3

stimulus = Grid(6,6, size = (500,500), row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([(30,30), (30*1.8,30*1.8)], 2 , 2),3)
stimulus.bounding_boxes = tiled_grid_1

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([Rectangle, Ellipse], 2 , 2),3)
stimulus.shapes = tiled_grid_1

stimulus.Show()

#%%
# Jitter size relative to bounding box size

random.seed(3)

stimulus = Grid(6,6, size = (500,500), row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([(30,30), (30*1.8,30*1.8)], 2 , 2),3)
stimulus.bounding_boxes = tiled_grid_1

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([Rectangle, Ellipse], 2 , 2),3)
stimulus.shapes = tiled_grid_1

x_boundingboxes =  [i[0] for i in stimulus.bounding_boxes]
x_maxjitter = [i*x_jitterratio for i in x_boundingboxes]
y_boundingboxes =  [i[1] for i in stimulus.bounding_boxes]
y_maxjitter = [i*y_jitterratio for i in y_boundingboxes]
random.seed(3)
x_jitter = [random.uniform(-x_maxjitter[_], x_maxjitter[_]) for _ in range(len(stimulus.positions.x))]
random.seed(3)
y_jitter = [random.uniform(-y_maxjitter[_], y_maxjitter[_]) for _ in range(len(stimulus.positions.y))]
new_x = [stimulus.positions.x[i] + x_jitter[i] for i in range(len(stimulus.positions.x))]
new_y = [stimulus.positions.y[i] + y_jitter[i] for i in range(len(stimulus.positions.y))]
stimulus.positions = Positions.CreateCustomPositions(x = new_x, y = new_y)
                                
stimulus.Show()


#%%

# Jitter size relative to -mean- bounding box size
random.seed(3)

stimulus = Grid(6,6, size = (500,500), row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([(30,30), (30*1.8,30*1.8)], 2 , 2),3)
stimulus.bounding_boxes = tiled_grid_1

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([Rectangle, Ellipse], 2 , 2),3)
stimulus.shapes = tiled_grid_1

x_boundingboxes =  [i[0] for i in stimulus.bounding_boxes]
x_maxjitter = x_jitterratio*np.mean(x_boundingboxes)
y_boundingboxes =  [i[1] for i in stimulus.bounding_boxes]
y_maxjitter = y_jitterratio*np.mean(y_boundingboxes)

random.seed(3)
stimulus.positions.SetLocationJitter(distribution = "uniform", axis = "x", min_val = -x_maxjitter, max_val = x_maxjitter)

random.seed(3)
stimulus.positions.SetLocationJitter(distribution = "uniform", axis = "y", min_val = -y_maxjitter, max_val = y_maxjitter)
                                
stimulus.Show()

#%%

# Jitter size relative to column & row spacing

random.seed(3)

stimulus = Grid(6,6, size = (500,500), row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([(30,30), (30*1.8,30*1.8)], 2 , 2),3)
stimulus.bounding_boxes = tiled_grid_1

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([Rectangle, Ellipse], 2 , 2),3)
stimulus.shapes = tiled_grid_1

x_maxjitter = x_jitterratio*stimulus.row_spacing
y_maxjitter = y_jitterratio*stimulus.col_spacing

random.seed(3)
stimulus.positions.SetLocationJitter(distribution = "uniform", axis = "x", min_val = -x_maxjitter, max_val = x_maxjitter)

random.seed(3)
stimulus.positions.SetLocationJitter(distribution = "uniform", axis = "y", min_val = -y_maxjitter, max_val = y_maxjitter)
                                
stimulus.Show()