# -*- coding: utf-8 -*-
"""
OCTA toolbox: demo
"""
from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern, Sequence, LinearGradient
from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg, ChangingEllipse
from octa.measurements import Complexity
import random


#%%
stimulus = Grid(1,9, col_spacing=60, stim_orientation = 50, background_color = "red", size = (500,500))
stimulus.shapes = GridPattern.RepeatAcrossElements([Polygon(8)])
stimulus.borderwidths = GridPattern.RepeatAcrossElements([10])
stimulus.bordercolors = GridPattern.RepeatAcrossElements([
"blue", 
"#d3d3d3",
["radial", "white", "red"], 
["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], 
["vertical", "green", "white", "green"], 
["diagonal", "red", "white"],
['set', "orange", 'to = "purple", begin = "click", dur = "2s"'],
['animate', "red", 'values = "red;orange;green;blue;indigo;violet;red", begin = "2s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'],
['animate', "red", 'values = "red;orange;green;blue;indigo;violet;red", begin = "2s", calcMode = "discrete", dur = "10s", repeatCount = "indefinite"']
])
stimulus.Show()
stimulus.SaveJSON("output/st")

Complexity.CalculateElementsLOCE(stimulus)

st = Stimulus.LoadFromJSON("output/st.json")
st.Show()

#%%
stimulus = Grid(5,5)
stimulus.Show()
stimulus.GetSVG()
stimulus.GetJSON()

stimulus.SaveJSON('test_stimulus', folder = "output")
stimulus.SaveSVG('test_stimulus', folder = "output")
stimulus.SavePNG('test_stimulus', folder = "output")
stimulus.SaveJPG('test_stimulus', folder = "output")
stimulus.SaveTIFF('test_stimulus', folder = "output")
stimulus.SavePDF('test_stimulus', folder = "output")

#%%
stimulus = Grid(1,5)
stimulus.shapes = GridPattern.RepeatAcrossElements([Polygon(8)])
stimulus.opacities = GridPattern.RepeatAcrossElements([1,
                                                       0.5,
                                                       ['set', 0.05, 'to = 1, begin = "click", dur = "2s"'],
['animate', 1, 'values = ".8;.6;.4;.2;0;.2;.4;.6;.8;1", begin = "2s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'],
['animate', 1, 'values = ".8;.6;.4;.2;0;.2;.4;.6;.8;1", begin = "2s", calcMode = "discrete", dur = "10s", repeatCount = "indefinite"']
])
stimulus.bordercolors = GridPattern.RepeatAcrossElements(["black"])
stimulus.Show()
stimulus.SaveSVG("output/stim")

#%%
stimulus = Grid(4,4)
stimulus.shapes = GridPattern.RepeatAcrossElements([Polygon(8)])
stimulus.borderwidths = GridPattern.RepeatAcrossElements([5,
                                                          ['set', 0, 'to = 15, begin = "click", dur = "2s"'],
['animate', 15, 'values = "10;8;6;4;2;0", begin = "2s", calcMode = "linear", dur = "10s", repeatCount = "indefinite"'],
['animate', 15, 'values = "10;8;6;4;2;0", begin = "2s", calcMode = "discrete", dur = "10s", repeatCount = "indefinite"']
])
stimulus.bordercolors = GridPattern.RepeatAcrossElements(["black"])
stimulus.Show()
stimulus.SaveSVG("output/stim")

#%%
stimulus = Grid(1,30, col_spacing = 5, row_spacing = 5)
stimulus.shapes = GridPattern.RepeatAcrossElements([Rectangle])
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(2,150)])
stimulus.fillcolors = GridPattern.RepeatAcrossElements(["lightgrey"])
stimulus.positions.SetLocationJitter("x", min_val = -35, max_val = 35)
stimulus.Show()
stimulus.SaveSVG("output/stim1")

#%%
stimulus = Grid(1,30, col_spacing = 5, row_spacing = 5, stim_orientation = 90)
stimulus.shapes = GridPattern.RepeatAcrossElements([Rectangle])
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(2,150)])
stimulus.fillcolors = GridPattern.RepeatAcrossElements(["lightgrey"])
stimulus.positions.SetLocationJitter("x", min_val = -35, max_val = 35)
stimulus.Show()

stimulus.SaveSVG("output/stim2")


#%%

stimulus = Grid(1,30, col_spacing = 5, row_spacing = 5)
stimulus.shapes = GridPattern.RepeatAcrossElements([Rectangle])
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(2,150)])
stimulus.fillcolors = GridPattern.RepeatAcrossElements(["lightgrey"])
stimulus.positions.SetLocationJitter("x", min_val = -35, max_val = 35)
# stimulus.Show()

# stimulus.positions.GetPositions()

stimulus2 = Grid(1,60, col_spacing = 5, row_spacing = 5)
x = [stimulus.positions.x[i] + 0 for i in range(len(stimulus.positions.x))]
y = [stimulus.positions.y[i] + 75 for i in range(len(stimulus.positions.y))]
new_x = [item for sublist in [x, y] for item in sublist]
new_y = [item for sublist in [y, x] for item in sublist]
stimulus2.positions = Positions.CreateCustomPositions(x = new_x, y = new_y)
stimulus2.shapes = GridPattern.RepeatAcrossElements([Rectangle])
stimulus2.bounding_boxes = GridPattern.RepeatAcrossElements([(2,150),(2,150),(2,150),(2,150),(2,150),
                                                             (2,150),(2,150),(2,150),(2,150),(2,150),
                                                             (2,150),(2,150),(2,150),(2,150),(2,150),
                                                             (2,150),(2,150),(2,150),(2,150),(2,150),
                                                             (2,150),(2,150),(2,150),(2,150),(2,150),
                                                             (2,150),(2,150),(2,150),(2,150),(2,150),
                                                             (150,2),(150,2),(150,2),(150,2),(150,2),
                                                             (150,2),(150,2),(150,2),(150,2),(150,2),
                                                             (150,2),(150,2),(150,2),(150,2),(150,2),
                                                             (150,2),(150,2),(150,2),(150,2),(150,2),
                                                             (150,2),(150,2),(150,2),(150,2),(150,2),
                                                             (150,2),(150,2),(150,2),(150,2),(150,2)])

