# OCTA toolbox

The OCTA Python toolbox was created by Van Geert, Bossens, and Wagemans (2021) as a tool for researchers to create stimuli varying in order and complexity on different dimensions. 
It was created in Python 3.8 and is dependent on the following Python libraries: svgwrite, svg.path, svgpathtools, svgutils, jsonpickle, html2image, svglib, reportlab, colour, and IPython. 
We thank the developers of each of these libraries and of the Python programming language.

## Install OCTA

```
pip install octa
```

## Use OCTA

A simple example:

```
from octa.Stimulus import Grid
from octa.patterns import GridPattern
from octa.shapes import Ellipse, Rectangle, Triangle

## Create new stimulus
stim = Grid(n_rows = 6, n_cols = 6, background_color = "none",
            row_spacing = 40, col_spacing = 40)

## Determine shape of elements used in the stimulus
stim.shapes = GridPattern.RepeatAcrossColumns([Rectangle, Triangle, Ellipse])

## Determine color of elements used in the stimulus
colors_to_use = ["#1b9fd8", "#6dd6ff", "#006ca1"]
stim.fillcolors = GridPattern.RepeatAcrossColumns(colors_to_use)

## Determine size of elements used in the stimulus
stim.boundingboxes = GridPattern.RepeatAcrossColumns([(30,30)])

stim.Show()
```

## OCTA Shiny app
A graphical user interface for OCTA is available in the form of a [Shiny app](https://elinevg.shinyapps.io/OCTA_toolbox/).

## Cite OCTA
If you use the **OCTA Python toolbox** in your (academic) work, please cite:
* Van Geert, E., Bossens, C., & Wagemans, J. (2022). The Order & Complexity Toolbox for Aesthetics (OCTA): A systematic approach to study the relations between order, complexity, and aesthetic appreciation. [https://doi.org/10.31234/osf.io/2bu8a](https://doi.org/10.31234/osf.io/2bu8a)
* Van Geert, E., Bossens, C., & Wagemans, J. (2021). The Order & Complexity Toolbox for Aesthetics Python library [Computer software]. [https://github.com/gestaltrevision/OCTA_toolbox](https://github.com/gestaltrevision/OCTA_toolbox)

If you use the **OCTA Shiny app** in your (academic) work, please cite:
* Van Geert, E., Bossens, C., & Wagemans, J. (2022). The Order & Complexity Toolbox for Aesthetics (OCTA): A systematic approach to study the relations between order, complexity, and aesthetic appreciation. [https://doi.org/10.31234/osf.io/2bu8a](https://doi.org/10.31234/osf.io/2bu8a)
* Van Geert, E., Bossens, C., & Wagemans, J. (2021). The Order & Complexity Toolbox for Aesthetics Shiny application [Online application]. [https://elinevg.shinyapps.io/OCTA_toolbox/](https://elinevg.shinyapps.io/OCTA_toolbox/)

## Documentation
Human-readable documentation: https://elinevg.github.io/OCTA_manual/

Computer-readable documentation: https://elinevg.github.io/OCTA_docs/

## License
The OCTA Python toolbox is licensed under the terms of the [GNU Lesser General Public License 3.0](https://choosealicense.com/licenses/lgpl-3.0/).

## Contact
[eline.vangeert@kuleuven.be](mailto:eline.vangeert@kuleuven.be)
