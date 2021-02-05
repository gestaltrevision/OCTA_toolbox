# -*- coding: utf-8 -*-
"""
Example stimuli for FWO project Elisabeth Van der Hulst
05/02/2021
@author: Eline Van Geert
"""

from octa.Stimulus import Grid
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg
#from octa.measurements import Complexity
import random

#%%

########################################
### Een grid volgens kolom obv kleur ###
########################################

## Choose number of rows and number of columns
n_rows = 12
n_cols = 12

## background color: "None" or "lightgrey" or "white" for example
## row spacing is distance between midpoints of elements in horizontal direction
## column spacing is distance between midpoints of elements in vertical direction
## size argument makes the stimuli a fixed size, 
## but you could also choose for automatic determination of size by removing the size argument
stimulus = Grid(n_rows, n_cols, background_color = "None", row_spacing = 35, col_spacing = 35, size = (600,600))

## Determine size of elements in the stimulus
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(30,30)])

## Determine shapes used in the stimulus
## Example shapes: Ellipse, Rectangle, Triangle, Polygon(n_sides = 8), ...
stimulus.shapes = GridPattern.RepeatAcrossElements([Ellipse])

## Determine colors used in the stimulus
colors_to_use = ['#1b9fd8', '#006ca1', '#6dd6ff'] 
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(colors_to_use)

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
stimulus.SaveSVG("colcolor_pattern", folder = "stim_elisabeth")
stimulus.SavePNG("colcolor_pattern", folder = "stim_elisabeth")


#%%

#############################################
### Een grid met kolom kleur en rij shape ###
#############################################

## Choose number of rows and number of columns
n_rows = 12
n_cols = 12

## background color: "None" or "lightgrey" or "white" for example
## row spacing is distance between midpoints of elements in horizontal direction
## column spacing is distance between midpoints of elements in vertical direction
## size argument makes the stimuli a fixed size, 
## but you could also choose for automatic determination of size by removing the size argument
stimulus = Grid(n_rows, n_cols, background_color = "None", row_spacing = 35, col_spacing = 35, size = (600,600))

## Determine size of elements in the stimulus
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(30,30)])

## Determine shapes used in the stimulus
## Example shapes: Ellipse, Rectangle, Triangle, Polygon(n_sides = 8), ...
shapes_to_use = [Ellipse, Rectangle, Triangle]
stimulus.shapes = GridPattern.RepeatAcrossRows(shapes_to_use)

## Determine colors used in the stimulus
colors_to_use = ['#1b9fd8', '#006ca1', '#6dd6ff'] 
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(colors_to_use)

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
stimulus.SaveSVG("colcolor_rowshape_pattern", folder = "stim_elisabeth")
stimulus.SavePNG("colcolor_rowshape_pattern", folder = "stim_elisabeth")

#%%

###################################################
### Een grid met 1 kwadrant in een andere kleur ###
###################################################

## Choose number of rows and number of columns
n_rows = 12
n_cols = 12

## background color: "None" or "lightgrey" or "white" for example
## row spacing is distance between midpoints of elements in horizontal direction
## column spacing is distance between midpoints of elements in vertical direction
## size argument makes the stimuli a fixed size, 
## but you could also choose for automatic determination of size by removing the size argument
stimulus = Grid(n_rows, n_cols, background_color = "None", row_spacing = 35, col_spacing = 35, size = (600,600))

## Determine size of elements in the stimulus
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(30,30)])

## Determine shapes used in the stimulus
## Example shapes: Ellipse, Rectangle, Triangle, Polygon(n_sides = 8), ...
shapes_to_use = [Ellipse]
stimulus.shapes = GridPattern.RepeatAcrossRows(shapes_to_use)