stimulus2.positions.SetLocationJitter("xy", min_val = -35, max_val = 35)
stimulus2.Show()
#.SaveSVG("output/stim2")


#%%
stimulus = Grid(4,4, row_spacing = 40, col_spacing = 40)
# shapes_source_grid = GridPattern.MirrorAcrossRightDiagonal([Image("output/stim1.svg"), Image("output/stim2.svg")])
stimulus.shapes = GridPattern.TiledGrid(GridPattern.MirrorAcrossRightDiagonal([Image("output/stim1.svg"), Image("output/stim2.svg")], 2 , 2), (2,2))
stimulus.Show()

stimulus.SaveSVG("output/combination")

#%%
stimulus = Grid(9,12)
stimulus.fillcolors = GridPattern.RepeatAcrossLayers(["red", "green", "blue"])
stimulus.bounding_boxes = GridPattern.MirrorAcrossLayers([(15,15), (30,30), (45,45)])
stimulus.borderwidths = GridPattern.GradientAcrossLayers(start_value = 0, end_value = 5)
stimulus.bordercolors = GridPattern.RepeatAcrossElements(["black"])
stimulus.Show()
# stimulus.SaveSVG("output/test")

#%%
stimulus = Grid(15,9)

stimulus.fillcolors = GridPattern.GradientAcrossLayers(start_value = 'red', end_value = 'green')
stimulus.Show()
# stimulus.SaveSVG("output/test")


#%%
stimulus = Grid(2,2)
stimulus.fillcolors = GridPattern.RepeatAcrossElements(["red", "green", "blue"])
stimulus.shapes         = GridPattern.RepeatAcrossElements([
        Rectangle, 
        Path("M12 22A10 10 0 1 0 2 12a10 10 0 0 0 10 10zM8.31 10.14l3-2.86a.49.49 0 0 1 .15-.1.54.54 0 0 1 .16-.1.94.94 0 0 1 .76 0 1 1 0 0 1 .33.21l3 3a1 1 0 0 1-1.42 1.42L13 10.41V16a1 1 0 0 1-2 0v-5.66l-1.31 1.25a1 1 0 0 1-1.38-1.45z", 24,24), 
        PathSvg("img/arrow-circle-up-svgrepo-com.svg"), 
        #Image("img/arrow-circle-up-svgrepo-com.svg"), 
        Path("M 256.00,0.00C 114.615,0.00,0.00,114.615,0.00,256.00s 114.615,256.00, 256.00,256.00s 256.00-114.615, 256.00-256.00S 397.385,0.00, 256.00,0.00z M 208.00,416.00L 102.00,278.00l 47.00-49.00l 59.00,75.00 l 185.00-151.00l 23.00,23.00L 208.00,416.00z", 512, 512), 
        PathSvg("img/checkmark.svg")
        ])

stimulus.Show()
# stimulus.SaveSVG("output/test")

#%%

stimulus = Grid(2,2, x_margin = 20.5)

stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(20, 20)])
# stimulus.orientations   = GridPattern.RepeatAcrossElements([0], self._n_rows, self._n_cols)
# stimulus.bordercolors   = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
# stimulus.borderwidths   = GridPattern.RepeatAcrossElements([0], self.n_rows, self.n_cols)
# stimulus.fillcolors     = GridPattern.RepeatAcrossElements(["dodgerblue"], self.n_rows, self.n_cols)
# stimulus.opacities      = GridPattern.RepeatAcrossElements([1], self.n_rows, self.n_cols)
stimulus.shapes         = GridPattern.RepeatAcrossElements([Polygon(8), ChangingEllipse])
# stimulus.class_labels   = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
# stimulus.id_labels      = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
# stimulus.mirror_values  = GridPattern.RepeatAcrossElements([""], self._n_rows, self._n_cols)
# stimulus.data           = GridPattern.RepeatAcrossElements(["8"], self._n_rows, self._n_cols)
stimulus.positions = Positions.CreateSineGrid(2,2)
stimulus.Show()

stimulus.SaveSVG("testaudio")

#%%

## Choose number of rows and number of columns
n_rows = 6
n_cols = 6

stimsize = (350,350)

clipshape = Ellipse(position = (stimsize[0]/2,stimsize[1]/2), bounding_box = stimsize)

# stimulus = Grid(n_rows, n_cols, background_color = ["diagonal", "black", "white"], stim_orientation = 30, 
                # stim_mirror_value="vertical", stim_class_label= "right", row_spacing = 40, col_spacing = 40, x_margin = 20, y_margin = (40,50))

# stimulus = Grid(n_rows, n_cols, background_color = ['set', "orange", 'to = "purple", begin = "click", dur = "2s"'], stim_orientation = 30, 
#                 stim_mirror_value="vertical", stim_class_label= "right", row_spacing = 40, col_spacing = 40, x_margin = 20, y_margin = (40,50))

# stimulus = Grid(n_rows, n_cols, background_color = ['animate', "red", 'values = "red;orange;green;blue;indigo;violet;red", begin = "2s", dur = "10s",repeatCount="indefinite"'], stim_orientation = 30, 
#                 stim_mirror_value="vertical", stim_class_label= "right", row_spacing = 40, col_spacing = 40, x_margin = 20, y_margin = (40,50))

stimulus = Grid(n_rows, n_cols, background_color = ['animate', "red", 'values = "red;orange;green;blue;indigo;violet;red", begin = "0s", dur = "10s",repeatCount="indefinite"'], 
                stim_orientation = ['animate', '0', '360', "begin = 'click', dur='4s', additive='sum'"], 
                stim_class_label= "right", row_spacing = 40, col_spacing = 40, size = stimsize, 
                background_shape = clipshape)




