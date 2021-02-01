# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:28:21 2021

@author: u0090621
"""

stimulus = Grid(10,10, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(30,30)])
stimulus.orientations = GridPattern.GradientAcrossColumns(-30, 30)
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
                                                             
random.seed(3)
stimulus.positions = Positions.CreateSineGrid(n_rows = 10, n_cols = 10, row_spacing = 30, col_spacing = 30, A = 25, f = .1, axis = "x")
x,y = stimulus.positions.GetPositions()
x = x + 10
y = y*2
stimulus.positions = [x,y]
stimulus.Show()