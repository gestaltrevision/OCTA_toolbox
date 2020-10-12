# -*- coding: utf-8 -*-
"""
@author: Eline Van Geert
"""

### IMPORT LIBRARIES ###
from octa.Stimulus import Grid
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle
from octa.measurements import Complexity

import random 

### SET SEED ###
random.seed(21)

### DEFINE COMPLEXITY LEVELS ###
complexity_levels = [1,2,3]

### DEFINE ORDER TYPE ###
patterns = ["Subgroups"]#["RepeatAcrossRows", "RepeatAcrossColumns", "AlternateRows", "AlternateColumns", "MirrorAcrossRows", "MirrorAcrossColumns", "Subgroups", "Outin", "Checkerboard"]
# Extra pattern: Frame (only possible with 2 values, not with 3)

### DEFINE NUMBER OF SWITCHES ###
n_switches = [0]#[0,1,2,3,4,5,6]
            

for shape_n in complexity_levels:
    for size_n in complexity_levels:
        for color_n in complexity_levels:
            for pattern in patterns:
                for switch_n in n_switches:

                    ### DEFINE VALUES PER STIMULUS DIMENSION ###
                    shapes = [Ellipse, Rectangle, Triangle]
                    random.shuffle(shapes)
                    
                    sizes = [(20,20),(28,28),(36,36)]
                    random.shuffle(sizes)
                    
                    colors = ['#6dd6ff', '#1b9fd8', '#006ca1'] 
                    random.shuffle(colors)
                    
                    ### DEFINE COMPLEXITY LEVELS ###
                    
                    n_shapes_1 = shape_n
                    n_sizes_1 = size_n
                    n_colors_1 = color_n
                    
                    complexity_1 = [n_shapes_1, n_sizes_1, n_colors_1]
                    
                    shapes_1 = shapes[0:n_shapes_1]
                    sizes_1 = sizes[0:n_sizes_1]
                    colors_1 = colors[0:n_colors_1]
                    
                    ### DEFINE FIXED STIMULUS ATTRIBUTES ###
                    n_rows = 6
                    n_cols = 6
                    
                    stimulus_1 = Grid(6,6, row_spacing = 40, col_spacing = 40, size = (330,330))
                    
                    
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
                        
                    
                    ####################################
                    ### INSERT DEVIANTS FROM PATTERN ###
                    ####################################
                    
                    ### SWITCH ELEMENTS ###
                    if(complexity_1 != [1,1,1]):
                        element_switches = switch_n
                    else:
                        element_switches = 0
                    
                    stimulus_1.swap_distinct_elements(element_switches, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors'])
                    
                    stimulus_1.Show()
                    
                    LOCI_1 = 0
                    for i in complexity_1: 
                        if(i > 1): 
                            LOCI_1 += 1
                                        
                    print("\n\nLOCI:\t", LOCI_1)
                    print("LOC:\t", sum(complexity_1))
                    print("LOCE:\t", Complexity.CalculateElementsLOCE(stimulus_1, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors']))