## Determine colors used in the stimulus
colors_to_use = ['#1b9fd8', '#006ca1', '#6dd6ff'] 
tiled_grid = GridPattern.TiledElementGrid(GridPattern.RepeatAcrossElements([colors_to_use[0], colors_to_use[1], colors_to_use[1], colors_to_use[1]], 2 , 2),6)
stimulus.fillcolors = tiled_grid

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
stimulus.SaveSVG("quadrantcolor_pattern", folder = "stim_elisabeth")
stimulus.SavePNG("quadrantcolor_pattern", folder = "stim_elisabeth")


#%%

##################################################################################
### Een ongeordende grid en een bijbehorend grid die geordend is op 1 dimensie ###
##################################################################################

## Choose number of rows and number of columns
n_rows = 12
n_cols = 12

## background color: "None" or "lightgrey" or "white" for example
## row spacing is distance between midpoints of elements in horizontal direction
## column spacing is distance between midpoints of elements in vertical direction
## size argument makes the stimuli a fixed size, 
## but you could also choose for automatic determination of size by removing the size argument
stimulus = Grid(n_rows, n_cols, background_color = "None", row_spacing = 35, col_spacing = 35, size = (600,600))

## Determine size of elements in the stimulus
sizes_to_use = [(30,30)] #, (20,20), (25,25)
stimulus.bounding_boxes = GridPattern.RandomPattern(sizes_to_use)

## Determine shapes used in the stimulus
## Example shapes: Ellipse, Rectangle, Triangle, Polygon(n_sides = 8), ...
shapes_to_use = [Ellipse, Rectangle, Triangle]
stimulus.shapes = GridPattern.RandomPattern(shapes_to_use)

## Determine colors used in the stimulus
colors_to_use = ['#1b9fd8', '#006ca1', '#6dd6ff'] 
stimulus.fillcolors = GridPattern.RandomPattern(colors_to_use)

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
stimulus.SaveSVG("random_pattern", folder = "stim_elisabeth")
stimulus.SavePNG("random_pattern", folder = "stim_elisabeth")

# ORDERED VERSION

stimulus.fillcolors = GridPattern.RepeatAcrossRows(colors_to_use)
stimulus.Show()
stimulus.SaveSVG("ordered_random_pattern", folder = "stim_elisabeth")
stimulus.SavePNG("ordered_random_pattern", folder = "stim_elisabeth")


#%%

############################################################################################
### Een complexe grid en een bijbehorende grid waar de complexiteit weg is op 1 dimensie ###
############################################################################################

## Choose number of rows and number of columns
n_rows = 12
n_cols = 12

## background color: "None" or "lightgrey" or "white" for example
## row spacing is distance between midpoints of elements in horizontal direction
## column spacing is distance between midpoints of elements in vertical direction
## size argument makes the stimuli a fixed size, 
## but you could also choose for automatic determination of size by removing the size argument
stimulus = Grid(n_rows, n_cols, background_color = "None", row_spacing = 35, col_spacing = 35, size = (600,600))

## Determine size of elements in the stimulus
sizes_to_use = [(30,30),(20,20), (25,25)]
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows(sizes_to_use)

## Determine shapes used in the stimulus
## Example shapes: Ellipse, Rectangle, Triangle, Polygon(n_sides = 8), ...
shapes_to_use = [Ellipse, Rectangle, Triangle]
stimulus.shapes = GridPattern.RepeatAcrossColumns(shapes_to_use)

## Determine colors used in the stimulus
colors_to_use = ['#1b9fd8', '#006ca1', '#6dd6ff'] 
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(colors_to_use)

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
stimulus.SaveSVG("complex_pattern", folder = "stim_elisabeth")
stimulus.SavePNG("complex_pattern", folder = "stim_elisabeth")

# ORDERED VERSION
colors_to_use = ['#1b9fd8']
stimulus.fillcolors = GridPattern.RepeatAcrossRows(colors_to_use)
stimulus.Show()
stimulus.SaveSVG("simplified_complex_pattern", folder = "stim_elisabeth")
stimulus.SavePNG("simplified_complex_pattern", folder = "stim_elisabeth")