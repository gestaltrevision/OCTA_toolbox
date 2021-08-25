# -*- coding: utf-8 -*-
"""
OCTA toolbox overview

The Order & Complexity Toolbox for Aesthetics (OCTA) Python library is a tool for researchers 
to create stimuli varying in order and complexity on different dimensions. 
Copyright (C) 2021  Eline Van Geert, Christophe Bossens, and Johan Wagemans

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: eline.vangeert@kuleuven.be

"""
from octa.Stimulus import Grid, Outline, Concentric, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern, Sequence, LinearGradient
from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg
# from octa.shapes.Image import Image_
# from octa.shapes.FitImage import FitImage_
# from octa.shapes.Text import Text_ 
# from octa.shapes.Polygon import Polygon_
# from octa.shapes.RegularPolygon import RegularPolygon_
# from octa.shapes.Path import Path_
# from octa.shapes.PathSvg import PathSvg_
from octa.measurements import Order, Complexity
import random

#%%

# s = Stimulus(x_margin = 20, y_margin = 20, size = None, 
#              background_color = "white", background_shape = None, 
#              stim_mask = None, stim_orientation = 0, stim_mirrorvalue = None, 
#              stim_link = None, stim_classlabel = None, stim_idlabel = None)

s = Grid(n_rows = 3, n_cols = 3, row_spacing = 50, col_spacing= 50, 
         x_margin = 20, y_margin = 20, size = None, 
         background_color = "white", background_shape = None, 
         stim_mask = None, stim_orientation = 0, stim_mirrorvalue = None, 
         stim_link = None, stim_classlabel = None, stim_idlabel = None)

filename = "test"

s.SaveSVG(filename, scale = None, folder = None)
s.GetSVG()
s.SavePNG(filename, scale = None, folder = None)
s.SavePDF(filename, scale = None, folder = None)
s.SaveTIFF(filename, scale = None, folder = None)
s.SaveJPG(filename, scale = None, folder = None)
s.SaveJSON(filename, folder = None)
s.GetElementsDF()
s.SaveElementsDF(filename, folder = None)
s.GetJSON()

s.Render()
s.Show()
s.x_margin = 0
s.y_margin = 0
s.n_rows = 4
s.n_cols = 2

s.Show()

#%% 
# LoadFromJSON example

# Save JSON file
filename = "test"
s.SaveJSON(filename, folder = None)

# Load JSON file and adapt as preferred
stim = Stimulus.LoadFromJSON(filename, folder = None)
stim.shapes = GridPattern.RepeatAcrossElements([Rectangle, Ellipse])

stim.Show()

#%%
# s.boundingboxes
s.shapes
s.bordercolors
s.fillcolors
s.opacities
s.borderwidths
s.orientations
s.data
s.classlabels
s.idlabels
s.mirrorvalues
s.links

element_id = 0
boundingbox_value = (5,5)
s.set_element_boundingbox(element_id, boundingbox_value)
s.set_element_shape(element_id, shape_value)
s.remove_element(element_id)

# s.set_element_boundingboxes(boundingbox_value, element_id = None, n_changes = None)
s.set_element_shapes(shape_value, element_id = None, n_changes = None)
s.remove_elements(n_removals = 0, element_id = None)

s.Show()

#%%

s.swap_elements(n_swap_pairs = 1, swap_pairs = None)
s.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'opacities', 'mirrorvalues', 'links', 'classlabels', 'idlabels'])

s.swap_features(n_swap_pairs = 1, feature_dimensions = ['fillcolors'], swap_pairs = None)
s.swap_distinct_features(self, n_swap_pairs = 1, feature_dimensions = ['fillcolors'])

#%%

stim = Concentric(n_elements, x_margin = 20, y_margin = 20, size = None, 
                 background_color = "white", background_shape = None, 
                 stim_mask = None, stim_orientation = 0, stim_mirrorvalue = None, 
                 stim_link = None, stim_classlabel = None, stim_idlabel = None)

stim = Outline(n_elements, shape = 'Ellipse', shape_boundingbox = (150,150), 
                 x_margin = 20, y_margin = 20, size = None, 
                 background_color = "white", background_shape = None, 
                 stim_mask = None, stim_orientation = 0, stim_mirrorvalue = None, 
                 stim_link = None, stim_classlabel = None, stim_idlabel = None)

#%%

s.positions 

