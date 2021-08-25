Overview
========

The OCTA Python toolbox was created by Van Geert, Bossens, and Wagemans (2021) as a tool for researchers to create stimuli varying in order and complexity on different dimensions. 

Stimulus types
---------------

:class:`~octa.Stimulus.Stimulus`, :class:`~octa.Stimulus.Grid`,
:class:`~octa.Stimulus.Outline`, :class:`~octa.Stimulus.Concentric`


Position patterns
------------------

:class:`~octa.Positions.Positions.CreateRectGrid`, 
:class:`~octa.Positions.Positions.CreateSineGrid`,
:class:`~octa.Positions.Positions.CreateRandomPositions`,  
:class:`~octa.Positions.Positions.CreateCircle`, 
:class:`~octa.Positions.Positions.CreateShape`, 
:class:`~octa.Positions.Positions.CreateCustomPositions`


Feature patterns
------------------

:class:`~octa.patterns.GridPattern.RepeatAcrossElements`,
:class:`~octa.patterns.GridPattern.ElementRepeatAcrossElements`,
:class:`~octa.patterns.GridPattern.MirrorAcrossElements`, 
:class:`~octa.patterns.GridPattern.GradientAcrossElements`,
:class:`~octa.patterns.GridPattern.RepeatAcrossRows`,
:class:`~octa.patterns.GridPattern.ElementRepeatAcrossRows`,
:class:`~octa.patterns.GridPattern.MirrorAcrossRows`, 
:class:`~octa.patterns.GridPattern.GradientAcrossRows`,
:class:`~octa.patterns.GridPattern.RepeatAcrossColumns`,
:class:`~octa.patterns.GridPattern.ElementRepeatAcrossColumns`,
:class:`~octa.patterns.GridPattern.MirrorAcrossColumns`, 
:class:`~octa.patterns.GridPattern.GradientAcrossColumns`,
:class:`~octa.patterns.GridPattern.RepeatAcrossLeftDiagonal`,
:class:`~octa.patterns.GridPattern.ElementRepeatAcrossLeftDiagonal`,
:class:`~octa.patterns.GridPattern.MirrorAcrossLeftDiagonal`, 
:class:`~octa.patterns.GridPattern.GradientAcrossLeftDiagonal`,
:class:`~octa.patterns.GridPattern.RepeatAcrossRightDiagonal`,
:class:`~octa.patterns.GridPattern.ElementRepeatAcrossRightDiagonal`,
:class:`~octa.patterns.GridPattern.MirrorAcrossRightDiagonal`, 
:class:`~octa.patterns.GridPattern.GradientAcrossRightDiagonal`,
:class:`~octa.patterns.GridPattern.RepeatAcrossLayers`,
:class:`~octa.patterns.GridPattern.ElementRepeatAcrossLayers`,
:class:`~octa.patterns.GridPattern.MirrorAcrossLayers`, 
:class:`~octa.patterns.GridPattern.GradientAcrossLayers`,
:class:`~octa.patterns.GridPattern.TiledGrid`,
:class:`~octa.patterns.GridPattern.TiledElementGrid`,
:class:`~octa.patterns.GridPattern.RandomPattern`

Features
---------

Shapes
~~~~~~

:class:`~octa.shapes.Ellipse`, :class:`~octa.shapes.Rectangle`,
:class:`~octa.shapes.Triangle`, :func:`~octa.shapes.Polygon`,
:func:`~octa.shapes.RegularPolygon`, :func:`~octa.shapes.Path`,
:func:`~octa.shapes.PathSvg`, :func:`~octa.shapes.Image`,
:func:`~octa.shapes.FitImage`, :func:`~octa.shapes.Text`

Deviations
-----------

Position deviations
~~~~~~~~~~~~~~~~~~~

:func:`~octa.Positions.Positions.SetPositionJitter`, 
:func:`~octa.Positions.Positions.SetPositionDeviations`