## Determine shapes used in the stimulus
## Example shapes: Ellipse, Rectangle, Triangle, Polygon(n_sides = 8), ...
stimulus.shapes = GridPattern.RepeatAcrossColumns([Rectangle, Triangle, Ellipse])

## Determine colors used in the stimulus
colors_to_use = ['#1b9fd8', '#6dd6ff', '#006ca1'] 
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(colors_to_use)

## Determine size of elements in the stimulus
stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns([(30,30)])


stimulus.Show()
stimulus.SaveSVG("testori")

#%%

## Choose number of rows and number of columns
n_rows = 6
n_cols = 6

stimulus = Grid(n_rows, n_cols, background_color = "none", row_spacing = 40, col_spacing = 40)

## Determine shapes used in the stimulus
## Example shapes: Ellipse, Rectangle, Triangle, Polygon(n_sides = 8), ...
stimulus.shapes = GridPattern.RepeatAcrossColumns([Rectangle, Triangle, Ellipse])

## Determine colors used in the stimulus
colors_to_use = ['#1b9fd8', '#6dd6ff', '#006ca1'] 
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(colors_to_use)

## Determine size of elements in the stimulus
stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns([(30,30)])


stimulus.positions.SetLocationJitter("xy", mu = 0, std = 2)

stimulus.Show()
#%%

## Choose number of rows and number of columns
n_rows = 1
n_cols = 1

stimulus = Grid(n_rows, n_cols, background_color = "none")

## Determine shapes used in the stimulus
## Example shapes: Ellipse, Rectangle, Triangle, Polygon(n_sides = 8), ...
stimulus.shapes = GridPattern.RepeatAcrossColumns([Image("https://upload.wikimedia.org/wikipedia/commons/4/49/KU_Leuven_logo.svg")])

## Determine colors used in the stimulus
colors_to_use = ['#1b9fd8'] 
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(colors_to_use)

## Determine size of elements in the stimulus
stimulus.bounding_boxes = GridPattern.RepeatAcrossColumns([(100,100)])

stimulus.Show()
stimulus.SaveSVG(folder = "output", filename = "image")

#%%
def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(round(r*255),round(g*255),round(b*255))

#%% Default grid + change in values after initialization
stimulus = Grid(6,6, background_color = "white", x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RandomPattern([(50,50), (40,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RandomPattern(['#6dd6ff', '#1b9fd8', '#006ca1'])  
#stimulus.bordercolors = GridPattern.RandomPattern(['#6dd6ff', '#1b9fd8', '#006ca1'])  
#stimulus.borderwidths = GridPattern.RandomPattern([5])

stimulus.Show()
stimulus.SavePNG(filename = "test", folder = "output")
stimulus.SavePDF(filename = "test", folder = "output")
stimulus.SaveSVG(filename = "test", folder = "output")

stimulus.positions.SetLocationJitter(distribution = "uniform", min_val = 5, max_val = 40)

random.seed(2)
stimulus.Show()

stimulus._fillcolors.pattern = ["red", "green", "blue"]

random.seed(2)
stimulus.Show()
#stimulus.CalculateCenter()

#%% Default grid with size (this should autocenter on the middle of the figure)
stimulus = Grid(6,6, background_color = "lightgrey", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (40,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.Show()
#print(stimulus.CalculateCenter())

#%% Example swap_distinct_features
stimulus = Grid(6,6, background_color = "lightgrey", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (40,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ["fillcolors"])
stimulus.Show()
#print(stimulus.CalculateCenter())

#%% Image
stimulus = Grid(6,6, background_color = "white", x_margin = 50, y_margin = 50)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.shapes = GridPattern.RepeatAcrossElements([Image("img/checkmark.svg"), Text("TEXT")])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,30), (10,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.Show()
#stimulus.CalculateCenter()
stimulus._fillcolors.pattern
stimulus._fillcolors.patterntype
stimulus._fillcolors.patternorientation

#%% Order and complexity measures
stimulus = Grid(6,6, background_color = "none", x_margin = 50, y_margin = 50)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (40,40),(30,30)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.Show()
print("LOCE = ", Complexity.CalculateElementsLOCE(stimulus, distinction_features = ["bounding_boxes", "fillcolors", "shapes"]))
print("LOC = ", Complexity.CalculateElementsLOC(stimulus, distinction_features = ["bounding_boxes", "fillcolors", "shapes"]))
print("LOCI = ", Complexity.CalculateElementsLOCI(stimulus, distinction_features = ["bounding_boxes", "fillcolors", "shapes"]))

#%% Output files
stimulus = Grid(6,6, background_color = "lightgrey", size =(300,300))
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (40,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.Show()
stimulus.SaveSVG(filename = "testoutput", folder = "output")
stimulus.SaveJSON(folder = "output", filename = "testoutput")

#%% Apply jitter to feature (e.g. orientation)

random.seed(3)   

stimulus = Grid(6,6, background_color = "white", size = (350,350), x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(20,40)])
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
                                                                                   
stimulus.orientations = GridPattern.RepeatAcrossElements([30])
#orientationjitter = Pattern(stimulus.orientations).AddUniformJitter(min_val = -20, max_val = 20)
orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0 , std = 30)
stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)
                                                          
stimulus.Show()

#%%

# remove an element

random.seed(3)

stimulus = Grid(18,18, background_color = "white", col_spacing = 12, row_spacing = 12)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(5,10)])
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
                                                                                   
stimulus.orientations = GridPattern.RepeatAcrossElements([30])
#orientationjitter = Pattern(stimulus.orientations).AddUniformJitter(min_val = -20, max_val = 20)
orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0 , std = 30)
stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)
                                                             
#stimulus.Show()

stimulus.remove_element([2,5])
stimulus.remove_element([10,15])
stimulus.remove_element([16,3])

stimulus.Show()

#%%

# image as shape

random.seed(3)

stimulus = Grid(6,6, background_color = "white", x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Image("img/checkmark.svg", name = "Checkmark")])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,40)])
                                                        
