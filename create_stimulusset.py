"""
Create sets of stimuli
"""

from octa.Stimulus import Stimulus
from octa.Positions import Positions
from octa import patterns
from octa.shapes import Ellipse, Triangle, Rectangle
import random

### COMPLEXITY ###
shape_options = [[Ellipse], [Triangle], [Rectangle], 
                 [Ellipse, Triangle], #[Triangle, Ellipse], 
                 [Ellipse, Rectangle], #[Rectangle, Ellipse],
                 [Triangle, Rectangle], #[Rectangle, Triangle],
                 [Ellipse, Triangle, Rectangle]
#                 ,[Ellipse, Rectangle, Triangle], [Triangle, Rectangle, Ellipse], [Triangle, Ellipse, Rectangle],
#                 [Rectangle, Ellipse, Triangle], [Rectangle, Triangle, Ellipse]
                 ]
color_options = [["#9C4B9C"], ["#5EA1D8"], ["#54C4D0"], ["#62BD80"], ["#B2D135"], ["#FCE533"], ["#F39130"], ["#ED4959"],
                 ["#9C4B9C","#5EA1D8"], ["#5EA1D8","#54C4D0"], ["#54C4D0","#62BD80"], ["#62BD80","#B2D135"], 
                 ["#B2D135","#FCE533"], ["#FCE533","#F39130"], ["#F39130","#ED4959"], ["#ED4959","#9C4B9C"],                   
                 ["#9C4B9C","#5EA1D8","#54C4D0"], ["#5EA1D8","#54C4D0","#62BD80"], ["#54C4D0","#62BD80","#B2D135"], 
                 ["#62BD80","#B2D135","#FCE533"], ["#B2D135","#FCE533","#F39130"], ["#FCE533","#F39130","#ED4959"],
                 ["#F39130","#ED4959","#9C4B9C"], ["#ED4959","#9C4B9C","#5EA1D8"]]
size_options = [[(20,20)], [(28,28)], [(36,36)],
                [(20,20), (28,28)], #[(28,28), (20,20)]
                [(28,28), (36,36)], #[(36,36), (28,28)]
                [(20,20), (36,36)], #[(36,36), (20,20)]
                [(20,20), (28,28), (36,36)]
                # [(20,20), (36,36), (28,28)], [(28,28), (20,20), (36,36)], [(28,28), (36,36), (20,20)],
                # [(36,36), (20,20), (28,28)], [(36,36), (28,28), (20,20)]
                ]

#size_options = [[(30,30)]]
#color_options = [["#9C4B9C"]]
#random.shuffle(shape_options)
#random.shuffle(size_options)
#random.shuffle(color_options)
shape_options = [random.choice(shape_options)]
size_options = [random.choice(size_options)]
color_options = [random.choice(color_options)]

### ORDER ###
#pattern_options = ["row_symmetry", "column_symmetry", "row_repeat", "column_repeat", 
pattern_options = ["subgroup_repeat", "outin_repeat", "checkerboard_repeat"] #random
#                   "row_gradient", "col_gradient",
#                   "rightdiag_repeat", "leftdiag_repeat", "rightdiag_gradient", "leftdiag_gradient", 
#                   "subgroup_repeat", "subgroup_gradient", "inward_outward", "outward_inward"]

#pattern_options = [random.choice(pattern_options)]

switch_features_options = [0] # 0,1,2 # if pattern not random
switch_elements_options = [1]
#switch_features_options = [random.choice(switch_features_options)]

### STANDARD PATTERN ###

n_rows = 6
n_cols = 6

row_spacing = 40
col_spacing = 40

x_offset = 40
y_offset = 40

stimulus = Stimulus(background_color = "white")
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)

