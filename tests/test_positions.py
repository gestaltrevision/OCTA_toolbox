# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:59:23 2020

@author: Christophe
"""

# The following import ensures that the octa module can be loaded from the 
# parent directory in an editor such as Spyder
import os
os.chdir('..')

import matplotlib.pyplot as plt
from octa.Positions import Positions

# Generate a pattern
p = Positions.CreateRandomPattern(10)

# Algorithm should fail if the number of elements and the minimum distance are
# incompatible
p = Positions.CreateRandomPattern(10, min_distance = 20)

plt.plot(p.x, p.y, '.')
#%%
p = Positions.CreateSineGrid(10, 10, 30, 30, A = 20, f = 0.1, axis = "y")


plt.plot(p.x, p.y, '.')