stimulus.orientations = GridPattern.RepeatAcrossElements([30])
#orientationjitter = Pattern(stimulus.orientations).AddUniformJitter(min_val = -20, max_val = 20)
orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0 , std = 30)
stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)
                                                             
stimulus.Show()

stimulus.remove_element([2,6])

stimulus.Show()

#%%

# svg as Path, PathSvg, or Image

# PathSvg: does not work well if other elements (eg rectangle) in the svg (should be paths only); 
# incorrect width and height is assumed, some parts are filled and some not, non-path elements are not shown
# (see problems with test.svg and arrow-circle-up-svgrepo-com.svg)

# use Path in case svg has more than one path; then you can define width and height yourself

# Image: not visible in PNG/PDF/JPG
# data URI possible solution? (datauri package)

random.seed(3)

stimulus = Grid(9,6, background_color = "gainsboro", x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([
        Path('M 100 350 l 150 -300 M 250 50 l 150 300 M 175 200 l 150 0 M 100 350 q 150 -300 300 0', 450, 400), 
        PathSvg("img/test.svg"), 
        Image("img/test.svg"), 
        Path("M12 22A10 10 0 1 0 2 12a10 10 0 0 0 10 10zM8.31 10.14l3-2.86a.49.49 0 0 1 .15-.1.54.54 0 0 1 .16-.1.94.94 0 0 1 .76 0 1 1 0 0 1 .33.21l3 3a1 1 0 0 1-1.42 1.42L13 10.41V16a1 1 0 0 1-2 0v-5.66l-1.31 1.25a1 1 0 0 1-1.38-1.45z", 24,24), 
        PathSvg("img/arrow-circle-up-svgrepo-com.svg"), 
        Image("img/arrow-circle-up-svgrepo-com.svg"), 
        Path("M 256.00,0.00C 114.615,0.00,0.00,114.615,0.00,256.00s 114.615,256.00, 256.00,256.00s 256.00-114.615, 256.00-256.00S 397.385,0.00, 256.00,0.00z M 208.00,416.00L 102.00,278.00l 47.00-49.00l 59.00,75.00 l 185.00-151.00l 23.00,23.00L 208.00,416.00z", 512, 512), 
        PathSvg("img/checkmark.svg"), 
        Image("img/checkmark.svg")])
stimulus.borderwidths = GridPattern.RepeatAcrossRows([2,2,2,0,0,0,2,2,2])
stimulus.bordercolors = GridPattern.RepeatAcrossElements(['black'])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,40)])
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
stimulus.mirror_values = GridPattern.RepeatAcrossColumns(["none", "horizontal", "vertical", "horizontalvertical"])
                                                               
#                                                        
#stimulus.orientations = GridPattern.RepeatAcrossElements([0,30,45])
#orientationjitter = Pattern(stimulus.orientations).AddUniformJitter(min_val = -20, max_val = 20)
#orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0 , std = 30)
#stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)
                                                             
stimulus.Show()
#stimulus.SavePNG("output/pathsvg_in_png")
#stimulus.SaveSVG("output/pathsvg_in_png")

#%%

# Text as shape

random.seed(3)

stimulus = Grid(6,6, background_color = "gainsboro", x_margin = 0, y_margin = 0, row_spacing = 40, col_spacing = 40)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Text("ABC\nB A G"), Text("B"), Rectangle, Text("C")])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,40)])
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
#stimulus.borderwidths = GridPattern.RepeatAcrossRows([2])
#stimulus.bordercolors = GridPattern.RepeatAcrossElements(['green'])
#stimulus.mirror_values = GridPattern.RepeatAcrossColumns(["none", "horizontal", "vertical", "horizontalvertical"])
                                                               
#                                                        
stimulus.orientations = GridPattern.RepeatAcrossElements([0,30,45])
#orientationjitter = Pattern(stimulus.orientations).AddUniformJitter(min_val = -20, max_val = 20)
#orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0 , std = 30)
#stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)
                                                             
stimulus.Show()

#%%

# PATH as shape

random.seed(3)

stimulus = Grid(6,6, background_color = "none", x_margin = 20, y_margin = 20, row_spacing = 40, col_spacing = 40)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([
        Path("M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z", 288,288)])
# path example from https://webkul.com/blog/morphing-using-svg-animate-css/
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,40)])
stimulus.fillcolors = GridPattern.MirrorAcrossColumns(Pattern.CreateColorRangeList( '#006ca1','#6dd6ff', n_elements = 5))
#stimulus.borderwidths = GridPattern.RepeatAcrossRows([2])
#stimulus.bordercolors = GridPattern.RepeatAcrossElements(['green'])
#stimulus.mirror_values = GridPattern.RepeatAcrossColumns(["none", "horizontal", "vertical", "horizontalvertical"])
                                                               
stimulus.orientations = GridPattern.RepeatAcrossElements([135])                                                       
#orientationjitter = Pattern(stimulus.orientations).AddUniformJitter(min_val = -20, max_val = 20)
#orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0 , std = 30)
#stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)
                           
stimulus.positions.x                                  
stimulus.Show()
stimulus.SaveSVG("testpathstimulus", folder = "output")

#%%

# Custom positions elements

random.seed(3)

stimulus = Grid(3,1, background_color = "gainsboro", x_margin = 50, y_margin = 50, row_spacing = 50, col_spacing = 50)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.Show()

x_jitter = [random.uniform(-50, 50) for _ in range(len(stimulus.positions.x))]
y_jitter = [random.uniform(-10, 10) for _ in range(len(stimulus.positions.y))]
new_x = [stimulus.positions.x[i] + x_jitter[i] for i in range(len(stimulus.positions.x))]
new_y = [stimulus.positions.y[i] + y_jitter[i] for i in range(len(stimulus.positions.y))]
stimulus.positions = Positions.CreateCustomPositions(x = new_x, y = new_y)
                                
