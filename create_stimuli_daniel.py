# -*- coding: utf-8 -*-
"""
Example stimuli Daniel
"""

import random
import numpy as np

from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Rectangle, Triangle, Ellipse


#### SUBGROUPS NOT POSSIBLE WHEN 8x8 or 16x16 and 3 values on dimension!!! ####
#### REPEATACROSSLEFTDIAGONAL AND REPEATACROSSRIGHTDIAGONAL only clearly directed when 3 values on dimension!!! ####
#### MIRRORACROSSLEFTDIAGONAL AND MIRRORACROSSRIGHTDIAGONAL only different from REPEAT... when 3 values on dimension!!! ####

seed = -620522398
nrows = [6] #[6,8,12,16,24]
ncols = nrows
xdist = [40,30,20,15,10]
ydist = xdist
stimsize = (330,330)
background_color = "white"

shapepattern = "MirrorAcrossRightDiagonal"
colorpattern = shapepattern
sizepattern = shapepattern

shapes = "[Rectangle, Triangle, Ellipse]"
shapes = "[Triangle, Ellipse]"

colors = "['#6dd6ff', '#1b9fd8', '#006ca1']"
colors = "['#1b9fd8', '#006ca1']"

sizes = ["[(20,20),(28,28),(36,36)]", "[(15,15),(21,21),(27,27)]", "[(10,10),(14,14),(18,18)]", "[(7.5,7.5),(10.5,10.5),(13.5,13.5)]", "[(5,5),(7,7),(9,9)]"]
sizes = ["[(20,20),(36,36)]", "[(15,15),(21,21),(27,27)]", "[(10,10),(14,14),(18,18)]", "[(7.5,7.5),(10.5,10.5),(13.5,13.5)]", "[(5,5),(7,7),(9,9)]"]

## DEFINE JITTER ##
jitter = ["nojitter"]
# "nojitter", "jitterrelativetoboundingbox", "jitterrelativetomeanboundingbox", "jitterrelativetocolumnrowspacing"
x_jitterratio = 0.30
y_jitterratio = x_jitterratio

## DEFINE ELEMENT SWITCHES ##
#n_switches = [[0,3,6], [0,4,8], [0,6,12], [0,8,16], [0,12,24]]
#n_switches = [[0,3,6], [0,5,11], [0,12,24], [0,21,43], [0,48,96]]
n_switches = [[0],[0],[0],[0],[0]]

