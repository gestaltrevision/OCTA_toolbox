# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 17:06:08 2021

@author: u0090621
"""
from octa.Stimulus import Grid, Outline, Concentric, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern, Sequence, LinearGradient
from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg, ChangingEllipse
from octa.shapes.Image import Image_
from octa.shapes.FitImage import FitImage_
from octa.shapes.Text import Text_ 
from octa.shapes.Polygon import Polygon_
from octa.shapes.RegularPolygon import RegularPolygon_
from octa.shapes.Path import Path_
from octa.shapes.PathSvg import PathSvg_
from octa.measurements import Order, Complexity
import random

#%%

s = Grid(2,2)
s.shapes = GridPattern.RepeatAcrossElements([Triangle])
s.fillcolors = GridPattern.RepeatAcrossElements(["black"])

s.Show()
s.SaveSVG("localglobal1")
#%%

s = Grid(2,2)
s.shapes = GridPattern.RepeatAcrossElements([Rectangle])
s.fillcolors = GridPattern.RepeatAcrossElements(["black"])

s.Show()
s.SaveSVG("localglobal2")
#%%

s = Grid(1,3)
s.shapes = GridPattern.RepeatAcrossElements([Triangle])
s.fillcolors = GridPattern.RepeatAcrossElements(["black"])

s.positions = Positions.CreateCustomPositions(x = [0,-25,25], y = [0,50,50])

s.Show()
s.SaveSVG("localglobal3")
#%%

s = Grid(1,3)
s.shapes = GridPattern.RepeatAcrossElements([Rectangle])
s.fillcolors = GridPattern.RepeatAcrossElements(["black"])

s.positions = Positions.CreateCustomPositions(x = [0,-25,25], y = [0,50,50])

s.Show()
s.SaveSVG("localglobal4")

#%%
s = Grid(1,3, x_margin = 10, y_margin = 10, col_spacing = 150)
s.shapes = GridPattern.RepeatAcrossElements([Image('localglobal1.svg'), Image('localglobal2.svg'), Image('localglobal3.svg'), Image('localglobal4.svg')])
s.boundingboxes = GridPattern.RepeatAcrossElements([(50,50)])
s.positions = Positions.CreateCustomPositions(x = [0,-25,25], y = [0,50,50])

s.Show()
s.SaveSVG("localglobal_1")

#%%
s = Outline(12)
s.positions = Positions.CreateCircle(150, 12)
s.shapes = GridPattern.RepeatAcrossElements([RegularPolygon(4)])
s.boundingboxes = GridPattern.RepeatAcrossElements([(40,40)])
s.fillcolors = GridPattern.RepeatAcrossElements(["orange"])

s.Show()
s.SaveSVG("localglobal5")
#%%
s = Outline(12)
s.positions = Positions.CreateCircle(150, 12)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse])
s.boundingboxes = GridPattern.RepeatAcrossElements([(40,40)])
s.fillcolors = GridPattern.RepeatAcrossElements(["orange"])

s.Show()
s.SaveSVG("localglobal6")
#%%
s = Outline(12)
s.positions = Positions.CreateShape(src = "regularpolygon4.svg", n_elements = 12)
s.shapes = GridPattern.RepeatAcrossElements([RegularPolygon(4)])
s.boundingboxes = GridPattern.RepeatAcrossElements([(40,40)])
s.fillcolors = GridPattern.RepeatAcrossElements(["black"])

s.Show()
s.SaveSVG("localglobal7")
#%%
s = Outline(12)
s.positions = Positions.CreateShape(src = "regularpolygon4.svg", n_elements = 12)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse])
s.boundingboxes = GridPattern.RepeatAcrossElements([(40,40)])
s.fillcolors = GridPattern.RepeatAcrossElements(["black"])

s.Show()
s.SaveSVG("localglobal8")


#%%

s = Outline(6)
s.positions = Positions.CreateCircle(400, 10, starting_point = "right")
s.shapes = GridPattern.RepeatAcrossElements([Ellipse])
s.boundingboxes = GridPattern.RepeatAcrossElements([(80,80)])
s.fillcolors = GridPattern.RepeatAcrossElements(["orange"])

s.Show()
s.SaveSVG("mouth")


#%%
s = Grid(1,3, x_margin = 10, y_margin = 10, col_spacing = 150)
s.shapes = GridPattern.RepeatAcrossElements([Image('localglobal6.svg'), Image('localglobal5.svg'), Image('mouth.svg')])
s.boundingboxes = GridPattern.RepeatAcrossElements([(50,50)])
s.positions = Positions.CreateCustomPositions(x = [-25,25,0], y = [50,50,100])

s.Show()
s.SaveSVG("creativity")
#%%
s = Grid(1,1, x_margin = 0, y_margin = 0)
s.shapes = GridPattern.RepeatAcrossElements([RegularPolygon(4)])
s.boundingboxes = GridPattern.RepeatAcrossColumns([(1500,1500)])
s.Show()
s.SaveSVG("regularpolygon4")
#%%
s = Grid(1,1, x_margin = 0, y_margin = 0)
s.shapes = GridPattern.RepeatAcrossElements([Rectangle])
s.boundingboxes = GridPattern.RepeatAcrossColumns([(1500,1500)])
s.Show()
s.SaveSVG("rectangle")

#%%
s = Grid(2,2, x_margin = 10, y_margin = 10, col_spacing = 60, row_spacing = 60)
s.shapes = GridPattern.RepeatAcrossElements([Image('localglobal6.svg'), Image('localglobal5.svg'), Image('localglobal7.svg'), Image('localglobal8.svg')])
s.boundingboxes = GridPattern.RepeatAcrossElements([(50,50)])
# s.positions = Positions.CreateCustomPositions(x = [0,-25,25], y = [0,50,50])

s.Show()
s.SaveSVG("localglobal_2")

# %%
#Ebbinghaus
pos = Positions.CreateCircle(n_elements = 6, radius = 70)
px = pos.x
py = pos.y
px.append(0)
py.append(0)
s = Outline(7, size = (200,200))
s.positions = Positions.CreateCustomPositions(x = px, y = py)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse])
s.boundingboxes = GridPattern.RepeatAcrossElements([(60,60)])
s.set_element_boundingbox(6, (40,40))
s.set_element_fillcolor(6, "orange")
s.Show()
s.SaveSVG("ebbinghaus1")
s = Outline(10, size = (200,200))
pos = Positions.CreateCircle(n_elements = 9, radius = 40)
px = pos.x
py = pos.y
px.append(0)
py.append(0)
s.positions = Positions.CreateCustomPositions(x = px, y = py)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse])
s.boundingboxes = GridPattern.RepeatAcrossElements([(20,20)])
s.set_element_boundingbox(9, (40,40))
s.set_element_fillcolor(9, "orange")

s.Show()
s.SaveSVG("ebbinghaus2")
#%%
s = Grid(1,2, x_margin = (4,-8), y_margin = (0,0), col_spacing = 45, row_spacing = 60)
s.shapes = GridPattern.RepeatAcrossElements([Image('ebbinghaus1.svg'), Image('ebbinghaus2.svg')])
s.Show()
s.SaveSVG("ebbinghaus")


# %%
# Kanizsa
pos = Positions.CreateCircle(n_elements = 3, radius = 65, starting_point = "bottom")
px = pos.x
py = pos.y
px.append(0)
py.append(-20)
px.append(0)
py.append(20)
s = Outline(5, x_margin = (-25,-25), y_margin = (-10,-30))
s.positions = Positions.CreateCustomPositions(x = px, y = py)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse, Ellipse, Ellipse, RegularPolygon(3), RegularPolygon(3)])
s.boundingboxes = GridPattern.RepeatAcrossElements([(50,50), (50,50), (50,50), (125,125), (125,125)])
s.fillcolors = GridPattern.RepeatAcrossElements(["black", "black", "black", "white", "white"])
s.set_element_borderwidth(3,5)
s.set_element_bordercolor(3,"black")
s.set_element_orientation(4,180)

s.Show()
s.SaveSVG("kanizsa")

#%%
s = Grid(1,3, x_margin = 10, y_margin = 10, col_spacing = 150)
s.shapes = GridPattern.RepeatAcrossElements([Image('kanizsa.svg'), Image('ebbinghaus1.svg'), Image('ebbinghaus2.svg')])
s.boundingboxes = GridPattern.RepeatAcrossElements([(50,50), (40,40), (40,40)])
s.positions = Positions.CreateCustomPositions(x = [0,-25,25], y = [0,50,50])

s.Show()
s.SaveSVG("illusions")

#%%
# outlier detection
random.seed(15)
s = Grid(6,6)
s.boundingboxes = GridPattern.RepeatAcrossElements([(3,30)])
s.shapes = GridPattern.RepeatAcrossElements([Rectangle])
s.orientations = GridPattern.GradientAcrossElements(15, 30).RandomizeAcrossElements()
# s.fillcolors = GridPattern.RepeatAcrossElements(["#d3d3d3"])
s.set_element_orientations(-30, n_changes = 1)
s.Show()
s.SaveSVG("outlierdetection1")

#%%
# visualsearch
random.seed(7897)
s = Grid(6,6, row_spacing = 40, col_spacing = 40, x_margin = 0, y_margin = 0)
# s.boundingboxes = GridPattern.RepeatAcrossElements([(250,65)])
s.shapes = GridPattern.RepeatAcrossElements([Image("img/gabor.png")])
s.orientations = GridPattern.GradientAcrossElements(-100,-80).RandomizeAcrossElements()
# s.fillcolors = GridPattern.RepeatAcrossElements(["#d3d3d3"])
s.set_element_orientations(10, n_changes = 1)
s.Show()
s.SaveSVG("outlierdetection2")

#%%
# visualsearch
random.seed(7897)
s = Grid(6,6, row_spacing = 150, col_spacing = 150)
s.boundingboxes = GridPattern.RepeatAcrossElements([(93.63, 122.88)])
s.shapes = GridPattern.RepeatAcrossElements([Image("img/locked.svg")])
# s.orientations = GridPattern.GradientAcrossElements(-100,-80).RandomizeAcrossElements()
# s.fillcolors = GridPattern.RepeatAcrossElements(["#d3d3d3"])
s.set_element_shape(15, shape_value = Image("img/unlocked.svg"))
s.set_element_boundingbox(15, boundingbox_value = (93.63*1.075, 122.88*1.075))

s.positions = Positions.CreateCustomPositions(x = s.positions.x, 
                                              y = [0,
 0,
 0,
 0,
 0,
 0,
 150,
 150,
 150,
 150,
 150,
 150,
 300,
 300,
 300,
 295,
 300,
 300,
 450,
 450,
 450,
 450,
 450,
 450,
 600,
 600,
 600,
 600,
 600,
 600,
 750,
 750,
 750,
 750,
 750,
 750])

s.Show()
s.SaveSVG("outlierdetection3")


#%%
# outlier detection
random.seed(15)
s = Grid(6,6, x_margin = 10, y_margin = 10)
# s.boundingboxes = GridPattern.RepeatAcrossElements([(3,30)])
s.shapes = GridPattern.RepeatAcrossElements([PathSvg("img/checkmark.svg")])
# s.orientations = GridPattern.GradientAcrossElements(15, 30).RandomizeAcrossElements()
# s.fillcolors = GridPattern.RepeatAcrossElements(["#d3d3d3"])
s.set_element_orientation(element_id = 27, orientation_value = 180)
s.Show()
s.SaveSVG("outlierdetection4")

#%%
s = Grid(2,2, x_margin = 10, y_margin = 10, col_spacing = 52, row_spacing = 50)
s.shapes = GridPattern.RepeatAcrossElements([Image('outlierdetection1.svg'), Image('outlierdetection2.svg'), Image('outlierdetection3.svg'), Image('outlierdetection4.svg')])
s.boundingboxes = GridPattern.RepeatAcrossElements([(50,50)])

s.Show()
s.SaveSVG("outlierdetection")

#%%
# grouping principles
random.seed(15)
s = Grid(16,16, background_shape = Ellipse(boundingbox = (500,500)), row_spacing = 65, col_spacing = 35, size = (500,500),
         stim_orientation = 30)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse])
# s.fillcolors = GridPattern.RepeatAcrossElements(["#d3d3d3"])
s.boundingboxes = GridPattern.RepeatAcrossElements([(25,25)])
s.fillcolors = GridPattern.RepeatAcrossRows(["limegreen", "steelblue"])
s.Show()
s.SaveSVG("grouping1")

s = Grid(16,16, background_shape = Ellipse(boundingbox = (500,500)), row_spacing = 35, col_spacing = 65, size = (500,500),
         stim_orientation = 30)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse])
# s.fillcolors = GridPattern.RepeatAcrossElements(["#d3d3d3"])
s.boundingboxes = GridPattern.RepeatAcrossElements([(25,25)])
s.fillcolors = GridPattern.RepeatAcrossColumns(["limegreen", "steelblue"])
s.Show()
s.SaveSVG("grouping2")

s = Grid(16,16, background_shape = Ellipse(boundingbox = (500,500)), row_spacing = 50, col_spacing = 50, size = (500,500),
         stim_orientation = 30)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse])
# s.fillcolors = GridPattern.RepeatAcrossElements(["#d3d3d3"])
s.boundingboxes = GridPattern.RepeatAcrossElements([(25,25)])
s.fillcolors = GridPattern.RepeatAcrossRows(["steelblue"])
s.Show()
s.SaveSVG("grouping3")

#%%
s = Grid(1,3, x_margin = 10, y_margin = 10)
s.shapes = GridPattern.RepeatAcrossElements([Image('grouping3.svg'), Image('grouping1.svg'), Image('grouping2.svg')])
s.boundingboxes = GridPattern.RepeatAcrossElements([(50,50)])
s.positions = Positions.CreateCustomPositions(x = [0,-30,30], y = [0,50,50])

s.Show()
s.SaveSVG("grouping_1")

#%% 
# order
import random
random.seed(12564)
s = Grid(6,6)
s.shapes = GridPattern.RepeatAcrossElements([Triangle])
s.fillcolors = GridPattern.RepeatAcrossColumns(["limegreen", "steelblue"])
s.Show()
s.SaveSVG("order1")
s.swap_distinct_elements(4)
s.Show()
s.SaveSVG("order2")
#%% 
random.seed(12564)
# complexity
s = Grid(6,6)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse])
s.fillcolors = GridPattern.RepeatAcrossColumns(["steelblue"])
s.Show()
s.SaveSVG("complexity1")

s = Grid(6,6)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse, Rectangle, Triangle])
s.boundingboxes = GridPattern.RepeatAcrossElements([(45,45)]).AddUniformJitter(-20,5, 'x=y')
s.orientations = GridPattern.RepeatAcrossElements([0]).AddUniformJitter(-15,15)
s.fillcolors = GridPattern.GradientAcrossColumns("limegreen", "steelblue")
s.Show()
s.SaveSVG("complexity2")
#%%
s = Grid(2,2, x_margin = 10, y_margin = 10, col_spacing = 50, row_spacing = 50)
s.shapes = GridPattern.RepeatAcrossElements([Image('order1.svg'), Image('order2.svg'), Image('complexity1.svg'), Image('complexity2.svg')])
s.boundingboxes = GridPattern.RepeatAcrossElements([(50,50)])
# s.positions = Positions.CreateCustomPositions(x = [0,-25,25], y = [0,50,50])

s.Show()
s.SaveSVG("ordercomplexity")

#%%
random.seed(145132)
s = Grid(6,6, x_margin = 0, y_margin = 0)
# positions = Positions.CreateRandomPositions(36, width = 150, height = 300, min_distance = 20 )


px = [130,
 55,
 10,
 97,
 98,
 81,
 111,
 96,
 6,
 121,
 65,
 82,
 142,
 133,
 23,
 59,
 133,
 101,
 133,
 34,
 19,
 113,
 4,
 46,
 38,
 11,
 50,
 102,
 79,
 16,
 73,
 68,
 96,
 1,
 131,
 11]
px2 = [35,
 55,
 10,
 97,
 98,
 81,
 111,
 96,
 6,
 121,
 65,
 82,
 142,
 133,
 23,
 59,
 133,
 101,
 133,
 34,
 19,
 113,
 4,
 46,
 38,
 11,
 50,
 102,
 79,
 16,
 73,
 68,
 96,
 1,
 131,
 11]
py = [103,
 153,
 232,
 97,
 52,
 132,
 218,
 198,
 73,
 74,
 213,
 73,
 7,
 262,
 179,
 106,
 58,
 26,
 174,
 201,
 119,
 140,
 170,
 278,
 16,
 150,
 250,
 274,
 22,
 5,
 54,
 173,
 243,
 96,
 33,
 275]

py2 = [50,
 153,
 232,
 97,
 52,
 132,
 218,
 198,
 73,
 74,
 213,
 73,
 7,
 262,
 179,
 106,
 58,
 26,
 174,
 201,
 119,
 140,
 170,
 278,
 16,
 150,
 250,
 274,
 22,
 5,
 54,
 173,
 243,
 96,
 33,
275]

s.positions = Positions.CreateCustomPositions(x = px, y = py)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse])
s.boundingboxes = GridPattern.RepeatAcrossElements([(20,20)])
# s.positions = Positions.CreateCustomPositions(x = [0,-25,25], y = [0,50,50])

s.Show()
s.SaveSVG("symmetry1")

s.positions = Positions.CreateCustomPositions(x = px2, y = py2)
s.shapes = GridPattern.RepeatAcrossElements([Ellipse])
s.boundingboxes = GridPattern.RepeatAcrossElements([(20,20)])
# s.positions = Positions.CreateCustomPositions(x = [0,-25,25], y = [0,50,50])

s.Show()
s.SaveSVG("symmetry2")

#%%
random.seed(145132)
s = Grid(12,12, x_margin = 10, y_margin = 10)
# positions = Positions.CreateRandomPositions(36, width = 150, height = 300, min_distance = 20 )

# s.positions = Positions.CreateCustomPositions(x = px, y = py)
s.shapes = GridPattern.MirrorAcrossColumns([Rectangle, Ellipse, RegularPolygon(4)])
s.fillcolors = GridPattern.MirrorAcrossColumns([ "steelblue", "limegreen"])
s.boundingboxes = GridPattern.RepeatAcrossElements([(40,40)])
# s.positions = Positions.CreateCustomPositions(x = [0,-25,25], y = [0,50,50])

s.Show()
s.SaveSVG("symmetry3")

s.shapes = GridPattern.MirrorAcrossColumns([Rectangle, Ellipse, RegularPolygon(4)])
s.fillcolors = GridPattern.MirrorAcrossColumns([ "steelblue", "limegreen"])
s.boundingboxes = GridPattern.RepeatAcrossElements([(40,40)])
s.set_element_orientation(33, 45)
s.set_element_orientation(44, 45)

s.Show()
s.SaveSVG("symmetry4")

#%%
s = Grid(1,2, x_margin = 10, y_margin = 10, col_spacing = 180, row_spacing = 320)
s.shapes = GridPattern.RepeatAcrossElements([Image('symmetry1.svg'), Image('symmetry1.svg'), Image('symmetry1.svg'), Image('symmetry2.svg')])
s.boundingboxes = GridPattern.RepeatAcrossElements([(170,320)])
s.mirrorvalues = GridPattern.RepeatAcrossElements(["none", "vertical", "none", "vertical"])
# s.positions = Positions.CreateCustomPositions(x = [0,-25,25], y = [0,50,50])

s.Show()
s.SaveSVG("symmetry_1")


#%%
s = Grid(1,2, x_margin = 10, y_margin = 10, col_spacing = 180, row_spacing = 320)
s.shapes = GridPattern.RepeatAcrossElements([Image('symmetry1.svg'), Image('symmetry2.svg'), Image('symmetry1.svg'), Image('symmetry2.svg')])
s.boundingboxes = GridPattern.RepeatAcrossElements([(170,320)])
s.mirrorvalues = GridPattern.RepeatAcrossElements(["none", "vertical", "none", "vertical"])
# s.positions = Positions.CreateCustomPositions(x = [0,-25,25], y = [0,50,50])

s.Show()
s.SaveSVG("symmetry_2")


#%%
s = Grid(18,18, x_margin = 10, y_margin = 10, row_spacing = 55, col_spacing = 55)
s.positions = Positions.CreateSineGrid(18, 18, row_spacing = 55, col_spacing = 55, A = 60, f = 0.05)
# s.positions.SetPositionJitter(distribution = "uniform", min_val = -5, max_val = 5)
s.shapes = GridPattern.RepeatAcrossLayers([Ellipse, Rectangle, Triangle])
s.fillcolors = GridPattern.GradientAcrossLayers("limegreen", "steelblue")
s.boundingboxes = GridPattern.GradientAcrossLayers((30,30), (45,45))
# s.orientations = GridPattern.GradientAcrossLayers(0,360)
s.Show()
s.SaveSVG("appreciation1")

#%%
s = Grid(18,18, x_margin = 10, y_margin = 10, row_spacing = 55, col_spacing = 55)
# s.positions = Positions.CreateSineGrid(18, 18, row_spacing = 55, col_spacing = 55, A = 60, f = 0.05)
# s.positions.SetPositionJitter(distribution = "uniform", min_val = -5, max_val = 5)
s.shapes = GridPattern.RepeatAcrossRightDiagonal([Rectangle])
# s.shapes = GridPattern.TiledElementGrid(source_grid = shapes, tile_multiplier=6)
fillcolors = GridPattern.GradientAcrossRightDiagonal("limegreen", "steelblue",6,6)
s.fillcolors = GridPattern.TiledGrid(source_grid = fillcolors, tile_multiplier=3)
s.fillcolors = GridPattern.GradientAcrossLayers("red", "steelblue")
s.boundingboxes = GridPattern.GradientAcrossLayers((30,30), (45,45))
# s.orientations = GridPattern.GradientAcrossLayers(0,360)
s.Show()
s.SaveSVG("appreciation2")


#%%
s = Grid(18,18, x_margin = 10, y_margin = 10, row_spacing = 45, col_spacing = 45, background_shape = "Triangle", background_color = "#F8F8F8")
# s.positions = Positions.CreateSineGrid(18, 18, row_spacing = 55, col_spacing = 55, A = 60, f = 0.05)
# s.positions.SetPositionJitter(distribution = "uniform", min_val = -5, max_val = 5)
s.shapes = GridPattern.RepeatAcrossRightDiagonal([RegularPolygon(3)])
# s.shapes = GridPattern.TiledElementGrid(source_grid = shapes, tile_multiplier=6)
# fillcolors = GridPattern.GradientAcrossRightDiagonal("limegreen", "steelblue",6,6)
# s.fillcolors = GridPattern.TiledGrid(source_grid = fillcolors, tile_multiplier=3)
s.fillcolors = GridPattern.GradientAcrossRows("red", "steelblue")
s.boundingboxes = GridPattern.GradientAcrossLayers((30,30), (45,45))
s.orientations = GridPattern.RepeatAcrossRows([0,180])
s.Show()
s.SaveSVG("appreciation3")

#%%
s = Grid(1,3, x_margin = 10, y_margin = 10)
s.shapes = GridPattern.RepeatAcrossElements([Image('appreciation3.svg'), Image('appreciation1.svg'), Image('appreciation2.svg')])
s.boundingboxes = GridPattern.RepeatAcrossElements([(50,50)])
s.positions = Positions.CreateCustomPositions(x = [0,-27,27], y = [0,52,52])

s.Show()
s.SaveSVG("appreciation")

#%%
s = Grid(2,2, x_margin = 10, y_margin = 10, col_spacing = 52, row_spacing = 50)
s.shapes = GridPattern.RepeatAcrossElements([Image('outlierdetection1.svg'), Image('outlierdetection2.svg'), Image('outlierdetection3.svg'), Image('outlierdetection4.svg')])
s.boundingboxes = GridPattern.RepeatAcrossElements([(50,50)])

s.Show()
s.SaveSVG("outlierdetection")