stimulus.Show()

#%%

# Jitter size relative to bounding box size

random.seed(3)

x_jitterratio = 0
y_jitterratio = 0.5

stimulus = Grid(6,6, background_color = "gainsboro", size = (350,350), row_spacing = 50, col_spacing = 50)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,30),(20,10)])

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([(20,20), (36,36)], 2 , 2),3)
stimulus.bounding_boxes = tiled_grid_1

#tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.RepeatAcrossRows([RegularPolygon(6), Image("img/checkmark.svg")], 2 , 2), (3,3))
#stimulus.shapes = tiled_grid_1
#
#tiled_grid_1 = GridPattern.TiledGrid(GridPattern.RepeatAcrossRows([RegularPolygon(6), Image("img/checkmark.svg")], 2 , 2), (3,3))
#stimulus.shapes = tiled_grid_1

center_grid = GridPattern.RepeatAcrossElements([Image("img/checkmark.svg")], 2, 2)
outer_layers= Pattern([PathSvg("img/checkmark.svg"),
        # Path('M 100 350 l 150 -300 M 250 50 l 150 300 M 175 200 l 150 0 M 100 350 q 150 -300 300 0', 450, 400)])
                        Path("M35.67,19.72a22.05,22.05,0,0,0,3-11.26c-.19-2.92-1.79-6-5.13-6-3.7,0-7.09,3.3-8.48,6.26-1.17,2.5-.41,6.67-4.46,6.8-4-.13-3.29-4.3-4.46-6.8-1.38-3-4.77-6.21-8.47-6.26-3.35,0-4.95,3-5.13,6a22.05,22.05,0,0,0,3,11.26c2.38,4-1.87,6.79-1.06,10.85.6,3,3.47,7.74,6.87,8.05s4.85-6.63,6.17-8.87a3.91,3.91,0,0,1,6.24,0C25,32,26.32,39,29.86,38.63s6.27-5.07,6.87-8.05C37.54,26.51,33.29,23.76,35.67,19.72Z", 41.15, 41.14)])

stimulus.shapes  = GridPattern.LayeredGrid(center_grid, outer_layers)

#stimulus.shapes = GridPattern.MirrorAcrossRightDiagonal([Rectangle, Ellipse])

stimulus.Show()
x_boundingboxes =  [i[0] for i in stimulus.bounding_boxes]
x_maxjitter = [i*x_jitterratio for i in x_boundingboxes]
y_boundingboxes =  [i[1] for i in stimulus.bounding_boxes]
y_maxjitter = [i*y_jitterratio for i in y_boundingboxes]
x_jitter = [random.uniform(-x_maxjitter[_], x_maxjitter[_]) for _ in range(len(stimulus.positions.x))]
y_jitter = [random.uniform(-y_maxjitter[_], y_maxjitter[_]) for _ in range(len(stimulus.positions.y))]
new_x = [stimulus.positions.x[i] + x_jitter[i] for i in range(len(stimulus.positions.x))]
new_y = [stimulus.positions.y[i] + y_jitter[i] for i in range(len(stimulus.positions.y))]
stimulus.positions = Positions.CreateCustomPositions(x = new_x, y = new_y)
                                
stimulus.Show()
stimulus.SaveJSON("test2")
#
stim = Stimulus.LoadFromJSON("test2.json")
##                  
stim.Show()

#%%

# Stimulus without background color

stimulus = Grid(6,6, background_color = "none", size = (350,350), row_spacing = 50, col_spacing = 50)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,40),(20,20)])

stimulus.Show()
stimulus.SaveSVG("testwithoutbackgroundcolor", folder = "output")
stimulus.SavePNG("testwithoutbackgroundcolor", folder = "output")
#%%

# remove_element example

stimulus = Grid(6,6, background_color = "lightgrey", size = (350,350), row_spacing = 50, col_spacing = 50)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,40),(20,20)])

# using row and column index starting from 0
stimulus.remove_element((1,1))
stimulus.Show()

# using element_id starting from 0
stimulus.remove_element(15)
stimulus.Show()

# how this works: putting shape to None
#print(stimulus._attribute_overrides)

#%%

# None shape example

stimulus = Grid(6,6, background_color = "lightgrey", size = (350,350), row_spacing = 50, col_spacing = 50)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossElements([Rectangle, None, Ellipse])

stimulus.Show()


#%%

# mirror example

stimulus = Grid(6,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([Triangle, Ellipse, Rectangle])
stimulus.orientations = GridPattern.RepeatAcrossRows([45])
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(40, 20)])
stimulus.mirror_values = GridPattern.RepeatAcrossColumns(["none", "horizontal", "vertical", "horizontalvertical"])

stimulus.Show()

#%%

# class & id example

stimulus = Grid(1,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Triangle, Ellipse, Rectangle])
stimulus.orientations = GridPattern.RepeatAcrossRows([45])
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(40, 20)])
stimulus.mirror_values = GridPattern.RepeatAcrossColumns(["none", "horizontal", "vertical", "horizontalvertical"])
stimulus.class_labels = GridPattern.RepeatAcrossColumns(["Triangle", "Ellipse", "Rectangle"])
stimulus.id_labels = GridPattern.RepeatAcrossElements(['firstelement', '', '', 'lastelement'])

stimulus.Show()
stimulus.SaveSVG("testclassesids", folder = "output")

#%%

# repeatacrossrows vs repeatacrosscolumns

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Triangle, Ellipse, Rectangle])
stimulus.fillcolors = GridPattern.RepeatAcrossRows(["red", "green", "blue"])
stimulus.Show()

#%%

