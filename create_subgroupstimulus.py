# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

from octa.Stimulus import Grid, Stimulus
from octa.patterns import GridPattern, Pattern
from octa.shapes import Rectangle, Triangle


seed = -620522398
nrows = 6
ncols = 6
xdist = 40
ydist = 40
background_color = "white"
pattern = "Subgroups"

random.seed(seed)
  
stimulus = Grid(n_rows = nrows, 
                n_cols = ncols, 
                row_spacing = xdist, 
                col_spacing = ydist,
                background_color = background_color, 
                size = (330,330))
  
#  if(parameters$pattern %in% c("MirrorAcrossRows", "MirrorAcrossColumns")):
#      stimulus.shapes = GridPattern.", parameters$pattern, "([", paste(parameters$shape, collapse = ", "])
#    py_run_string(paste0("stimulus.fillcolors = GridPattern.", parameters$pattern, "([", paste(parameters$color, collapse = ", "), "])"))
#    py_run_string(paste0("stimulus.bounding_boxes = GridPattern.", parameters$pattern, "([", paste(parameters$size, collapse = ", "), "])"))
#  } else if(parameters$pattern == "AlternateRows"){
#    
#    py_run_string(paste0("stimulus.shapes = GridPattern.", "RepeatAcrossRows", "([", paste(parameters$shape, collapse = ", "), "])"))
#    py_run_string(paste0("stimulus.fillcolors = GridPattern.", "RepeatAcrossRows", "([", paste(parameters$color, collapse = ", "), "])"))
#    py_run_string(paste0("stimulus.bounding_boxes = GridPattern.", "RepeatAcrossRows", "([", paste(parameters$size, collapse = ", "), "])"))
#  } else if(parameters$pattern == "AlternateColumns"){
#    
#    py_run_string(paste0("stimulus.shapes = GridPattern.", "RepeatAcrossColumns", "([", paste(parameters$shape, collapse = ", "), "])"))
#    py_run_string(paste0("stimulus.fillcolors = GridPattern.", "RepeatAcrossColumns", "([", paste(parameters$color, collapse = ", "), "])"))
#    py_run_string(paste0("stimulus.bounding_boxes = GridPattern.", "RepeatAcrossColumns", "([", paste(parameters$size, collapse = ", "), "])"))
#  } else if(parameters$pattern == "RepeatAcrossRows"){
#    
#    py_run_string(paste0("stimulus.shapes = GridPattern.", "RepeatAcrossRows", "(Pattern([", paste(parameters$shape, collapse = ", "), "])",
#                         ".RepeatElements(int(", parameters$nrows, "/", length(parameters$shape), ")))"))
#    py_run_string(paste0("stimulus.fillcolors = GridPattern.", "RepeatAcrossRows", "(Pattern([", paste(parameters$color, collapse = ", "),
#                         "])", ".RepeatElements(int(", parameters$nrows, "/", length(parameters$color), ")))"))
#    py_run_string(paste0("stimulus.bounding_boxes = GridPattern.", "RepeatAcrossRows", "(Pattern([", paste(parameters$size, collapse = ", "),
#                         "])", ".RepeatElements(int(", parameters$nrows, "/", length(parameters$size), ")))"))
#  } else if(parameters$pattern == "RepeatAcrossColumns"){
#    
#    py_run_string(paste0("stimulus.shapes = GridPattern.", "RepeatAcrossColumns", "(Pattern([", paste(parameters$shape, collapse = ", "), "])",
#                         ".RepeatElements(int(", parameters$nrows, "/", length(parameters$shape), ")))"))
#    py_run_string(paste0("stimulus.fillcolors = GridPattern.", "RepeatAcrossColumns", "(Pattern([", paste(parameters$color, collapse = ", "),
#                         "])", ".RepeatElements(int(", parameters$nrows, "/", length(parameters$color), ")))"))
#    py_run_string(paste0("stimulus.bounding_boxes = GridPattern.", "RepeatAcrossColumns", "(Pattern([", paste(parameters$size, collapse = ", "),
#                         "])", ".RepeatElements(int(", parameters$nrows, "/", length(parameters$size), ")))"))
#  } else if(parameters$pattern == "Subgroups"){
    

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([(20,20), (36,36)], 2 , 2),3)

stimulus.bounding_boxes = tiled_grid_1
stimulus.Show()

stimulus.swap_distinct_elements(n_swap_pairs = 6)
newpresentationorder = stimulus._element_presentation_order

stimulus.Show()
svg = stimulus.GetSVG()