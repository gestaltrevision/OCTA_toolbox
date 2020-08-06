# **OCTA to do list** (20/07/2020)

## ADDITIONAL PATTERNS / PATTERN FEATURES

### important

* structural change: all grid patterns in same file:
  * add the possibility to switch between patterns
    e.g.:
    stimulus.colors.pattern = RepeatAcrossColumns (instead of eg MirrorAcrossRows)
* make clear in documentation that top->bottom left-> right is standard in OCTA
* naming RepeaterPattern / Duplicate functions: Duplicate/Repeat/Replicate/Iterate/Alternate/...?

### very nice

* extend function for BasicPattern: 
  BasicPattern([1,2,3]) and BasicPattern([4,5,6]) --> BasicPattern([1,2,3,4,5,6])
  bijv.:
  pattern1 = BasicPattern([1,2,3])
  pattern2 = BasicPattern([4,5,6])
  BasicPattern([pattern1, pattern2])

  of bijv.: pattern1.extend([4,5,6])

* additional jitter options:

  * regularly increasing jitter
  * regularly decreasing jitter

* in/out and out/in as additional dimensions 
  (like row/column/leftdiagonal/rightdiagonal)
  thus: repeater/gradient/symmetry patterns along this dimension

* gradient in size working with tuples? (gradient in aspectratio)

* extra deviant options:

  * replace_value (of one feature of an element): arguments = element_id and new_value (feature_dimension could be an additional argument OR could be part of the name of the function, like replace_color)
  * replace_element (& all features of element): arguments = element_id and all new values (for different feature dimensions)
  * IMPLEMENTED: switch_value (like implemented, but not random switch)
  * switch_element (like implemented, but not random switch)
  * add_element
  * [add_value (only if not all features need to be given and defaults are implemented)]


### nice 

* RandomizeAcrossRows / Columns / ... ? (ie randomizeorder but not across whole stimulus; only switch row / column /leftdiag / rightdiag / inout/ outin values)
* add other directions than top->bottom left-> right
* additional jitter options: jitter not on all elements
* extra gradient options?
* better color gradients?
* extra deviant options: transform one, some, or all elements (e.g. change on condition, e.g. = rectangle)
* [let user give structure and apply it to given values? eg alternate (abcb)]

## ADDITIONAL STIMULUS FEATURE DIMENSIONS

### important

* mirror parameter
* class
* id

### nice

* [filltexture?]
* [animate ? (changing attributes across time: moving elements, changing orientation / color / ...)]

## ADDITIONAL POSITIONS / POSITION FUNCTIONS

### important

* Circle: bug in # elements on circle --> Eline implemented quick fix but please check :-)

### very nice 

* patterns in positions: different distances in 1 stimulus (eg regularly increasing x/y distance, symmetric distances, ...)
* distances including shapes vs between shapes
* change positions after initialization: eg. stimulus.positions + 20
* contour only options (eg for grids: only elements on outline) as well as filled options for closed shapes (eg for circle: circle filled with elements)
* Spiral
* different / custom overall shape = specific boundary of the complete pattern (ideally same options as for element shapes) --> look at GERT?

### nice

* [masks = pattern going to infinity and cut (ideally same options as for element shapes)] --> look at GERT?
* [dot lattices as one set of grids?]
* [more curved lines, eg. literature dot lattices Kubovy?]
* [zigzag lattices Peter Claessens]
* [diffeomorphic transformations]



## ADDITIONAL STIMULUS FUNCTIONS

### very nice

* transparent background color? (also png?)

 ### nice

* change orientation of overall pattern?

## SHAPES

CRUCIAL SHAPES: ellipse, rectangle, triangle, polygon, none, image, text, (newshape), (rounded_rectangle, rounded_triangle), (curve)

### important

* triangle: 
  * check function used (now Eline's but can probably be improved)
  * also not equilateral triangles
* text:
  * center text in bounding box
* [curve:]
  * border color same as fill color
* none shape

### very nice

* image: 
  * externe svg code embedden/inladen
  * externe png/jpg inladen???
* converter module bepaling grootte (different parameters possible at initialization --> bounding box params)
* [rounded_rectangle, rounded_triangle, rounded_polygon]
* [spiral]
* [newshape]
  * ook externe code inladen en kleur aanpassen?
* text: 
  * different font types [& sizes]?

## INPUT

OCTA code (= now)

important:

* OCTA json file (implemented now but will need to changed/adapted together with outputfiles and additional functionality toolbox)

### [nice ?]

* [OCTA text file: only element info?]

## OUTPUT

### important 

* inhoud outputfiles verder aanvullen
* json file + json inline
* svg file + svg inline

### very nice

* order & complexity measures (of elements & position = location & orientation)
* [txt file + txt inline]
* png file + png inline / jpg file + jpg inline

### nice

* [OCTA code]

## USER INTERFACE [not part of the toolbox itself]

### important

* Shiny app:
  * also output OCTA code to generate same stimulus in python
* documentation (gitbook via Rmd); look at documentation GERT 

### very nice

* tutorial (learnr tutorial via Rmd)

### nice

* create elements > draggable elements in javascript

## GENERAL ISSUES

### important

* problem with image and text stimuli:
  * can not be switched
  * complexity calculation
* output files verder aanvullen
* clarify use of the word "pattern": 
  * set of values to create ordering with (pattern argument)
  * resulting ordering (RepeaterPattern, SymmetryPattern, etc.)

## EXTRA'S

### very nice 

* **in general: look at consistency options on element and stimulus level**

### [ nice ? ]

* svg.js (https://svgjs.com/docs/3.0/)

## OCTA 2.0: adding on basic functionality

### very nice

* generate range of stimuli
  
  * e.g. give values for each feature dimension + dataframe with different order combinations + names stimuli --> create several svgs
* when generating range of stimuli: html image grid as output option = create_grid function to create combination of several stimuli varying in order & complexity dimensions

* combine different displays / stimuli / elementgroups (e.g. 2 concentric circles with elements); group elements together?
  extend_stimuli

  merge_svg function: does viewbox change as well?

* generate shape with certain level of order / complexity?

### nice

* plot different elements (with different sizes) on top of each other?

* integration online svg database/repository (inject svg + change color):
  * svgrepo (https://www.svgrepo.com/)
  * publicdomainvectors (https://publicdomainvectors.org/en/tag/svg)