# complexity measurements

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Triangle, Ellipse, Rectangle])
stimulus.orientations = GridPattern.RepeatAcrossRows([45])
stimulus.Show()

# LOCE: level of element complexity
# Calculate how many different types of elements are present in the display based on the feature dimensions specified in distinction_features.
print("LOCE: " + str(Complexity.CalculateElementsLOCE(stimulus, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors'])))
# LOC: level of complexity
# Calculate how many different features are present across all dimensions.
print("LOC: " + str(Complexity.CalculateElementsLOC(stimulus, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors'])))
# LOCI: level of non-identical complexity
# Calculate how many different feature dimensions have more than one feature value (i.e., have non-identical values).
print("LOCI: " + str(Complexity.CalculateElementsLOCI(stimulus, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors'])))

#%%

# encode png in svg

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image("img/file_example_PNG_500kB.png"), Image("img/w3c_home.png")])

stimulus.Show()
stimulus.SaveSVG("testembeddedpng", folder = "output")

#%%

# encode svg image in svg (including animation!!!)
# WARNING: if animated, not visible in Spyder preview of image!

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image("img/gears.svg"), Image("img/file_example_SVG_20kB.svg")])

stimulus.Show()
stimulus.SaveSVG("testembeddedsvg", folder = "output")


#%%

# encode jpg image in svg

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image("img/w3c_home.jpg"), Image("img/file_example_JPG_100kB.jpg")])

stimulus.Show()
stimulus.SaveSVG("testembeddedjpg", folder = "output")

#%%

# encode bmp image in svg

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image("img/w3c_home.bmp")])

stimulus.Show()
stimulus.SaveSVG("testembeddedbmp", folder = "output")

#%%

# encode gif image in svg (including animation!!!)
# WARNING: if animated, not visible in Spyder preview of image!

stimulus = Grid(4,4, background_color = "none", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image("img/w3c_home.gif"), Image("img/w3c_home_animation.gif")])

stimulus.Show()
stimulus.SaveSVG("testembeddedgif", folder = "output")

#%%

# encode ico image in svg

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image("img/file_example_favicon.ico")])

stimulus.Show()
stimulus.SaveSVG("testembeddedico", folder = "output")

#%%

# encode tiff image in svg

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image("img/file_example_TIFF_1MB.tiff")])

stimulus.Show()
stimulus.SaveSVG("testembeddedtiff", folder = "output")

#%%

# encode webp image in svg

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image("img/file_example_WEBP_50kB.webp")])

stimulus.Show()
stimulus.SaveSVG("testembeddedwebp", folder = "output")

#%%

# encode image from online source in svg (including animation!!!)
# WARNING: image preview in Spyder not always accurate!
# WARNING: if animated, not visible in Spyder preview of image!

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([
        Image("https://media.inkscape.org/media/resources/file/Gears_8IWk3lq.svg"),
        Image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg"), 
        Image("https://upload.wikimedia.org/wikipedia/commons/6/6a/PNG_Test.png"),
        Image("https://upload.wikimedia.org/wikipedia/commons/d/d0/RStudio_logo_flat.svg")])

stimulus.Show()
stimulus.SaveSVG("testembeddedonlineimage", folder = "output")

#%%

# test out how to animate properties (in ChangingEllipse.py)
from octa.shapes import ChangingEllipse

stimulus = Grid(4,4, background_color = "white", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"


stimulus.shapes = GridPattern.RepeatAcrossColumns([ChangingEllipse])
#stimulus.fillcolors = GridPattern.RepeatAcrossColumns(["green", "blue", "orange"])

stimulus.Show()
stimulus.SaveSVG("testanimatesvg", folder = "output")

#%%

# shaping of image

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([
        FitImage("https://media.inkscape.org/media/resources/file/Gears_8IWk3lq.svg"), 
        FitImage("https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg"),
        FitImage("https://upload.wikimedia.org/wikipedia/commons/6/6a/PNG_Test.png"), 
        FitImage("https://upload.wikimedia.org/wikipedia/commons/d/d0/RStudio_logo_flat.svg"),
        Image("https://media.inkscape.org/media/resources/file/Gears_8IWk3lq.svg"), 
        Image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg"),
        Image("https://upload.wikimedia.org/wikipedia/commons/6/6a/PNG_Test.png"), 
        Image("https://upload.wikimedia.org/wikipedia/commons/d/d0/RStudio_logo_flat.svg")])

stimulus.Show()
stimulus.SaveSVG("testscalingimage", folder = "output")

#%%

# gradient fillcolor

stimulus = Grid(5,5, background_color = "none", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

      
stimulus.shapes = GridPattern.RepeatAcrossElements([Ellipse, Rectangle, Triangle, Polygon(8), 
        Path("M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z", 288,288)])
stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.Show()
stimulus.SaveSVG("testgradientellipse", folder = "output")
stimulus.SavePNG("testgradientellipse", folder = "output")

#%%

# gradient bordercolor
from octa.shapes import Ellipse

stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

      
stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,40)])
stimulus.borderwidths = GridPattern.RepeatAcrossRows([10,10,0,10,10])
stimulus.bordercolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], "green", ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.Show()
stimulus.SaveSVG("testgradientellipseborder", folder = "output")

#%%

# use swaps and orientation changes on elements with gradient fill

stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([Ellipse, ChangingEllipse, Triangle, Ellipse])
stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

#stimulus.swap_distinct_elements(n_swap_pairs = 1)
stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['fillcolors'])

stimulus.Show()
stimulus.SaveSVG("test", folder = "output")

#%%

# Test Polygon shapes with n_sides as input 

stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([RegularPolygon(4), RegularPolygon(5), RegularPolygon(6, "Hexagon"), Polygon(6, "Hexagon")])
stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")


#%%

# Test Text shape with text to use as input 
stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([Text("OCTA"), Rectangle, Text("O3"), Text("Hola\nPola", name = "stopexpression"), Polygon(8)])
#stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")

#%%

