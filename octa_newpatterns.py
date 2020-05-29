# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Stimulus
from octa.Positions import Positions
from octa import shapes, patterns
from octa.patterns import GridPattern, Pattern


# RepeatAcrossOutIn substitute
center_grid = GridPattern.RepeatElements([1], 2, 4)
outer_layers= Pattern([7, 8, 9])
g = GridPattern.LayeredGrid(center_grid, outer_layers)
print(g.generate())

# RepeatElementsInSubgroups
g = GridPattern.RepeatAcrossRightDiagonal([1,2,3], 3, 3).generate()
print(g)

print(g.tile_elements(2))


# RepeatPatternInCheckerboard
g = GridPattern.RepeatElements([1,2,3], 2, 2).generate()
print(g)

print(g.tile_grid(3))