for i in range(len(nrows)):   
    for jittertype in jitter:
        for nswitches in n_switches[i]:
        
            random.seed(seed)
              
            stimulus = Grid(n_rows = nrows[i], 
                            n_cols = ncols[i], 
                            row_spacing = xdist[i], 
                            col_spacing = ydist[i],
                            background_color = background_color, 
                            size = stimsize)
            
            if shapepattern == "Subgroups":
                
                stimulus.shapes = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(eval(shapes), len(eval(shapes)), len(eval(shapes))), int(stimulus.n_rows/len(eval(shapes))))
            
            elif shapepattern == "Checkerboard":
                
                if(len(eval(shapes)) < 3):
                    source_grid = GridPattern.RepeatAcrossElements(Pattern(eval(shapes) + eval(shapes)[::-1]), 2, 2)
               
                elif(len(eval(shapes)) >= 3):
                    source_grid = GridPattern.RepeatAcrossElements(Pattern(eval(shapes)).RepeatPatternToSize(count = 4), 2, 2)
                
                stimulus.shapes = GridPattern.TiledGrid(source_grid, (int(stimulus.n_rows/2),int(stimulus.n_cols/2)))
            
            elif shapepattern == "Outin":
                
                shapes_to_use = Pattern(eval(shapes)).RepeatPatternToSize(count = int(stimulus.n_rows / 2)) 
                # count = number of layers
                center_grid = GridPattern.RepeatAcrossElements(Pattern(shapes_to_use.pattern[0]), 2, 2)
                outer_layers = Pattern(shapes_to_use.pattern[1:])
                stimulus.shapes = GridPattern.LayeredGrid(center_grid, outer_layers)
   
    
            else:
                stimulus.shapes = eval("GridPattern." + shapepattern + "(" + shapes + ")")
                
                
            if colorpattern == "Subgroups":
                
                stimulus.fillcolors = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(eval(colors), len(eval(colors)), len(eval(colors))), int(stimulus.n_rows/len(eval(colors))))
            
            elif colorpattern == "Checkerboard":
                
                if(len(eval(colors)) < 3):
                    source_grid = GridPattern.RepeatAcrossElements(Pattern(eval(colors) + eval(colors)[::-1]), 2, 2)
               
                elif(len(eval(colors)) >= 3):
                    source_grid = GridPattern.RepeatAcrossElements(Pattern(eval(colors)).RepeatPatternToSize(count = 4), 2, 2)
                
                stimulus.fillcolors = GridPattern.TiledGrid(source_grid, (int(stimulus.n_rows/2),int(stimulus.n_cols/2)))
                
            elif colorpattern == "Outin":
                
                colors_to_use = Pattern(eval(colors)).RepeatPatternToSize(count = int(stimulus.n_rows / 2)) 
                # count = number of layers
                center_grid = GridPattern.RepeatAcrossElements(Pattern(colors_to_use.pattern[0]), 2, 2)
                outer_layers = Pattern(colors_to_use.pattern[1:])
                stimulus.fillcolors = GridPattern.LayeredGrid(center_grid, outer_layers)
                
            else:
                stimulus.fillcolors = eval("GridPattern." + colorpattern + "(" + colors + ")")
 
            if sizepattern == "Subgroups":
                
                stimulus.boundingboxes = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(eval(sizes[i]), len(eval(sizes[i])), len(eval(sizes[i]))), int(stimulus.n_rows/len(eval(sizes[i]))))
    
            elif sizepattern == "Checkerboard":
                
                if(len(eval(sizes[i])) < 3):
                    source_grid = GridPattern.RepeatAcrossElements(Pattern(eval(sizes[i]) + eval(sizes[i])[::-1]), 2, 2)
               
                elif(len(eval(sizes[i])) >= 3):
                    source_grid = GridPattern.RepeatAcrossElements(Pattern(eval(sizes[i])).RepeatPatternToSize(count = 4), 2, 2)
                
                stimulus.boundingboxes = GridPattern.TiledGrid(source_grid, (int(stimulus.n_rows/2),int(stimulus.n_cols/2)))
            
            elif sizepattern == "Outin":
                
                sizes_to_use = Pattern(eval(sizes[i])).RepeatPatternToSize(count = int(stimulus.n_rows / 2)) 
                # count = number of layers
                center_grid = GridPattern.RepeatAcrossElements(Pattern(sizes_to_use.pattern[0]), 2, 2)
                outer_layers = Pattern(sizes_to_use.pattern[1:])
                stimulus.boundingboxes = GridPattern.LayeredGrid(center_grid, outer_layers)

            else:
                stimulus.boundingboxes = eval("GridPattern." + sizepattern + "(" + sizes[i] + ")")
            
            ### PATTERNS FOR COLORS ###  
#            
#            if(color_pattern == "MirrorAcrossLeftDiagonal"):
#                stimulus_1.fillcolors = GridPattern.MirrorAcrossLeftDiagonal(colors_1)
#               
#            elif(color_pattern == "MirrorAcrossRightDiagonal"):
#                stimulus_1.fillcolors = GridPattern.MirrorAcrossRightDiagonal(colors_1)                    
#            
#            elif(color_pattern == "RepeatAcrossRows"):
#                stimulus_1.fillcolors = GridPattern.RepeatAcrossColumns(Pattern(colors_1).RepeatElements(int(stimulus_1.n_rows/len(colors_1))))
#                
#            elif(color_pattern == "RepeatAcrossColumns"):
#                stimulus_1.fillcolors = GridPattern.RepeatAcrossRows(Pattern(colors_1).RepeatElements(int(stimulus_1.n_cols/len(colors_1))))
#            
#            elif(color_pattern == "AlternateRows"):
#                stimulus_1.fillcolors = GridPattern.RepeatAcrossColumns(colors_1)    
#            
#            elif(color_pattern == "AlternateColumns"):
#                stimulus_1.fillcolors = GridPattern.RepeatAcrossRows(colors_1) 
#            
#            elif(color_pattern == "MirrorAcrossRows"):
#                stimulus_1.fillcolors = GridPattern.MirrorAcrossRows(colors_1)
#            
#            elif(color_pattern == "MirrorAcrossColumns"):
#                stimulus_1.fillcolors = GridPattern.MirrorAcrossColumns(colors_1)
#           
#            elif(color_pattern == "Subgroups"):
#                stimulus_1.fillcolors = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(colors_1, len(colors_1), len(colors_1)), int(stimulus_1.n_rows/len(colors_1)))
#            
#            elif(color_pattern == "Checkerboard"):
#        
#                if(len(colors_1) < 3):
#                    source_grid_colors = GridPattern.RepeatAcrossElements(Pattern(colors_1 + colors_1[::-1]), 2, 2)
#               
#                elif(len(colors_1) >= 3):
#                    source_grid_colors = GridPattern.RepeatAcrossElements(Pattern(colors_1).RepeatPatternToSize(count = 4), 2, 2)
#                    stimulus_1.fillcolors = GridPattern.TiledGrid(source_grid_colors, (int(stimulus_1.n_rows/2),int(stimulus_1.n_cols/2)))
#            
            