Element deviations
~~~~~~~~~~~~~~~~~~~

:func:`~octa.Stimulus.Grid.remove_elements`,
:func:`~octa.Stimulus.Grid.randomize_elements`,
:func:`~octa.Stimulus.Grid.swap_distinct_elements`

Feature deviations
~~~~~~~~~~~~~~~~~~~

:func:`~octa.Stimulus.Grid.swap_distinct_features`,
:func:`~octa.patterns.GridPattern.GridPattern.AddNormalJitter`,
:func:`~octa.patterns.GridPattern.GridPattern.AddUniformJitter`,
:func:`~octa.patterns.GridPattern.GridPattern.RandomizeAcrossElements`, 
:func:`~octa.patterns.GridPattern.GridPattern.RandomizeAcrossRows`, 
:func:`~octa.patterns.GridPattern.GridPattern.RandomizeAcrossColumns`, 
:func:`~octa.patterns.GridPattern.GridPattern.RandomizeAcrossLeftDiagonal`, 
:func:`~octa.patterns.GridPattern.GridPattern.RandomizeAcrossRightDiagonal`, 
:func:`~octa.Stimulus.Grid.set_element_shapes`, 
:func:`~octa.Stimulus.Grid.set_element_boundingboxes`, 
:func:`~octa.Stimulus.Grid.set_element_fillcolors`, 
:func:`~octa.Stimulus.Grid.set_element_orientations`, 
:func:`~octa.Stimulus.Grid.set_element_borderwidths`, 
:func:`~octa.Stimulus.Grid.set_element_bordercolors`, 
:func:`~octa.Stimulus.Grid.set_element_opacities`, 
:func:`~octa.Stimulus.Grid.set_element_mirrorvalues`, 
:func:`~octa.Stimulus.Grid.set_element_links`, 
:func:`~octa.Stimulus.Grid.set_element_classlabels`, 
:func:`~octa.Stimulus.Grid.set_element_idlabels`

Measurements
-------------

Order measures
~~~~~~~~~~~~~~~

:func:`~octa.measurements.Order.GetPatterns`,
:func:`~octa.measurements.Order.GetPatternTypes`,
:func:`~octa.measurements.Order.GetPatternDirections`,
:func:`~octa.measurements.Order.CheckPatternCongruency`,
:func:`~octa.measurements.Order.CheckPatternTypeCongruency`,
:func:`~octa.measurements.Order.CheckPatternDirectionCongruency`,
:func:`~octa.measurements.Order.CalculatePatternCongruency`,
:func:`~octa.measurements.Order.CalculatePatternTypeCongruency`,
:func:`~octa.measurements.Order.CalculatePatternDirectionCongruency`,
:func:`~octa.measurements.Order.CalculatePatternDeviants`,
:func:`~octa.measurements.Order.CalculatePositionDeviants`

Complexity measures
~~~~~~~~~~~~~~~~~~~~

:func:`~octa.measurements.Complexity.CalculateElementsN`,
:func:`~octa.measurements.Complexity.CalculateElementsLOC`,
:func:`~octa.measurements.Complexity.CalculateElementsLOCE`,
:func:`~octa.measurements.Complexity.CalculateElementsLOCI`


Output options
---------------

:func:`~octa.Stimulus.Stimulus.Show`, 
:func:`~octa.Stimulus.Stimulus.GetSVG`, 
:func:`~octa.Stimulus.Stimulus.SaveSVG`, 
:func:`~octa.Stimulus.Stimulus.GetJSON`, 
:func:`~octa.Stimulus.Stimulus.SaveJSON`, 
:func:`~octa.Stimulus.Stimulus.LoadFromJSON`, 
:func:`~octa.Stimulus.Stimulus.SavePNG`, 
:func:`~octa.Stimulus.Stimulus.SaveJPG`, 
:func:`~octa.Stimulus.Stimulus.SavePDF`, 
:func:`~octa.Stimulus.Stimulus.SaveTIFF` 