stimulus.orientation = patterns.BasicPattern([0]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.shapes  = patterns.BasicPattern(shape_options[0]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.colour  = patterns.BasicPattern(color_options[0]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size  = patterns.BasicPattern(size_options[0]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)

#stimulus.Render()
#stimulus.Show()
                            
for i in range(len(shape_options)):
    if len(shape_options[i]) > 1:        
        for shapepattern in pattern_options:
            
            if shapepattern == "row_symmetry":
                stimulus.shapes  = patterns.SymmetryPattern(shape_options[i], n_rows, n_cols).MirrorAcrossRows()
            elif shapepattern == "column_symmetry":
                stimulus.shapes  = patterns.SymmetryPattern(shape_options[i], n_rows, n_cols).MirrorAcrossColumns()
            elif shapepattern == "row_repeat":
                stimulus.shapes  = patterns.GridRepeater(shape_options[i], n_rows, n_cols).RepeatAcrossRows()
            elif shapepattern == "column_repeat":
                stimulus.shapes  = patterns.GridRepeater(shape_options[i], n_rows, n_cols).RepeatAcrossColumns()  
            elif shapepattern == "subgroup_repeat":
                stimulus.shapes  = patterns.GridRepeater(shape_options[i], n_rows, n_cols).RepeatElementsInSubgroups()
            elif shapepattern == "outin_repeat":
                stimulus.shapes  = patterns.GridRepeater(shape_options[i], n_rows, n_cols).RepeatAcrossOutIn()
            elif shapepattern == "checkerboard_repeat":
                stimulus.shapes  = patterns.GridRepeater(shape_options[i], n_rows, n_cols).RepeatPatternInCheckerboard()
            elif shapepattern == "random":
                stimulus.shapes  = patterns.BasicPattern(shape_options[i]).DuplicatePatternToSize(n_rows * n_cols)
                stimulus.shapes.RandomizeOrder()
            
            if shapepattern != "random":
                for n_switches in switch_features_options:
                    stimulus.shapes.SwitchValues(n_switches)
                    
    else:
        stimulus.shapes  = patterns.BasicPattern(shape_options[i]).DuplicatePatternToSize(n_rows * n_cols)
    
    for j in range(len(size_options)): 
        if len(size_options[j]) > 1:
            for sizepattern in pattern_options:
        
                if sizepattern == "row_symmetry":
                    stimulus.size  = patterns.SymmetryPattern(size_options[j], n_rows, n_cols).MirrorAcrossRows()
                elif sizepattern == "column_symmetry":
                    stimulus.size  = patterns.SymmetryPattern(size_options[j], n_rows, n_cols).MirrorAcrossColumns()
                elif sizepattern == "row_repeat":
                    stimulus.size  = patterns.GridRepeater(size_options[j], n_rows, n_cols).RepeatAcrossRows()
                elif sizepattern == "column_repeat":
                    stimulus.size  = patterns.GridRepeater(size_options[j], n_rows, n_cols).RepeatAcrossColumns()  
                elif sizepattern == "subgroup_repeat":
                    stimulus.size  = patterns.GridRepeater(size_options[i], n_rows, n_cols).RepeatElementsInSubgroups()
                elif sizepattern == "outin_repeat":
                    stimulus.size  = patterns.GridRepeater(size_options[j], n_rows, n_cols).RepeatAcrossOutIn()
                elif sizepattern == "checkerboard_repeat":
                    stimulus.size  = patterns.GridRepeater(size_options[j], n_rows, n_cols).RepeatPatternInCheckerboard()
                elif sizepattern == "random":
                    stimulus.size  = patterns.BasicPattern(size_options[j]).DuplicatePatternToSize(n_rows * n_cols)
                    stimulus.size.RandomizeOrder()
                
                if sizepattern != "random":   
                    for n_switches in switch_features_options:
                        stimulus.size.SwitchValues(n_switches)
        else:
            stimulus.size  = patterns.BasicPattern(size_options[j]).DuplicatePatternToSize(n_rows * n_cols)
            
        for k in range(len(color_options)):
            if len(color_options[k]) > 1:
                for colorpattern in pattern_options:
        
                    if colorpattern == "row_symmetry":
                        stimulus.colour  = patterns.SymmetryPattern(color_options[k], n_rows, n_cols).MirrorAcrossRows()
                    elif colorpattern == "column_symmetry":
                        stimulus.colour  = patterns.SymmetryPattern(color_options[k], n_rows, n_cols).MirrorAcrossColumns()
                    elif colorpattern == "row_repeat":
                        stimulus.colour  = patterns.GridRepeater(color_options[k], n_rows, n_cols).RepeatAcrossRows()
                    elif colorpattern == "column_repeat":
                        stimulus.colour  = patterns.GridRepeater(color_options[k], n_rows, n_cols).RepeatAcrossColumns()  
                    elif colorpattern == "subgroup_repeat":
                        stimulus.colour  = patterns.GridRepeater(color_options[k], n_rows, n_cols).RepeatElementsInSubgroups()
                    elif colorpattern == "outin_repeat":
                        stimulus.colour  = patterns.GridRepeater(color_options[k], n_rows, n_cols).RepeatAcrossOutIn()
                    elif colorpattern == "checkerboard_repeat":
                        stimulus.colour  = patterns.GridRepeater(color_options[k], n_rows, n_cols).RepeatPatternInCheckerboard()
                    elif colorpattern == "random":
                        stimulus.colour  = patterns.BasicPattern(color_options[k]).DuplicatePatternToSize(n_rows * n_cols)
                        stimulus.colour.RandomizeOrder()
                    
                    if colorpattern != "random":
                        for n_switches in switch_features_options:
                            stimulus.colour.SwitchValues(n_switches)
                            
                        for i in switch_elements_options:
                            stimulus.SwitchElements(i)                        
                            stimulus.Render()
                            stimulus.Show()
                
            else:
                stimulus.colour  = patterns.BasicPattern(color_options[k]).DuplicatePatternToSize(n_rows * n_cols)
                        
                stimulus.Render()
                stimulus.Show()
