"""
Create sets of stimuli
"""

from octa.Stimulus import Stimulus
from octa.Positions import Positions
from octa import patterns
from octa.shapes import Ellipse, Triangle, Rectangle
import random

############################################################
### GENERATE RANDOM LEVEL OF COMPLEXITY, ORDER, DEVIANTS ###
############################################################

##################
### COMPLEXITY ###
##################
shapecompl1 = random.sample([[Ellipse], [Triangle], [Rectangle]], 1)
shapecompl2 = random.sample([[Ellipse, Triangle], [Triangle, Ellipse], 
               [Ellipse, Rectangle], [Rectangle, Ellipse],
               [Triangle, Rectangle], [Rectangle, Triangle]], 1)
shapecompl3 = random.sample([[Ellipse, Triangle, Rectangle], [Ellipse, Rectangle, Triangle], 
               [Triangle, Rectangle, Ellipse], [Triangle, Ellipse, Rectangle],
               [Rectangle, Ellipse, Triangle], [Rectangle, Triangle, Ellipse]], 1)
shape_values = random.sample([shapecompl1, shapecompl2, shapecompl3],1)[0]
#shape_values = random.sample([shapecompl1, shapecompl2],1)[0]


colorcompl1 = random.sample([["#9C4B9C"], ["#5EA1D8"], ["#54C4D0"], ["#62BD80"], ["#B2D135"], ["#FCE533"], ["#F39130"], ["#ED4959"]], 1)
# subsample of color combinations: only neighboring colors
colorcompl2 = random.sample([["#9C4B9C","#5EA1D8"], ["#5EA1D8","#54C4D0"], ["#54C4D0","#62BD80"], ["#62BD80","#B2D135"], 
                 ["#B2D135","#FCE533"], ["#FCE533","#F39130"], ["#F39130","#ED4959"], ["#ED4959","#9C4B9C"]], 1)
# subsample of color combinations: only analogous colors (neighboring colors)
colorcompl3 = random.sample([["#9C4B9C","#5EA1D8","#54C4D0"], ["#5EA1D8","#54C4D0","#62BD80"], ["#54C4D0","#62BD80","#B2D135"], 
                 ["#62BD80","#B2D135","#FCE533"], ["#B2D135","#FCE533","#F39130"], ["#FCE533","#F39130","#ED4959"],
                 ["#F39130","#ED4959","#9C4B9C"], ["#ED4959","#9C4B9C","#5EA1D8"]], 1)
color_values = random.sample([colorcompl1, colorcompl2, colorcompl3],1)[0]
#color_values = random.sample([colorcompl1, colorcompl2],1)[0]

size1, size2, size3 = 20, 28, 36
sizecompl1 = random.sample([[(size1,size1)], [(size2,size2)], [(size3,size3)]], 1)
sizecompl2 = random.sample([[(size1,size1), (size2,size2)], [(size2,size2), (size1,size1)],
                            [(size2,size2), (size3,size3)], [(size3,size3), (size2,size2)],
                            [(size1,size1), (size3,size3)], [(size3,size3), (size1,size1)]], 1)
sizecompl3 = random.sample([[(size1,size1), (size2,size2), (size3,size3)], [(size1,size1), (size3,size3), (size2,size2)], 
                            [(size2,size2), (size1,size1), (size3,size3)], [(size2,size2), (size3,size3), (size1,size1)],
                            [(size3,size3), (size1,size1), (size2,size2)], [(size3,size3), (size2,size2), (size1,size1)]], 1)
size_values = random.sample([sizecompl1, sizecompl2, sizecompl3],1)[0]
#size_values = random.sample([sizecompl1, sizecompl2],1)[0]

### ADDITIONAL COMPLEXITY PARAMETERS: SHAPEXYRATIO, ORIENTATION ###
### ADDITIONAL COMPLEXITY MEASURES: LOCE: see below ###

