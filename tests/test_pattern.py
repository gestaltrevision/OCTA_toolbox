# -*- coding: utf-8 -*-
"""
Created on Mon May 18 15:07:44 2020

@author: Christophe
"""

# The following import ensures that the octa module can be loaded from the 
# parent directory in an editor such as Spyder
import os
os.chdir('..')

import matplotlib.pyplot as plt
from octa.patterns import Pattern

p = Pattern([12,13,14, 15])
p.SwitchValues(1)
print(p)