# Test Image shape with source to use as input 
stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([Image("img/checkmark.svg", name = "Checkmark"), Image("https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg"), FitImage("img/w3c_home.png", name = "W3C_png")])
#stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")

#%%

# # Test Path shape with path and size of path to use as input 
stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows(
        [Path(name = "Arrow", path = "M12 22A10 10 0 1 0 2 12a10 10 0 0 0 10 10zM8.31 10.14l3-2.86a.49.49 0 0 1 .15-.1.54.54 0 0 1 .16-.1.94.94 0 0 1 .76 0 1 1 0 0 1 .33.21l3 3a1 1 0 0 1-1.42 1.42L13 10.41V16a1 1 0 0 1-2 0v-5.66l-1.31 1.25a1 1 0 0 1-1.38-1.45z", xsize = 24, ysize = 24),
          Path(name = "Checkmark", path = "M 256.00,0.00C 114.615,0.00,0.00,114.615,0.00,256.00s 114.615,256.00, 256.00,256.00s 256.00-114.615, 256.00-256.00S 397.385,0.00, 256.00,0.00z M 208.00,416.00L 102.00,278.00l 47.00-49.00l 59.00,75.00 l 185.00-151.00l 23.00,23.00L 208.00,416.00z", xsize = 512, ysize = 512)])
#stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")

#%%

# # Test PathSvg shape with path and size of path to use as input 
stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows(
        [PathSvg("img/checkmark.svg", name = "Checkmark"),
          PathSvg("img/arrow-circle-up-svgrepo-com.svg", name = "Arrow")])
#stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")


#%%

# # Test PathSvg shape with path and size of path to use as input 
stimulus = Grid(5,5, background_color = "none", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows(
        [PathSvg("img/checkmark.svg", name = "Checkmark")])
stimulus.fillcolors = GridPattern.GradientAcrossElements(start_value = "red", end_value = "blue")
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

stimulus.positions.SetLocationJitter("xy", "uniform", min_val = -10, max_val = 10)

#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
#stimulus.SaveSVG("test")


#%%

stimulus = Grid(3,3, background_color = "none", row_spacing = 120, col_spacing = 120)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows(
        [Image("https://live.staticflickr.com/1888/44590255382_677039f088_b.jpg")])
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(100,100)])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90])


#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
stimulus.SaveSVG("test")

#%%

stimulus = Grid(6,6, background_color = "none", row_spacing = 120, col_spacing = 120)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([Polygon(5)])
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements(Pattern.Create2DGradient(Sequence(start = 90, step = -5), Sequence(start = 90, step = -5), 6))
stimulus.orientations = GridPattern.RepeatAcrossColumns(Pattern.CreateNumberRangeList(start_number = 0, end_number = 180, n_elements = 6))


#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()


#%%

stimulus = Grid(6,6, background_color = "none", row_spacing = 120, col_spacing = 120)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([Polygon(5)])
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements(Pattern.Create2DGradient(LinearGradient(start = 50, end = 90, n_elements = 6), 90, 6))
stimulus.orientations = GridPattern.RepeatAcrossColumns(Pattern.CreateNumberRangeList(start_number = 0, end_number = 0, n_elements = 3))


#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()


#%%

backgroundcolor = "none"
stimulus = Grid(6,6, background_color = backgroundcolor, row_spacing = 120, col_spacing = 120)
stimulus.background_color = "blue"
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([Polygon(5)])
stimulus.bounding_boxes = GridPattern.RepeatAcrossElements(Pattern.Create2DGradient(LinearGradient(start = 50, end = 90, n_elements = 6), 90, 6))
stimulus.orientations = GridPattern.RepeatAcrossColumns(Pattern.CreateNumberRangeList(start_number = 0, end_number = 0, n_elements = 3))


#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()


#%%

from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg, ChangingEllipse
stimulus = Grid(4,4, background_color = "none", row_spacing = 50, col_spacing = 50)

stimulus.shapes = GridPattern.RepeatAcrossElements([Ellipse])

stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(50,50)])
#stimulus.orientations = GridPattern.RepeatAcrossElements([['animate', '0', '360', "id='anim1', dur = '4s', begin='0s;anim1.end+6s', additive = 'sum'"],
#                                                          ['animate', '0', '360', "id='anim2', dur = '4s', begin='2s;anim2.end+6s', additive = 'sum'"],
#                                                          ['animate', '0', '360', "id='anim3', dur = '4s', begin='4s;anim3.end+6s', additive = 'sum'"],
#                                                        ['animate', '0', '360', "id='anim4', dur = '4s', begin='6s; anim4.end+6s', additive = 'sum'"]])
##stimulus.fillcolors = GridPattern.RepeatAcrossElements([['set', "orange", 'to = "purple", begin = "click", dur = "2s"']])
#stimulus.fillcolors = GridPattern.RepeatAcrossElements([["radial", "white", "red"], ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"],
#                                                        ['animate', "red", 'values = "red;white;red", begin = "2s", dur = "10s",repeatCount="indefinite"'],
#                                                        ['animate', "red", 'values = "red;orange;green;blue;indigo;violet;red", begin = "2s", dur = "10s",repeatCount="indefinite"'],
#                                                        ['animate', "green", 'values = "green;purple;green", begin = "2s", dur = "10s",repeatCount="indefinite"'],
#                                                        ['animate', "red", 'values = "red;white;red", begin = "2s", dur = "10s",repeatCount="indefinite"'],
#                                                        ['set', "red", 'to = "purple", begin = "2s", dur = "10s"'],
#                                                        ['animate', "red", 'values = "red;orange;green;blue;indigo;violet;red", begin = "2s", calcMode = "discrete", dur = "10s"'],
#                                                        ['set', "green", 'to = "purple", begin = "click", dur = "10s"'],
#                                                        ['set', "red", 'to = "white;red", begin = "2s", dur = "10s"']
#                                                        ])
    
    
stimulus.set_element_shape(10, ChangingEllipse)
#stimulus.set_element_fillcolor(0, "red")
#stimulus.set_element_orientation(0, 30)
stimulus.set_element_shape(9, Path("M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z", 288,288))
stimulus.set_element_bounding_box(10, (48,50))

