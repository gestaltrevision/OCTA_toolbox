# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:57:21 2020

@author: u0090621
"""
from octa.Stimulus import Grid
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle
from octa.measurements import LOCE

import random 

shapes = [Ellipse, Rectangle, Triangle]
random.shuffle(shapes)

sizes = [(20,20),(28,28),(36,36)]
random.shuffle(sizes)

#colors = ['#1C3D61','#5E78A1','#A0BAE6']
colors = ['#6dd6ff', '#1b9fd8', '#006ca1'] 
random.shuffle(colors)

# DEFINE COMPLEXITY FOR STIMULUS 1 and 2
more = random.choice([2,3])

n_shapes_1 = random.choice([1,more])
n_sizes_1 = random.choice([1,more])
n_colors_1 = random.choice([1,more])
complexity_1 = [n_shapes_1, n_sizes_1, n_colors_1]

complexity_2 = complexity_1
while complexity_2 == complexity_1:
    n_shapes_2 = random.choice([1,more])
    n_sizes_2 = random.choice([1,more])
    n_colors_2 = random.choice([1,more])
    complexity_2 = [n_shapes_2, n_sizes_2, n_colors_2]

shapes_1 = shapes[0:n_shapes_1]
sizes_1 = sizes[0:n_sizes_1]
colors_1 = colors[0:n_colors_1]

shapes_2 = shapes[0:n_shapes_2]
sizes_2 = sizes[0:n_sizes_2]
colors_2 = colors[0:n_colors_2]

n_rows = 6
n_cols = 6

stimulus_1 = Grid(6,6, row_spacing = 40, col_spacing = 40)
stimulus_2 = Grid(6,6, row_spacing = 40, col_spacing = 40)

# DEFINE ORDER

pattern = random.choice(["RepeatAcrossRows", "RepeatAcrossColumns", "AlternateRows", "AlternateColumns", "MirrorAcrossRows", "MirrorAcrossColumns", "Subgroups", "Outin", "Checkerboard"])
# Extra pattern: Frame (only possible with 2 values, not with 3)

if(pattern == "RepeatAcrossRows"):
    stimulus_1.shapes = GridPattern.RepeatAcrossColumns(Pattern(shapes_1).RepeatElements(int(stimulus_1.n_rows/len(shapes_1))))
    stimulus_1.bounding_boxes = GridPattern.RepeatAcrossColumns(Pattern(sizes_1).RepeatElements(int(stimulus_1.n_rows/len(sizes_1))))
    stimulus_1.fillcolors = GridPattern.RepeatAcrossColumns(Pattern(colors_1).RepeatElements(int(stimulus_1.n_rows/len(colors_1))))
elif(pattern == "RepeatAcrossColumns"):
    stimulus_1.shapes = GridPattern.RepeatAcrossRows(Pattern(shapes_1).RepeatElements(int(stimulus_1.n_cols/len(shapes_1))))
    stimulus_1.bounding_boxes = GridPattern.RepeatAcrossRows(Pattern(sizes_1).RepeatElements(int(stimulus_1.n_cols/len(sizes_1))))
    stimulus_1.fillcolors = GridPattern.RepeatAcrossRows(Pattern(colors_1).RepeatElements(int(stimulus_1.n_cols/len(colors_1))))
elif(pattern == "AlternateRows"):
    stimulus_1.shapes = GridPattern.RepeatAcrossColumns(shapes_1)
    stimulus_1.bounding_boxes = GridPattern.RepeatAcrossColumns(sizes_1)
    stimulus_1.fillcolors = GridPattern.RepeatAcrossColumns(colors_1)    
elif(pattern == "AlternateColumns"):
    stimulus_1.shapes = GridPattern.RepeatAcrossRows(shapes_1)
    stimulus_1.bounding_boxes = GridPattern.RepeatAcrossRows(sizes_1)
    stimulus_1.fillcolors = GridPattern.RepeatAcrossRows(colors_1) 
elif(pattern == "MirrorAcrossRows"):
    stimulus_1.shapes = GridPattern.MirrorAcrossRows(shapes_1)
    stimulus_1.bounding_boxes = GridPattern.MirrorAcrossRows(sizes_1)
    stimulus_1.fillcolors = GridPattern.MirrorAcrossRows(colors_1)
elif(pattern == "MirrorAcrossColumns"):
    stimulus_1.shapes = GridPattern.MirrorAcrossColumns(shapes_1)
    stimulus_1.bounding_boxes = GridPattern.MirrorAcrossColumns(sizes_1)
    stimulus_1.fillcolors = GridPattern.MirrorAcrossColumns(colors_1)
elif(pattern == "Subgroups"):
    stimulus_1.shapes = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(shapes_1, len(shapes_1), len(shapes_1)), int(stimulus_1.n_rows/len(shapes_1)))   
    stimulus_1.bounding_boxes = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(sizes_1, len(sizes_1), len(sizes_1)), int(stimulus_1.n_rows/len(sizes_1)))
    stimulus_1.fillcolors = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(colors_1, len(colors_1), len(colors_1)), int(stimulus_1.n_rows/len(colors_1)))
elif(pattern == "Checkerboard"):
    if(len(shapes_1) < 3):
        source_grid_shapes = GridPattern.RepeatAcrossElements(Pattern(shapes_1 + shapes_1[::-1]), 2, 2)
    elif(len(shapes_1) >= 3):
        source_grid_shapes = GridPattern.RepeatAcrossElements(Pattern(shapes_1).RepeatPatternToSize(count = 4), 2, 2)
    stimulus_1.shapes = GridPattern.TiledGrid(source_grid_shapes, (int(stimulus_1.n_rows/2),int(stimulus_1.n_cols/2)))
    if(len(sizes_1) < 3):
        source_grid_sizes = GridPattern.RepeatAcrossElements(Pattern(sizes_1 + sizes_1[::-1]), 2, 2)
    elif(len(sizes_1) >= 3):
        source_grid_sizes = GridPattern.RepeatAcrossElements(Pattern(sizes_1).RepeatPatternToSize(count = 4), 2, 2)
    stimulus_1.bounding_boxes = GridPattern.TiledGrid(source_grid_sizes, (int(stimulus_1.n_rows/2),int(stimulus_1.n_cols/2)))
    if(len(colors_1) < 3):
        source_grid_colors = GridPattern.RepeatAcrossElements(Pattern(colors_1 + colors_1[::-1]), 2, 2)
    elif(len(colors_1) >= 3):
        source_grid_colors = GridPattern.RepeatAcrossElements(Pattern(colors_1).RepeatPatternToSize(count = 4), 2, 2)
    stimulus_1.fillcolors = GridPattern.TiledGrid(source_grid_colors, (int(stimulus_1.n_rows/2),int(stimulus_1.n_cols/2)))
elif(pattern == "Outin"):
    shapes_1 = Pattern(shapes_1).RepeatPatternToSize(count = 3) # count = number of layers
    center_grid_shapes = GridPattern.RepeatAcrossElements(Pattern(shapes_1.pattern[0]), 2, 2)
    outer_layers_shapes = Pattern(shapes_1.pattern[1:])
    stimulus_1.shapes = GridPattern.LayeredGrid(center_grid_shapes, outer_layers_shapes)
    sizes_1 = Pattern(sizes_1).RepeatPatternToSize(count = 3) # count = number of layers
    center_grid_sizes = GridPattern.RepeatAcrossElements(Pattern(sizes_1.pattern[0]), 2, 2)
    outer_layers_sizes = Pattern(sizes_1.pattern[1:])
    stimulus_1.bounding_boxes = GridPattern.LayeredGrid(center_grid_sizes, outer_layers_sizes)
    colors_1 = Pattern(colors_1).RepeatPatternToSize(count = 3) # count = number of layers
    center_grid_colors = GridPattern.RepeatAcrossElements(Pattern(colors_1.pattern[0]), 2, 2)
    outer_layers_colors = Pattern(colors_1.pattern[1:])
    stimulus_1.fillcolors = GridPattern.LayeredGrid(center_grid_colors, outer_layers_colors)
elif(pattern == "Frame"):
    shapes_1 = Pattern(shapes_1).RepeatPatternToSize(count = 2) # count = number of layers
    center_grid_shapes = GridPattern.RepeatAcrossElements(Pattern(shapes_1.pattern[0]), 2, 2)
    outer_layers_shapes = Pattern(shapes_1.pattern)
    stimulus_1.shapes = GridPattern.LayeredGrid(center_grid_shapes, outer_layers_shapes)
    sizes_1 = Pattern(sizes_1).RepeatPatternToSize(count = 2) # count = number of layers
    center_grid_sizes = GridPattern.RepeatAcrossElements(Pattern(sizes_1.pattern[0]), 2, 2)
    outer_layers_sizes = Pattern(sizes_1.pattern)
    stimulus_1.bounding_boxes = GridPattern.LayeredGrid(center_grid_sizes, outer_layers_sizes)
    colors_1 = Pattern(colors_1).RepeatPatternToSize(count = 2) # count = number of layers
    center_grid_colors = GridPattern.RepeatAcrossElements(Pattern(colors_1.pattern[0]), 2, 2)
    outer_layers_colors = Pattern(colors_1.pattern)
    stimulus_1.fillcolors = GridPattern.LayeredGrid(center_grid_colors, outer_layers_colors)
    
if(pattern == "RepeatAcrossRows"):
    stimulus_2.shapes = GridPattern.RepeatAcrossColumns(Pattern(shapes_2).RepeatElements(int(stimulus_2.n_rows/len(shapes_2))))
    stimulus_2.bounding_boxes = GridPattern.RepeatAcrossColumns(Pattern(sizes_2).RepeatElements(int(stimulus_2.n_rows/len(sizes_2))))
    stimulus_2.fillcolors = GridPattern.RepeatAcrossColumns(Pattern(colors_2).RepeatElements(int(stimulus_2.n_rows/len(colors_2))))
elif(pattern == "RepeatAcrossColumns"):
    stimulus_2.shapes = GridPattern.RepeatAcrossRows(Pattern(shapes_2).RepeatElements(int(stimulus_2.n_cols/len(shapes_2))))
    stimulus_2.bounding_boxes = GridPattern.RepeatAcrossRows(Pattern(sizes_2).RepeatElements(int(stimulus_2.n_cols/len(sizes_2))))
    stimulus_2.fillcolors = GridPattern.RepeatAcrossRows(Pattern(colors_2).RepeatElements(int(stimulus_2.n_cols/len(colors_2))))
elif(pattern == "AlternateRows"):
    stimulus_2.shapes = GridPattern.RepeatAcrossColumns(shapes_2)
    stimulus_2.bounding_boxes = GridPattern.RepeatAcrossColumns(sizes_2)
    stimulus_2.fillcolors = GridPattern.RepeatAcrossColumns(colors_2)    
elif(pattern == "AlternateColumns"):
    stimulus_2.shapes = GridPattern.RepeatAcrossRows(shapes_2)
    stimulus_2.bounding_boxes = GridPattern.RepeatAcrossRows(sizes_2)
    stimulus_2.fillcolors = GridPattern.RepeatAcrossRows(colors_2) 
elif(pattern == "MirrorAcrossRows"):
    stimulus_2.shapes = GridPattern.MirrorAcrossRows(shapes_2)
    stimulus_2.bounding_boxes = GridPattern.MirrorAcrossRows(sizes_2)
    stimulus_2.fillcolors = GridPattern.MirrorAcrossRows(colors_2)
elif(pattern == "MirrorAcrossColumns"):
    stimulus_2.shapes = GridPattern.MirrorAcrossColumns(shapes_2)
    stimulus_2.bounding_boxes = GridPattern.MirrorAcrossColumns(sizes_2)
    stimulus_2.fillcolors = GridPattern.MirrorAcrossColumns(colors_2)
elif(pattern == "Subgroups"):
    stimulus_2.shapes = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(shapes_2, len(shapes_2), len(shapes_2)), int(stimulus_2.n_rows/len(shapes_2)))   
    stimulus_2.bounding_boxes = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(sizes_2, len(sizes_2), len(sizes_2)), int(stimulus_2.n_rows/len(sizes_2)))
    stimulus_2.fillcolors = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(colors_2, len(colors_2), len(colors_2)), int(stimulus_2.n_rows/len(colors_2)))
elif(pattern == "Checkerboard"):
    if(len(shapes_2) < 3):
        source_grid_shapes = GridPattern.RepeatAcrossElements(Pattern(shapes_2 + shapes_2[::-1]), 2, 2)
    elif(len(shapes_2) >= 3):
        source_grid_shapes = GridPattern.RepeatAcrossElements(Pattern(shapes_2).RepeatPatternToSize(count = 4), 2, 2)
    stimulus_2.shapes = GridPattern.TiledGrid(source_grid_shapes, (int(stimulus_2.n_rows/2),int(stimulus_2.n_cols/2)))
    if(len(sizes_2) < 3):
        source_grid_sizes = GridPattern.RepeatAcrossElements(Pattern(sizes_2 + sizes_2[::-1]), 2, 2)
    elif(len(sizes_2) >= 3):
        source_grid_sizes = GridPattern.RepeatAcrossElements(Pattern(sizes_2).RepeatPatternToSize(count = 4), 2, 2)
    stimulus_2.bounding_boxes = GridPattern.TiledGrid(source_grid_sizes, (int(stimulus_2.n_rows/2),int(stimulus_2.n_cols/2)))
    if(len(colors_2) < 3):
        source_grid_colors = GridPattern.RepeatAcrossElements(Pattern(colors_2 + colors_2[::-1]), 2, 2)
    elif(len(colors_2) >= 3):
        source_grid_colors = GridPattern.RepeatAcrossElements(Pattern(colors_2).RepeatPatternToSize(count = 4), 2, 2)
    stimulus_2.fillcolors = GridPattern.TiledGrid(source_grid_colors, (int(stimulus_2.n_rows/2),int(stimulus_2.n_cols/2)))
elif(pattern == "Outin"):
    shapes_2 = Pattern(shapes_2).RepeatPatternToSize(count = 3) # count = number of layers
    center_grid_shapes = GridPattern.RepeatAcrossElements(Pattern(shapes_2.pattern[0]), 2, 2)
    outer_layers_shapes = Pattern(shapes_2.pattern[1:])
    stimulus_2.shapes = GridPattern.LayeredGrid(center_grid_shapes, outer_layers_shapes)
    sizes_2 = Pattern(sizes_2).RepeatPatternToSize(count = 3) # count = number of layers
    center_grid_sizes = GridPattern.RepeatAcrossElements(Pattern(sizes_2.pattern[0]), 2, 2)
    outer_layers_sizes = Pattern(sizes_2.pattern[1:])
    stimulus_2.bounding_boxes = GridPattern.LayeredGrid(center_grid_sizes, outer_layers_sizes)
    colors_2 = Pattern(colors_2).RepeatPatternToSize(count = 3) # count = number of layers
    center_grid_colors = GridPattern.RepeatAcrossElements(Pattern(colors_2.pattern[0]), 2, 2)
    outer_layers_colors = Pattern(colors_2.pattern[1:])
    stimulus_2.fillcolors = GridPattern.LayeredGrid(center_grid_colors, outer_layers_colors)
elif(pattern == "Frame"):
    shapes_2 = Pattern(shapes_2).RepeatPatternToSize(count = 2) # count = number of layers
    center_grid_shapes = GridPattern.RepeatAcrossElements(Pattern(shapes_2.pattern[0]), 2, 2)
    outer_layers_shapes = Pattern(shapes_2.pattern)
    stimulus_2.shapes = GridPattern.LayeredGrid(center_grid_shapes, outer_layers_shapes)
    sizes_2 = Pattern(sizes_2).RepeatPatternToSize(count = 2) # count = number of layers
    center_grid_sizes = GridPattern.RepeatAcrossElements(Pattern(sizes_2.pattern[0]), 2, 2)
    outer_layers_sizes = Pattern(sizes_2.pattern)
    stimulus_2.bounding_boxes = GridPattern.LayeredGrid(center_grid_sizes, outer_layers_sizes)
    colors_2 = Pattern(colors_2).RepeatPatternToSize(count = 2) # count = number of layers
    center_grid_colors = GridPattern.RepeatAcrossElements(Pattern(colors_2.pattern[0]), 2, 2)
    outer_layers_colors = Pattern(colors_2.pattern)
    stimulus_2.fillcolors = GridPattern.LayeredGrid(center_grid_colors, outer_layers_colors)
    

####################################
### INSERT DEVIANTS FROM PATTERN ###
####################################

### SWITCH ELEMENTS ###
if((complexity_1 != [1,1,1]) & (complexity_2 != [1,1,1])):
    element_switches = random.choice([0,1,2])
else:
    element_switches = 0

stimulus_1.swap_distinct_elements(element_switches, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors'])
newpresentationorder_1 = stimulus_1._element_presentation_order
stimulus_2._element_presentation_order = newpresentationorder_1

stimulus_1.Show()
stimulus_2.Show()


LOCI_1 = 0
for i in complexity_1: 
    if(i > 1): 
        LOCI_1 += 1
        
LOCI_2 = 0
for i in complexity_2: 
    if(i > 1): 
        LOCI_2 += 1

print("\n\nLOCI:\t", LOCI_1, " vs. ", LOCI_2)
print("LOC:\t", sum(complexity_1), " vs. ", sum(complexity_2))
print("LOCE:\t", LOCE.CalculateElementsLOCE(stimulus_1), " vs. ", LOCE.CalculateElementsLOCE(stimulus_2))