Positions(x, y, positiontype = None, positionparameters = {})

s.positions.x
s.positions.y

s.positions.GetPositions()
s.positions.SetPositionDeviations(element_id = [0], x_offset = None, y_offset = None)
s.positions.SetPositionJitter(axis = "xy", distribution = "normal", **kwargs)

CreateRectGrid(n_rows, n_cols, row_spacing = 50, col_spacing= 50)
CreateCustomPositions(x, y)
CreateSineGrid(n_rows, n_cols, row_spacing = 50, col_spacing = 50, A = 25, f = .1, axis = "xy")
CreateCircle(radius, n_elements, starting_point = "left")
CreateShape(n_elements, src = None, path = None, width = 300, height = 300)
CreateRandomPositions(n_elements, width = 300, height = 300, min_distance = 30, max_iterations = 10)

#%%

#Pattern

p = Pattern(pattern, patterntype = "", patterndirection = "", patternclass = "Pattern")

p #string
p + p # add
p.RepeatElements(n_repeats, max_elements = None)
p.RepeatPattern(n_repeats, max_elements = None)
p.RepeatElementsToSize(count)
p.RepeatPatternToSize(count)
p.AddNormalJitter(mu = 0, std = 1, axis = None)
p.AddUniformJitter(min_val = -1, max_val = 1, axis = None)
p.RandomizeOrder()

CreateGradientPattern(start_value, end_value, n_elements)
CreateColorRangeList(start_color, end_color, n_elements)
CreateNumberRangeList(start_number, end_number, n_elements)
Create2DGradient(x, y, n_elements)
Sequence(start, step)
LinearGradient(start, end, n_elements, invert = False)

#%%

#GridPattern
p = GridPattern(pattern, n_rows = 5, n_cols = 5, patterntype = None, patterndirection = None, patternclass = "GridPattern.")

#string
#generate()
p.AddNormalJitter(mu = 0, std = 1, axis = None)
p.AddUniformJitter(min_val = -1, max_val = 1, axis = None)

p.RandomizeAcrossElements()
p.RandomizeAcrossRows()
p.RandomizeAcrossColumns()
p.RandomizeAcrossLeftDiagonal()
p.RandomizeAcrossRightDiagonal()

ElementRepeatAcrossElements(GridPattern)
#generate()
AcrossColumns
AcrossRows
AcrossLeftDiagonal
AcrossRightDiagonal
AcrossLayers

RepeatAcrossElements
#generate()
AcrossColumns
AcrossRows
AcrossLeftDiagonal
AcrossRightDiagonal
AcrossLayers

MirrorAcrossElements
#generate()
AcrossColumns
AcrossRows
AcrossLeftDiagonal
AcrossRightDiagonal
AcrossLayers


GradientAcrossElements
#generate()
AcrossColumns
AcrossRows
AcrossLeftDiagonal
AcrossRightDiagonal
AcrossLayers


TiledGrid(source_grid, tile_multiplier)
get_dimensions
generate

TiledElementGrid(source_grid, tile_multiplier)
get_dimensions
generate

RandomPattern(pattern, n_rows = 5, n_cols = 5, patterntype = None, patterndirection = None, counts = None)
check_counts
generate

#%%
# Complexity

s.CalculateElementsN()
s.CalculateElementsLOCE(distinction_features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])

CalculateElementsLOC(self, distinction_features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])
CalculateElementsLOCI(self, distinction_features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])


# Order


GetPatterns(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])

GetPatternTypes(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])
GetPatternDirections(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])


CheckPatternCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])
CalculatePatternCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])

CheckPatternTypeCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])
CalculatePatternTypeCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])

CheckPatternDirectionCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])
CalculatePatternDirectionCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])

CalculatePatternDeviants(self, distinction_features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data'])
CalculatePositionDeviants(self)

#%%


['position', 'boundingbox', 'orientation' ,'bordercolor', 'borderwidth', 'fillcolor', 'opacity', 'classlabel', 'idlabel', 'mirrorvalue', 'link']
Ellipse()
Rectangle
Triangle()

Polygon(n_sides, name = None)
Polygon_
RegularPolygon(n_sides, name = None)
RegularPolygon_
Path(path, xsize, ysize, name = None)
Path_

PathSvg(src, name = None)
PathSvg_

Text(text, name = None)
Text_

Image(src, name = None)
Image_
FitImage(src, name = None)
FitImage_