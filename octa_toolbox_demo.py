# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:31:15 2020

@author: Christophe
"""
from octa.Stimulus import Grid, Stimulus
from octa.Positions import Positions
from octa.patterns import GridPattern, Pattern
from octa.shapes import Ellipse, Rectangle, Triangle, Image, FitImage, Text, Polygon, RegularPolygon, Path, PathSvg
from octa.measurements import Complexity
import random

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
stimulus.SavePNG(filename = "output/test")
stimulus.SavePDF(filename = "output/test")
stimulus.SaveSVG(filename = "output/test")

random.seed(2)
stimulus.positions.SetLocationJitter(distribution = "uniform", min_val = 5, max_val = 40)

stimulus.Show()

random.seed(2)
stimulus._fillcolors.pattern = ["red", "green", "blue"]

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
stimulus.shapes = GridPattern.RepeatAcrossElements([Image, Text])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,30), (10,40),(30,30), (20,20)])
stimulus.fillcolors = GridPattern.RepeatAcrossColumns(['#6dd6ff', '#1b9fd8', '#006ca1'])
stimulus.data = GridPattern.RepeatAcrossElements(["img/test.jpg", "TEXT"])
stimulus.Show()
#stimulus.CalculateCenter()
stimulus._fillcolors.pattern
stimulus._fillcolors.patterntype
stimulus._fillcolors.patternorientation

#%% Order and complexity measures
stimulus = Grid(6,6, background_color = "lightgrey", x_margin = 50, y_margin = 50)
stimulus._autosize_method = "maximum_bounding_box"
#stimulus._autosize_method = "tight_fit"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(50,50), (40,40),(30,30), (20,20)])
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
stimulus.SaveSVG(filename = "output/testoutput")
stimulus.SaveJSON(folder = "output", filename = "testoutput")

#%% Apply jitter to feature (e.g. orientation)

#%%
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

stimulus.remove_element(2)

stimulus.Show()

#%%

# image as shape

random.seed(3)

stimulus = Grid(6,6, background_color = "white", x_margin = 0, y_margin = 0)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Image])
stimulus.data = GridPattern.RepeatAcrossElements(["img/checkmark.svg"])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,40)])
                                                        
stimulus.orientations = GridPattern.RepeatAcrossElements([30])
#orientationjitter = Pattern(stimulus.orientations).AddUniformJitter(min_val = -20, max_val = 20)
orientationjitter = Pattern(stimulus.orientations).AddNormalJitter(mu = 0 , std = 30)
stimulus.orientations = GridPattern.RepeatAcrossElements(orientationjitter)
                                                             
stimulus.Show()

stimulus.remove_element(2)

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
stimulus.shapes = GridPattern.RepeatAcrossRows([Path, PathSvg, Image, Path, PathSvg, Image, Path, PathSvg, Image])
stimulus.data = GridPattern.RepeatAcrossRows([('M 100 350 l 150 -300 M 250 50 l 150 300 M 175 200 l 150 0 M 100 350 q 150 -300 300 0', 450, 400), 
                                              "img/test.svg", "img/test.svg",
                                              ("M12 22A10 10 0 1 0 2 12a10 10 0 0 0 10 10zM8.31 10.14l3-2.86a.49.49 0 0 1 .15-.1.54.54 0 0 1 .16-.1.94.94 0 0 1 .76 0 1 1 0 0 1 .33.21l3 3a1 1 0 0 1-1.42 1.42L13 10.41V16a1 1 0 0 1-2 0v-5.66l-1.31 1.25a1 1 0 0 1-1.38-1.45z", 24,24),
                                              "img/arrow-circle-up-svgrepo-com.svg", 
                                              "img/arrow-circle-up-svgrepo-com.svg",
                                              ("M 256.00,0.00C 114.615,0.00,0.00,114.615,0.00,256.00s 114.615,256.00, 256.00,256.00s 256.00-114.615, 256.00-256.00S 397.385,0.00, 256.00,0.00z M 208.00,416.00L 102.00,278.00l 47.00-49.00l 59.00,75.00 l 185.00-151.00l 23.00,23.00L 208.00,416.00z", 512, 512),
                                              "img/checkmark.svg",
                                              "img/checkmark.svg"])
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
stimulus.shapes = GridPattern.RepeatAcrossRows([Text, Rectangle])
stimulus.data = GridPattern.RepeatAcrossRows(["ABC\nB A G", "B", "C"])
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

stimulus = Grid(6,6, background_color = "gainsboro", x_margin = 50, y_margin = 50, row_spacing = 40, col_spacing = 40)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.shapes = GridPattern.RepeatAcrossRows([Path])
# path example from https://webkul.com/blog/morphing-using-svg-animate-css/
stimulus.data = GridPattern.RepeatAcrossRows([("M37.5,186c-12.1-10.5-11.8-32.3-7.2-46.7c4.8-15,13.1-17.8,30.1-36.7C91,68.8,83.5,56.7,103.4,45 c22.2-13.1,51.1-9.5,69.6-1.6c18.1,7.8,15.7,15.3,43.3,33.2c28.8,18.8,37.2,14.3,46.7,27.9c15.6,22.3,6.4,53.3,4.4,60.2 c-3.3,11.2-7.1,23.9-18.5,32c-16.3,11.5-29.5,0.7-48.6,11c-16.2,8.7-12.6,19.7-28.2,33.2c-22.7,19.7-63.8,25.7-79.9,9.7 c-15.2-15.1,0.3-41.7-16.6-54.9C63,186,49.7,196.7,37.5,186z", 288,288)])
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

tiled_grid_1 = GridPattern.TiledElementGrid(GridPattern.MirrorAcrossRightDiagonal([Rectangle, Ellipse], 2 , 2),3)
stimulus.shapes = tiled_grid_1

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

#%%

# Stimulus without background color

stimulus = Grid(6,6, background_color = "None", size = (350,350), row_spacing = 50, col_spacing = 50)
stimulus._autosize_method = "maximum_bounding_box"
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,40),(20,20)])

stimulus.Show()
# stimulus.SaveSVG("test")

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
print(stimulus._attribute_overrides)

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
stimulus.SaveSVG("testclassesids")

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

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image])
stimulus.data = GridPattern.RepeatAcrossColumns(["img/file_example_PNG_500kB.png", "img/w3c_home.png"])

stimulus.Show()
stimulus.SaveSVG("testembeddedpng")

#%%

# encode svg image in svg (including animation!!!)
# WARNING: if animated, not visible in Spyder preview of image!

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image])
stimulus.data = GridPattern.RepeatAcrossColumns(["img/gears.svg", "img/file_example_SVG_20kB.svg"])

stimulus.Show()
stimulus.SaveSVG("testembeddedsvg")


#%%

# encode jpg image in svg

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image])
stimulus.data = GridPattern.RepeatAcrossColumns(["img/w3c_home.jpg", "img/file_example_JPG_100kB.jpg"])

stimulus.Show()
stimulus.SaveSVG("testembeddedjpg")

#%%

# encode bmp image in svg

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image])
stimulus.data = GridPattern.RepeatAcrossColumns(["img/w3c_home.bmp"])

stimulus.Show()
stimulus.SaveSVG("testembeddedbmp")

#%%

# encode gif image in svg (including animation!!!)
# WARNING: if animated, not visible in Spyder preview of image!

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image])
stimulus.data = GridPattern.RepeatAcrossColumns(["img/w3c_home.gif", "img/w3c_home_animation.gif"])

stimulus.Show()
stimulus.SaveSVG("testembeddedgif")

#%%

# encode ico image in svg

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image])
stimulus.data = GridPattern.RepeatAcrossColumns(["img/file_example_favicon.ico"])

stimulus.Show()
stimulus.SaveSVG("testembeddedico")

#%%

# encode tiff image in svg

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image])
stimulus.data = GridPattern.RepeatAcrossColumns(["img/file_example_TIFF_1MB.tiff"])

stimulus.Show()
stimulus.SaveSVG("testembeddedtiff")
#%%

# encode webp image in svg

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image])
stimulus.data = GridPattern.RepeatAcrossColumns(["img/file_example_WEBP_50kB.webp"])

stimulus.Show()
stimulus.SaveSVG("testembeddedwebp")


#%%

# encode image from online source in svg (including animation!!!)
# WARNING: image preview in Spyder not always accurate!
# WARNING: if animated, not visible in Spyder preview of image!

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossColumns([Image])
stimulus.data = GridPattern.RepeatAcrossColumns(["https://media.inkscape.org/media/resources/file/Gears_8IWk3lq.svg", "https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg", "https://upload.wikimedia.org/wikipedia/commons/6/6a/PNG_Test.png", "https://upload.wikimedia.org/wikipedia/commons/d/d0/RStudio_logo_flat.svg"])

stimulus.Show()
stimulus.SaveSVG("testembeddedonlineimage")

#%%

# test out how to animate properties (in ChangingEllipse.py)
from octa.shapes import ChangingEllipse

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"


stimulus.shapes = GridPattern.RepeatAcrossColumns([ChangingEllipse])
#stimulus.fillcolors = GridPattern.RepeatAcrossColumns(["green", "blue", "orange"])

stimulus.Show()
stimulus.SaveSVG("testanimatesvg")


#%%

# shaping of image

stimulus = Grid(4,4, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([Image, FitImage])
stimulus.data = GridPattern.RepeatAcrossColumns(["https://media.inkscape.org/media/resources/file/Gears_8IWk3lq.svg", "https://upload.wikimedia.org/wikipedia/commons/b/bd/Test.svg", "https://upload.wikimedia.org/wikipedia/commons/6/6a/PNG_Test.png", "https://upload.wikimedia.org/wikipedia/commons/d/d0/RStudio_logo_flat.svg"])

stimulus.Show()
stimulus.SaveSVG("testscalingimage")

#%%

# gradient fillcolor
from octa.shapes import GradientEllipse

stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

      
stimulus.shapes = GridPattern.RepeatAcrossRows([GradientEllipse])
stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.Show()
stimulus.SaveSVG("testgradientellipse")

#%%

# gradient bordercolor
from octa.shapes import GradientEllipse

stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

      
stimulus.shapes = GridPattern.RepeatAcrossRows([GradientEllipse])
stimulus.bounding_boxes = GridPattern.RepeatAcrossRows([(40,40)])
stimulus.borderwidths = GridPattern.RepeatAcrossRows([10,10,0,10,10])
stimulus.bordercolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], "green", ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.Show()
stimulus.SaveSVG("testgradientellipseborder")


#%%

# use swaps and orientation changes on elements with gradient fill
from octa.shapes import GradientEllipse

stimulus = Grid(5,5, background_color = "lightgrey", row_spacing = 60, col_spacing = 60)
stimulus._autosize_method = "maximum_bounding_box"

stimulus.shapes = GridPattern.RepeatAcrossRows([GradientEllipse, ChangingEllipse, Triangle, Ellipse])
stimulus.fillcolors = GridPattern.RepeatAcrossRows([["radial", "white", "red"], "green", ["horizontal", "red", "orange", "green", "blue", "indigo", "violet"], ["vertical", "green", "white", "green"], ["diagonal", "red", "white"]])
stimulus.orientations = GridPattern.RepeatAcrossColumns([0,45,90,115,180])

#stimulus.swap_distinct_elements(n_swap_pairs = 1)
stimulus.swap_distinct_features(n_swap_pairs = 1, feature_dimensions = ['fillcolors'])

stimulus.Show()
stimulus.SaveSVG("test")