stimulus.Show()
stimulus.SaveSVG("testsearchwithaudio")
stimulus.SaveJSON("testsearchwithaudio")

# stim = Stimulus.LoadFromJSON("testsearchwithaudio.json")
                  
# stim.Show()
# stim.SaveSVG("testsearchwithaudio")

#%%

from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg, ChangingEllipse
stimulus = Grid(4,4, background_color = "none", row_spacing = 50, col_spacing = 50)

stimulus.shapes = GridPattern.RepeatAcrossElements([ChangingEllipse, #PathSvg("img/checkmark.svg"),
                                                    Path('M35.67,19.72 C490,290, 550,290, 570,240', 500,500),
                                                    Path("M35.67,19.72a22.05,22.05,0,0,0,3-11.26c-.19-2.92-1.79-6-5.13-6-3.7,0-7.09,3.3-8.48,6.26-1.17,2.5-.41,6.67-4.46,6.8-4-.13-3.29-4.3-4.46-6.8-1.38-3-4.77-6.21-8.47-6.26-3.35,0-4.95,3-5.13,6a22.05,22.05,0,0,0,3,11.26c2.38,4-1.87,6.79-1.06,10.85.6,3,3.47,7.74,6.87,8.05s4.85-6.63,6.17-8.87a3.91,3.91,0,0,1,6.24,0C25,32,26.32,39,29.86,38.63s6.27-5.07,6.87-8.05C37.54,26.51,33.29,23.76,35.67,19.72Z", 41.15, 41.14),
                                                    Polygon(5), RegularPolygon(6), 
                                                    Rectangle, Triangle, 
                                                    Text('OCTA'),
                                                    Image("img/checkmark.svg"),
                                                    FitImage("img/checkmark.svg")])

stimulus.bounding_boxes = GridPattern.RepeatAcrossElements([(40,50)])
# stimulus.orientations = GridPattern.RepeatAcrossElements([['animate', '0', '360', "id='anim1', dur = '4s', begin='0s;anim1.end+6s', additive = 'sum'"],
#                                                           ['animate', '0', '360', "id='anim2', dur = '4s', begin='2s;anim2.end+6s', additive = 'sum'"],
#                                                           ['animate', '0', '360', "id='anim3', dur = '4s', begin='4s;anim3.end+6s', additive = 'sum'"],
#                                                         ['animate', '0', '360', "id='anim4', dur = '4s', begin='6s; anim4.end+6s', additive = 'sum'"]])
stimulus.orientations = GridPattern.RepeatAcrossElements([['animate', '0', '360', "id='anim1', dur = '4s', begin='0s', additive = 'sum'"],
                                                          ['animate', '0', '360', "id='anim2', dur = '4s', begin='2s', additive = 'sum'"],
                                                          ['animate', '0', '360', "id='anim3', dur = '4s', begin='4s', additive = 'sum'"],
                                                        ['animate', '0', '360', "id='anim4', dur = '4s', begin='6s', additive = 'sum'"]])#stimulus.fillcolors = GridPattern.RepeatAcrossElements([['set', "orange", 'to = "purple", begin = "click", dur = "2s"']])
stimulus.fillcolors = GridPattern.RepeatAcrossElements([["radial", "white", "red"], ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"],
                                                        ['animate', "red", 'values = "red;white;red", begin = "2s", dur = "10s",repeatCount="indefinite"'],
                                                        ['animate', "red", 'values = "red;orange;green;blue;indigo;violet;red", begin = "2s", dur = "10s",repeatCount="indefinite"'],
                                                        ['animate', "green", 'values = "green;purple;green", begin = "2s", dur = "10s",repeatCount="indefinite"'],
                                                        ['animate', "red", 'values = "red;white;red", begin = "2s", dur = "10s",repeatCount="indefinite"'],
                                                        ['set', "red", 'to = "purple", begin = "2s", dur = "10s"'],
                                                        ['animate', "red", 'values = "red;orange;green;blue;indigo;violet;red", begin = "2s", calcMode = "discrete", dur = "10s"'],
                                                        ['set', "green", 'to = "purple", begin = "click", dur = "10s"'],
                                                        ['set', "red", 'to = "white;red", begin = "2s", dur = "10s"']
                                                        ])
    
    
#stimulus.set_element_shape(0, ChangingEllipse)
#stimulus.set_element_fillcolor(0, "red")
#stimulus.set_element_orientation(0, 30)
# stimulus.set_element_shape(9, Path("M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z", 288,288))
#stimulus.set_element_orientation(2, ['animate', '0', '360', "id='anim2', dur = '4s', begin='0s; anim2.end+4s', additive = 'sum'"])
#stimulus.set_element_shape(1, Image("img/checkmark.svg"))
stimulus.set_element_bounding_box(2, (40,50))
#stimulus.set_element_fillcolor(2, ["horizontal", "blue", "red"])
#stimulus.set_element_fillcolor(5, ['animate', "green", 'values = "green;purple;green", begin = "2s", dur = "10s",repeatCount="indefinite"'])
#stimulus.set_element_orientation(2, ['animate', '0', '90', "dur = '8s', begin='0s',repeatCount='indefinite'"])

#stimulus.set_element_position(2, (20,50))
#stimulus.swap_distinct_elements(n_swap_pairs = 1, distinction_features = ['shapes'])
#stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['shapes'])

stimulus.Show()
stimulus.SaveSVG("testanimation")
stimulus.SaveJSON("testanimation")

# stim = Stimulus.LoadFromJSON("testanimation.json")
                  
# stim.Show()
# stim.SaveSVG("testanimationviajson")