#############
### ORDER ###
#############
### TYPES OF ORDER ###
    
    ### SHAPE ###
symmetry = random.choice(["row_symmetry", "column_symmetry"])
alternation = random.choice(["row_alternate", "column_alternate"])
repetition = random.choice(["row_repeat", "column_repeat"])
subgroups = "subgroup_repeat"
outin = "outin_repeat"
checkerboard = "checkerboard_repeat"
randompattern = "randompattern"
### ADDITIONAL ORDERINGS: gradient (row / column) ###
### DIAGONAL OPTIONS: rightdiag_repeat, leftdiag_repeat, rightdiag_gradient, leftdiag_gradient ###
### EXTRA/TOCREATE: subgroup_gradient, inout_repeat ###

if len(shape_values[0]) > 1:
    shape_pattern = [random.choice([symmetry, alternation, repetition, subgroups, outin, checkerboard, randompattern])]
else:
    shape_pattern = ["identity"]

    ### COLOR ###
symmetry = random.choice(["row_symmetry", "column_symmetry"])
alternation = random.choice(["row_alternate", "column_alternate"])
repetition = random.choice(["row_repeat", "column_repeat"])
subgroups = "subgroup_repeat"
outin = "outin_repeat"
checkerboard = "checkerboard_repeat"
randompattern = "randompattern"
### ADDITIONAL ORDERINGS: gradient (row / column) ###
### DIAGONAL OPTIONS: rightdiag_repeat, leftdiag_repeat, rightdiag_gradient, leftdiag_gradient ###
### EXTRA/TOCREATE: subgroup_gradient, inout_repeat ###
if len(color_values[0]) > 1:
    color_pattern = [random.choice([symmetry, alternation, repetition, subgroups, outin, checkerboard, randompattern])]    
else:
    color_pattern = ["identity"]
    
    ### SIZE ###
symmetry = random.choice(["row_symmetry", "column_symmetry"])
alternation = random.choice(["row_alternate", "column_alternate"])
repetition = random.choice(["row_repeat", "column_repeat"])
subgroups = "subgroup_repeat"
outin = "outin_repeat"
checkerboard = "checkerboard_repeat"
randompattern = "randompattern"
### ADDITIONAL ORDERINGS: gradient (row / column) ###
### DIAGONAL OPTIONS: rightdiag_repeat, leftdiag_repeat, rightdiag_gradient, leftdiag_gradient ###
### EXTRA/TOCREATE: subgroup_gradient, inout_repeat ###
if len(size_values[0]) > 1:
    size_pattern = [random.choice([symmetry, alternation, repetition, subgroups, outin, checkerboard, randompattern])]
else:
    size_pattern = ["identity"]
    
############################################
### SPECIFY COMPLEXITY AND ORDER OPTIONS ###
############################################
#shape_values = [[Ellipse]]
#shape_pattern = ["identity"]
#
#size_values = [[28]]
#size_pattern = ["identity"]
##size_pattern = [symmetry, repetition, subgroups, outin, checkerboard, randompattern]
#
#color_values = [["#9C4B9C","#5EA1D8","#54C4D0"]]
##color_pattern = ["identity"]
##color_pattern = ["row_symmetry", "column_symmetry", "row_alternate", "column_alternate",  "row_repeat", "column_repeat", subgroups, outin, checkerboard, randompattern]
#color_pattern = ["row_repeat", "column_repeat"]

#############################################################
### CALCULATE ORDER AND COMPLEXITY MEASURES (except LOCE) ###
#############################################################

LOC = len(shape_values[0]) + len(color_values[0]) + len(size_values[0]) # number of different features across all dimensions
LOCI = 0 # number of dimensions on which the elements of the display are non-identical 

if len(shape_values[0]) > 1:
    LOCI += 1
if len(color_values[0]) > 1:
    LOCI += 1
if len(size_values[0]) > 1:
    LOCI += 1    
    