#            ### PATTERNS FOR SHAPES ###
#            
#            if(shape_pattern == "MirrorAcrossLeftDiagonal"):
#                stimulus_1.shapes = GridPattern.MirrorAcrossLeftDiagonal(shapes_1)
#               
#            elif(shape_pattern == "MirrorAcrossRightDiagonal"):
#                stimulus_1.shapes = GridPattern.MirrorAcrossRightDiagonal(shapes_1)
#              
#            elif(shape_pattern == "RepeatAcrossRows"):
#                stimulus_1.shapes = GridPattern.RepeatAcrossColumns(Pattern(shapes_1).RepeatElements(int(stimulus_1.n_rows/len(shapes_1))))
#                
#            elif(shape_pattern == "RepeatAcrossColumns"):
#                stimulus_1.shapes = GridPattern.RepeatAcrossRows(Pattern(shapes_1).RepeatElements(int(stimulus_1.n_cols/len(shapes_1))))
#               
#            elif(shape_pattern == "AlternateRows"):
#                stimulus_1.shapes = GridPattern.RepeatAcrossColumns(shapes_1)
#               
#            elif(shape_pattern == "AlternateColumns"):
#                stimulus_1.shapes = GridPattern.RepeatAcrossRows(shapes_1)
#               
#            elif(shape_pattern == "MirrorAcrossRows"):
#                stimulus_1.shapes = GridPattern.MirrorAcrossRows(shapes_1)
#               
#            elif(shape_pattern == "MirrorAcrossColumns"):
#                stimulus_1.shapes = GridPattern.MirrorAcrossColumns(shapes_1)
#               
#            elif(shape_pattern == "Subgroups"):
#                stimulus_1.shapes = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(shapes_1, len(shapes_1), len(shapes_1)), int(stimulus_1.n_rows/len(shapes_1)))   
#                
#            elif(shape_pattern == "Checkerboard"):
#                if(len(shapes_1) < 3):
#                    source_grid_shapes = GridPattern.RepeatAcrossElements(Pattern(shapes_1 + shapes_1[::-1]), 2, 2)
#                
#                elif(len(shapes_1) >= 3):
#                    source_grid_shapes = GridPattern.RepeatAcrossElements(Pattern(shapes_1).RepeatPatternToSize(count = 4), 2, 2)
#                    stimulus_1.shapes = GridPattern.TiledGrid(source_grid_shapes, (int(stimulus_1.n_rows/2),int(stimulus_1.n_cols/2)))
#              
#            ### PATTERNS FOR SIZES ###         
#              
#            if(size_pattern == "MirrorAcrossLeftDiagonal"):
#                stimulus_1.boundingboxes = GridPattern.MirrorAcrossLeftDiagonal(sizes_1)
#                
#            elif(size_pattern == "MirrorAcrossRightDiagonal"):
#                stimulus_1.boundingboxes = GridPattern.MirrorAcrossRightDiagonal(sizes_1)
#              
#            elif(size_pattern == "RepeatAcrossRows"):
#                stimulus_1.boundingboxes = GridPattern.RepeatAcrossColumns(Pattern(sizes_1).RepeatElements(int(stimulus_1.n_rows/len(sizes_1))))
#                 
#            elif(size_pattern == "RepeatAcrossColumns"):
#                stimulus_1.boundingboxes = GridPattern.RepeatAcrossRows(Pattern(sizes_1).RepeatElements(int(stimulus_1.n_cols/len(sizes_1))))
#                
#            elif(size_pattern == "AlternateRows"):
#                stimulus_1.boundingboxes = GridPattern.RepeatAcrossColumns(sizes_1)
#                
#            elif(size_pattern == "AlternateColumns"):
#                stimulus_1.boundingboxes = GridPattern.RepeatAcrossRows(sizes_1)
#                
#            elif(size_pattern == "MirrorAcrossRows"):
#                stimulus_1.boundingboxes = GridPattern.MirrorAcrossRows(sizes_1)
#                
#            elif(size_pattern == "MirrorAcrossColumns"):
#                stimulus_1.boundingboxes = GridPattern.MirrorAcrossColumns(sizes_1)
#                
#            elif(size_pattern == "Subgroups"):
#                stimulus_1.boundingboxes = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal(sizes_1, len(sizes_1), len(sizes_1)), int(stimulus_1.n_rows/len(sizes_1)))
#                
#            elif(size_pattern == "Checkerboard"):
#                if(len(sizes_1) < 3):
#                    source_grid_sizes = GridPattern.RepeatAcrossElements(Pattern(sizes_1 + sizes_1[::-1]), 2, 2)
#               
#                elif(len(sizes_1) >= 3):
#                    source_grid_sizes = GridPattern.RepeatAcrossElements(Pattern(sizes_1).RepeatPatternToSize(count = 4), 2, 2)
#                stimulus_1.boundingboxes = GridPattern.TiledGrid(source_grid_sizes, (int(stimulus_1.n_rows/2),int(stimulus_1.n_cols/2)))
#                                 

            
            ## JITTER ##               
            if jittertype == "jitterrelativetoboundingbox":
                x_boundingboxes =  [i[0] for i in stimulus.boundingboxes]
                x_maxjitter = [i*x_jitterratio for i in x_boundingboxes]
                y_boundingboxes =  [i[1] for i in stimulus.boundingboxes]
                y_maxjitter = [i*y_jitterratio for i in y_boundingboxes]

                x_jitter = [random.uniform(-x_maxjitter[_], x_maxjitter[_]) for _ in range(len(stimulus.positions.x))]
                y_jitter = [random.uniform(-y_maxjitter[_], y_maxjitter[_]) for _ in range(len(stimulus.positions.y))]
                new_x = [stimulus.positions.x[i] + x_jitter[i] for i in range(len(stimulus.positions.x))]
                new_y = [stimulus.positions.y[i] + y_jitter[i] for i in range(len(stimulus.positions.y))]
                stimulus.positions = Positions.CreateCustomPositions(x = new_x, y = new_y)
                
            elif jittertype == "jitterrelativetomeanboundingbox":
                x_boundingboxes =  [i[0] for i in stimulus.boundingboxes]
                x_maxjitter = x_jitterratio*np.mean(x_boundingboxes)
                y_boundingboxes =  [i[1] for i in stimulus.boundingboxes]
                y_maxjitter = y_jitterratio*np.mean(y_boundingboxes)
                
                x_jitter = [random.uniform(-x_maxjitter, x_maxjitter) for _ in range(len(stimulus.positions.x))]
                y_jitter = [random.uniform(-y_maxjitter, y_maxjitter) for _ in range(len(stimulus.positions.y))]
                new_x = [stimulus.positions.x[i] + x_jitter[i] for i in range(len(stimulus.positions.x))]
                new_y = [stimulus.positions.y[i] + y_jitter[i] for i in range(len(stimulus.positions.y))]
                stimulus.positions = Positions.CreateCustomPositions(x = new_x, y = new_y)
                
            elif jittertype == "jitterrelativetocolumnrowspacing":
                x_maxjitter = x_jitterratio*stimulus.row_spacing
                y_maxjitter = y_jitterratio*stimulus.col_spacing
                
                x_jitter = [random.uniform(-x_maxjitter, x_maxjitter) for _ in range(len(stimulus.positions.x))]
                y_jitter = [random.uniform(-y_maxjitter, y_maxjitter) for _ in range(len(stimulus.positions.y))]
                new_x = [stimulus.positions.x[i] + x_jitter[i] for i in range(len(stimulus.positions.x))]
                new_y = [stimulus.positions.y[i] + y_jitter[i] for i in range(len(stimulus.positions.y))]
                stimulus.positions = Positions.CreateCustomPositions(x = new_x, y = new_y)
            
            ## SWITCHES ##      
            stimulus.swap_distinct_elements(n_swap_pairs = nswitches, distinction_features = ["fillcolors", "shapes", "boundingboxes"])
#                newpresentationorder = stimulus._element_presentation_order

            ## SHOW STIMULUS / SAVE STIMULUS ##
            stimulus.Show()
#            print("\nxmaxjitter:\n", x_maxjitter, "\n\n ymaxjitter:\n", y_maxjitter) 
            stimname = str(nswitches) + "switches_" + str(nrows[i]) + "by" + str(ncols[i])
            stimulus.SaveSVG(stimname, folder = "switchexamples_daniel")