### ORDER ###
    
LOOC = 0 # level of order congruency
if shape_pattern == color_pattern:
    LOOC += 1
if size_pattern == color_pattern:
    LOOC += 1
if shape_pattern == size_pattern:
    LOOC += 1
 
####################################
### INSERT DEVIANTS FROM PATTERN ###
####################################

### SWITCH FEATURES ###
shape_switches = [0] # 0,1,2 # if pattern not random or identity
color_switches = [0]
size_switches = [0]

### SWITCH ELEMENTS ###
element_switches = [0]
#switch_features_options = [random.choice(switch_features_options)]

######################
### CREATE STIMULI ###
######################

### STANDARD PATTERN ###
n_rows = 6
n_cols = 6

row_spacing = 40
col_spacing = 40

x_offset = 40
y_offset = 40

stimulus = Stimulus(background_color = "white", width = 300, height = 300)
stimulus.positions   = Positions.Create2DGrid(n_rows, n_cols, row_spacing, col_spacing, x_offset, y_offset)

stimulus.orientation = patterns.BasicPattern([0]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.shapes  = patterns.BasicPattern(shape_values[0]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.color  = patterns.BasicPattern(color_values[0]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.size  = patterns.BasicPattern(size_values[0]).DuplicatePatternToSize(n_rows * n_cols)
stimulus.data        = patterns.BasicPattern(["none"]).DuplicatePatternToSize(n_rows * n_cols)

#stimulus.Render()
#stimulus.Show()
                            
for i in range(len(shape_values)):  
    for a in range(len(shape_pattern)):
            
        if shape_pattern[a] == "identity":
            stimulus.shapes  = patterns.BasicPattern(shape_values[i]).DuplicatePatternToSize(n_rows * n_cols)  
        elif shape_pattern[a] == "row_symmetry":
            stimulus.shapes  = patterns.SymmetryPattern(shape_values[i], n_rows, n_cols).MirrorAcrossRows()
        elif shape_pattern[a] == "column_symmetry":
            stimulus.shapes  = patterns.SymmetryPattern(shape_values[i], n_rows, n_cols).MirrorAcrossColumns()        
        elif shape_pattern[a] == "row_alternate":
            stimulus.shapes  = patterns.GridRepeater(shape_values[i], n_rows, n_cols).RepeatAcrossRows()
        elif shape_pattern[a] == "column_alternate":
            stimulus.shapes  = patterns.GridRepeater(shape_values[i], n_rows, n_cols).RepeatAcrossColumns()  
        elif shape_pattern[a] == "row_repeat":
            shapepattern = patterns.BasicPattern(shape_values[i]).DuplicateElements(n_duplications = int(n_cols/len(shape_values[i]))).pattern
            stimulus.shapes  = patterns.GridRepeater(shapepattern, n_rows, n_cols).RepeatAcrossRows()
        elif shape_pattern[a] == "column_repeat":
            shapepattern = patterns.BasicPattern(shape_values[i]).DuplicateElements(n_duplications = int(n_cols/len(shape_values[i]))).pattern
            stimulus.shapes  = patterns.GridRepeater(shapepattern, n_rows, n_cols).RepeatAcrossColumns()  
        elif shape_pattern[a] == "subgroup_repeat":
            stimulus.shapes  = patterns.GridRepeater(shape_values[i], n_rows, n_cols).RepeatElementsInSubgroups()
        elif shape_pattern[a] == "outin_repeat":
            stimulus.shapes  = patterns.GridRepeater(shape_values[i], n_rows, n_cols).RepeatAcrossOutIn()
        elif shape_pattern[a] == "checkerboard_repeat":
            stimulus.shapes  = patterns.GridRepeater(shape_values[i], n_rows, n_cols).RepeatPatternInCheckerboard()
        elif shape_pattern[a] == "randompattern":
            stimulus.shapes  = patterns.BasicPattern(shape_values[i]).DuplicatePatternToSize(n_rows * n_cols)
            stimulus.shapes.RandomizeOrder()

        if (shape_pattern[a] != "randompattern") & (shape_pattern[a] != "identity"):
            for n_switches in shape_switches:
                stimulus.shapes.SwitchValues(n_switches)
    
    for j in range(len(size_values)): 
        for b in range(len(size_pattern)):
    
            if size_pattern[b] == "identity":
                stimulus.size  = patterns.BasicPattern(size_values[j]).DuplicatePatternToSize(n_rows * n_cols)
            elif size_pattern[b] == "row_symmetry":
                stimulus.size  = patterns.SymmetryPattern(size_values[j], n_rows, n_cols).MirrorAcrossRows()
            elif size_pattern[b] == "column_symmetry":
                stimulus.size  = patterns.SymmetryPattern(size_values[j], n_rows, n_cols).MirrorAcrossColumns()
            elif size_pattern[b] == "row_alternate":
                stimulus.size  = patterns.GridRepeater(size_values[j], n_rows, n_cols).RepeatAcrossRows()
            elif size_pattern[b] == "column_alternate":
                stimulus.size  = patterns.GridRepeater(size_values[j], n_rows, n_cols).RepeatAcrossColumns()  
            elif size_pattern[b] == "row_repeat":
                sizepattern = patterns.BasicPattern(size_values[j]).DuplicateElements(n_duplications = int(n_cols/len(size_values[j]))).pattern
                stimulus.size  = patterns.GridRepeater(sizepattern, n_rows, n_cols).RepeatAcrossRows()
            elif size_pattern[b] == "column_repeat":
                sizepattern = patterns.BasicPattern(size_values[j]).DuplicateElements(n_duplications = int(n_cols/len(size_values[j]))).pattern
                stimulus.size  = patterns.GridRepeater(sizepattern, n_rows, n_cols).RepeatAcrossColumns()  
            elif size_pattern[b] == "subgroup_repeat":
                stimulus.size  = patterns.GridRepeater(size_values[j], n_rows, n_cols).RepeatElementsInSubgroups()
            elif size_pattern[b] == "outin_repeat":
                stimulus.size  = patterns.GridRepeater(size_values[j], n_rows, n_cols).RepeatAcrossOutIn()
            elif size_pattern[b] == "checkerboard_repeat":
                stimulus.size  = patterns.GridRepeater(size_values[j], n_rows, n_cols).RepeatPatternInCheckerboard()
            elif size_pattern[b] == "randompattern":
                stimulus.size  = patterns.BasicPattern(size_values[j]).DuplicatePatternToSize(n_rows * n_cols)
                stimulus.size.RandomizeOrder()
            
            if (size_pattern[b] != "randompattern") & (size_pattern[b] != "identity"):   
                for n_switches in size_switches:
                    stimulus.size.SwitchValues(n_switches)
            
        for k in range(len(color_values)):
                for c in range(len(color_pattern)):
        
                    if color_pattern[c] == "identity":
                        stimulus.color  = patterns.BasicPattern(color_values[k]).DuplicatePatternToSize(n_rows * n_cols)
                    elif color_pattern[c] == "row_symmetry":
                        stimulus.color  = patterns.SymmetryPattern(color_values[k], n_rows, n_cols).MirrorAcrossRows()
                    elif color_pattern[c] == "column_symmetry":
                        stimulus.color  = patterns.SymmetryPattern(color_values[k], n_rows, n_cols).MirrorAcrossColumns()
                    elif color_pattern[c] == "row_alternate":
                        stimulus.color  = patterns.GridRepeater(color_values[k], n_rows, n_cols).RepeatAcrossRows()
                    elif color_pattern[c] == "column_alternate":
                        stimulus.color  = patterns.GridRepeater(color_values[k], n_rows, n_cols).RepeatAcrossColumns()  
                    elif color_pattern[c] == "row_repeat":
                        colorpattern = patterns.BasicPattern(color_values[k]).DuplicateElements(n_duplications = int(n_cols/len(color_values[k]))).pattern
                        stimulus.color  = patterns.GridRepeater(colorpattern, n_rows, n_cols).RepeatAcrossRows()
                    elif color_pattern[c] == "column_repeat":
                        colorpattern = patterns.BasicPattern(color_values[k]).DuplicateElements(n_duplications = int(n_cols/len(color_values[k]))).pattern
                        stimulus.color  = patterns.GridRepeater(colorpattern, n_rows, n_cols).RepeatAcrossColumns()  
                    elif color_pattern[c] == "subgroup_repeat":
                        stimulus.color  = patterns.GridRepeater(color_values[k], n_rows, n_cols).RepeatElementsInSubgroups()
                    elif color_pattern[c] == "outin_repeat":
                        stimulus.color  = patterns.GridRepeater(color_values[k], n_rows, n_cols).RepeatAcrossOutIn()
                    elif color_pattern[c] == "checkerboard_repeat":
                        stimulus.color  = patterns.GridRepeater(color_values[k], n_rows, n_cols).RepeatPatternInCheckerboard()
                    elif color_pattern[c] == "randompattern":
                        stimulus.color  = patterns.BasicPattern(color_values[k]).DuplicatePatternToSize(n_rows * n_cols)
                        stimulus.color.RandomizeOrder()
                    
                    if (color_pattern[c] != "randompattern") & (color_pattern[c] != "identity"):
                        for n_switches in color_switches:
                            stimulus.color.SwitchValues(n_switches)
                            
                        for nr_switches in element_switches:
                            stimulus.SwitchElements(nr_switches)                        
                            stimulus.Render()
                            stimulus.Show()
                            LOCE = stimulus.CalculateElementsLOCE() # number of different element types present in display
                            print("LOC: " + str(LOC) + "\t")
                            print("LOCI: " + str(LOCI) + "\t")
                            print("LOCE: " + str(LOCE) + "\t")
                            print("shape_values: " + str(shape_values[0]) + "\t")
                            print("color_values: " + str(color_values[0]) + "\t")
                            print("size_values: " + str(size_values[0]) + "\t")
                            print("LOOC: " + str(LOOC) + "\t")
                            print("shape_pattern: " + str(shape_pattern[a]) + "\t")
                            print("color_pattern: " + str(color_pattern[c]) + "\t")
                            print("size_pattern: " + str(size_pattern[b]) + "\t")
#                            print("shape_switches: " + str(shape_switches) + "\t")
#                            print("color_switches: " + str(color_switches) + "\t")
#                            print("size_switches: " + str(size_switches) + "\t")
                            print("element_switches: " + str(nr_switches) + "\t")
                            
                    else:
                                        
                        stimulus.Render()
                        stimulus.Show()
                        LOCE = stimulus.CalculateElementsLOCE() # number of different element types present in display
                        print("LOC: " + str(LOC) + "\t")
                        print("LOCI: " + str(LOCI) + "\t")
                        print("LOCE: " + str(LOCE) + "\t")
                        print("shape_values: " + str(shape_values[0]) + "\t")
                        print("color_values: " + str(color_values[0]) + "\t")
                        print("size_values: " + str(size_values[0]) + "\t")
                        print("LOOC: " + str(LOOC) + "\t")
                        print("shape_pattern: " + str(shape_pattern[a]) + "\t")
                        print("color_pattern: " + str(color_pattern[c]) + "\t")
                        print("size_pattern: " + str(size_pattern[b]) + "\t")
#                       print("shape_switches: " + str(shape_switches) + "\t")
#                       print("color_switches: " + str(color_switches) + "\t")
#                       print("size_switches: " + str(size_switches) + "\t")
                        print("element_switches: " + str(0) + "\t")
