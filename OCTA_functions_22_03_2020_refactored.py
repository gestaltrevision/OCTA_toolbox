# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:21:35 2019
OCTA: Order & Complexity Toolbox for Aesthetics
@author: Eline Van Geert
"""

# Import necessary libraries 
import os
import svgwrite
import numpy as np
import pandas as pd
import colour
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import svgutils.transform as st
import json

import GradientPattern
import RepeaterPattern
import SymmetryPattern

### CREATE JSON FILE
def create_pattern_json(template = "grid",
                   shape = ['rectangle'], 
                   image = ["none"], #'../vector_images/hotdog.svg',
                   text = ["none"],
                   nrows = 5, ncols = 5,
                   startx = 30, starty = 30,
                   xdist = 30, ydist = 30,
                   shapemirror = ['none'],
                   orientation = [0],
                   shapecolour = ["blue"],
                   repeateachcolor = 1,
                   colourpattern = 'identity',
                   colourdim = 'element',
                   repeateachshape = 1,
                   shapepattern = 'identity',
                   shapedim = 'element',
                   repeateachshapeorientation = 1,
                   shapeorientationpattern = 'identity',
                   shapeorientationdim = 'element',
                   shapesize = [20],
                   shapexyratio = [1],
                   jitterscale = [0],
                   writedir = "OCTA_stimuli"):
     
    # If folder for .json-files does not exist yet, create folder
    if not os.path.exists(writedir + '/json/'):
        os.makedirs(writedir + '/json/')
            
    imgs = os.listdir('OCTA_stimuli/json/')
    
    # LOCATIONS
    
    if template == "grid":  
        x = np.tile(np.arange(startx, startx + xdist*ncols, xdist), reps = nrows)
        y = np.repeat(np.arange(starty, starty + ydist*nrows, ydist), repeats = ncols)
    elif template == "sine":
        x = np.tile(np.arange(startx, startx + xdist*ncols, xdist), reps = nrows)
        y = np.repeat(np.arange(starty, starty + ydist*nrows, ydist), repeats = ncols) - np.sin(x)*(shapesize)
    elif template == "cosine":
        x = np.tile(np.arange(startx, startx + xdist*ncols, xdist), reps = nrows)
        y = np.repeat(np.arange(starty, starty + ydist*nrows, ydist), repeats = ncols) - np.cos(x)*(shapesize)
    elif template == "circle":
        x = startx + xdist * np.cos(2*np.pi*np.arange(1, ncols+1, 1)/ncols)
        y = starty + xdist * np.sin(2*np.pi*np.arange(1, ncols+1, 1)/ncols)
    elif template == "unity":
        x = np.repeat(startx, repeats = nrows*ncols)
        y = np.repeat(starty, repeats = nrows*ncols)

    # Calculate dimensions resulting image
    max_x = float(max(x) + xdist)
    max_y = float(max(y) + ydist)
    
    # Naming of output image 
    jsonfilename = (writedir + '/json/test.json')
      
    # BACKGROUND COLOR 
#    dwg.add(dwg.rect(insert=(0, 0), size=('1530', '530'), rx=None, ry=None, fill='lightgrey'))
    
    ### COMPLEXITY ###
    
    ## IN LOCATION ##
    
    # ADD JITTER
    xjitter = np.random.normal(loc = 0, scale = jitterscale, size = nrows*ncols)
    x = x + xjitter
    yjitter = np.random.normal(loc = 0, scale = jitterscale, size = nrows*ncols)
    y = y + yjitter
    
    ## IN COLOUR ##
    
    # COLOUR
    if colourpattern == "gradient":
        gradient_pattern = GradientPattern.GridGradient(shapecolour[0], shapecolour[1], nrows, ncols)
        
        if colourdim == "element":
            col = gradient_pattern.GradientElements().pattern
            
        elif colourdim == "row":
            col = gradient_pattern.GradientAcrossRows().pattern
            
        elif colourdim == "col":
            col = gradient_pattern.GradientAcrossColumns().pattern
            
        elif colourdim == "rightdiag":
            col = gradient_pattern.GradientAcrossRightDiagonal().pattern
                
        elif colourdim == "leftdiag":
            col = gradient_pattern.GradientAcrossLeftDiagonal().pattern
        
    elif colourpattern == "repeateach":
        repeater_pattern = RepeaterPattern.GridRepeater(shapecolour, nrows, ncols)
        
        if colourdim == "element":
            col = repeater_pattern.RepeatElements().pattern            
            
        elif colourdim == "row":
            col = repeater_pattern.RepeatAcrossRows().pattern
            
        elif colourdim == "col":
            col = repeater_pattern.RepeatAcrossColumns().pattern

        elif colourdim == "rightdiag":
            col = repeater_pattern.RepeatAcrossRightDiagonal().pattern
                
        elif colourdim == "leftdiag":
            col = repeater_pattern.RepeatAcrossLeftDiagonal().pattern
                
    elif colourpattern == "symmetric":
        symmetry_pattern = SymmetryPattern.SymmetryPattern(shapecolour, nrows, ncols)
        
        if colourdim == "element":
            col = symmetry_pattern.MirrorElements().pattern
            
        elif colourdim == "row":
            col = symmetry_pattern.MirrorAcrossColumns().pattern
            
        elif colourdim == "col":
            col = symmetry_pattern.MirrorAcrossRows().pattern

        elif colourdim == "rightdiag":
            col = symmetry_pattern.MirrorAcrossRightDiagonal().pattern

        elif colourdim == "leftdiag":
            col = symmetry_pattern.MirrorAcrossLeftDiagonal().pattern
               
    elif colourpattern == "identity":
        col = np.resize(shapecolour, [nrows*ncols,1]).flatten()
        
    elif colourpattern == "random":
        col = np.resize(shapecolour, [nrows*ncols,1]).flatten()
        np.random.shuffle(col)

    ## IN SIZE ##
    
    # SIZE
    # create list that is as long as number of elements in grid (nrows * ncols)
    size = np.resize(shapesize, [nrows*ncols,1]).flatten()
        
    ## IN shapeorientation ##
    
    # shapeorientation
        
    if shapeorientationpattern == "repeateach":
        repeater_pattern = RepeaterPattern.GridRepeater(orientation, nrows, ncols)
        shapeorientation = repeater_pattern.GenerateOnAxis(shapeorientationdim)
                
    elif shapeorientationpattern == "symmetric":
        symmetry_pattern = SymmetryPattern.SymmetryPattern(orientation, nrows, ncols)
        shapeorientation = symmetry_pattern.GenerateOnAxis(shapeorientationdim)
               
    elif shapeorientationpattern == "identity":
        # create list that is as long as number of elements in grid (nrows * ncols)
        shapeorientation = np.resize(orientation, [nrows*ncols,1]).flatten()
        
    elif shapeorientationpattern == "random":
        # create list that is as long as number of elements in grid (nrows * ncols)
        shapeorientation = np.resize(orientation, [nrows*ncols,1]).flatten()
        np.random.shuffle(shapeorientation)
        
    ## IN SHAPE ##
    
    if shapepattern == "repeateach":
        repeater_pattern = RepeaterPattern.GridRepeater(shape, nrows, ncols)
        elementshape     = repeater_pattern.GenerateOnAxis(shapedim)
                
    elif shapepattern == "symmetric":        
        symmetry_pattern = SymmetryPattern.SymmetryPattern(shape, nrows, ncols)
        elementshape = symmetry_pattern.GenerateOnAxis(shapedim)
    
    elif shapepattern == "identity":
        # create list that is as long as number of elements in grid (nrows * ncols)
        elementshape = np.resize(shape, [nrows*ncols,1]).flatten()
    
    elif shapepattern == "random":
        # create list that is as long as number of elements in grid (nrows * ncols)
        elementshape = np.resize(shape, [nrows*ncols,1]).flatten()
        np.random.shuffle(elementshape)
        
    text = np.resize(text, [nrows*ncols,1]).flatten()
    
    image = np.resize(image, [nrows*ncols,1]).flatten()
    
    # add image info
    
    n = 0
    img = np.repeat(None, (nrows*ncols))
    for i in range(nrows*ncols):
        if elementshape[i] == 'image': 
            img[i] = image[n]
            n += 1
    
    # add text info
    
    n = 0
    txt = np.repeat(None, (nrows*ncols))
    for i in range(nrows*ncols):
        if elementshape[i] == 'text': 
            txt[i] = text[n]
            n += 1
    
    # create list that is as long as number of elements in grid (nrows * ncols)    
    xyratioshape = np.resize(shapexyratio, [nrows*ncols,1]).flatten()
        
    ## TRANSLATION (HORIZONTAL, VERTICAL, HORIZONTALVERTICAL)
    
    # create list that is as long as number of elements in grid (nrows * ncols)
    mirror = np.resize(shapemirror, [nrows*ncols,1]).flatten() 
    
    # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
    data = {}
    data['display'] = []
    data['display'].append({
                       'template': template, 
                       'max_x': max_x,
                       'max_y': max_y,
                       'xdist': xdist,
                       'ydist': ydist,
                       'shaperepeat': repeateachshape,
                       'colourpattern': colourpattern,
                       'colourdim': colourdim,
                       'colourrepeat': repeateachcolor})
    
    data['elements'] = []
#    df = pd.DataFrame({
#                   'number': range(1,nrows*ncols+1), 
#                   'column': np.array(list(np.arange(1, ncols+1, 1)) * nrows),
#                   'row': np.repeat(np.arange(1, nrows+1, 1), repeats = ncols),
#                   'x': x,
#                   'y': y,
#                   'xjitter': xjitter,
#                   'yjitter': yjitter,
#                   'shape': elementshape,
#                   'img': img,
#                   'txt': txt,
#                   'xyratio': xyratioshape,
#                   'colour': col,
#                   'size': size,
#                   'shapeorientation': shapeorientation,
#                   'mirror': mirror
#                   })
#    data['elements'] = df.to_json(orient='index')
#    # https://stackoverflow.com/questions/11942364/typeerror-integer-is-not-json-serializable-when-serializing-json-in-python
    data['elements'].append({
                       'number': list(range(1,nrows*ncols+1)), 
                       'column': list(map(int, np.array(list(np.arange(1, ncols+1, 1)) * nrows))),
                       'row': list(map( int, np.repeat(np.arange(1, nrows+1, 1), repeats = ncols))),
                       'x': list(x),
                       'y': list(y),
                       'xjitter': list(xjitter),
                       'yjitter': list(yjitter),
                       'shape': list(elementshape),
                       'img': list(img),
                       'txt': list(txt),
                       'xyratio': list(map(float, xyratioshape)),
                       'colour': list(col),
                       'size': list(map(int, size)),
                       'shapeorientation': list(map(int,shapeorientation)),
                       'mirror': list(mirror)})  
        
    # write JSON file
    with open(jsonfilename, 'w') as outfile:
        json.dump(data, outfile, indent = 4)
    #data.to_csv(txtfilename, index = False, header = True, sep = "|")
    
#    data = pd.read_csv(writedir + '/txt/' + str(len(imgs)+1).zfill(8) +'.txt', sep='|')

### CREATE JSON 
def create_pattern_json_inline(template = "grid",
                   shape = ['rectangle'], 
                   image = ["none"], #'../vector_images/hotdog.svg',
                   text = ["none"],
                   nrows = 5, ncols = 5,
                   startx = 30, starty = 30,
                   xdist = 30, ydist = 30,
                   shapemirror = ['none'],
                   orientation = [0],
                   shapecolour = ["blue"],
                   repeateachcolor = 1,
                   colourpattern = 'identity',
                   colourdim = 'element',
                   repeateachshape = 1,
                   shapepattern = 'identity',
                   shapedim = 'element',
                   repeateachshapeorientation = 1,
                   shapeorientationpattern = 'identity',
                   shapeorientationdim = 'element',
                   shapesize = [20],
                   shapexyratio = [1],
                   jitterscale = [0],
                   writedir = "OCTA_stimuli"):
       
    # LOCATIONS
    
    if template == "grid":  
        x = np.tile(np.arange(startx, startx + xdist*ncols, xdist), reps = nrows)
        y = np.repeat(np.arange(starty, starty + ydist*nrows, ydist), repeats = ncols)
    elif template == "sine":
        x = np.tile(np.arange(startx, startx + xdist*ncols, xdist), reps = nrows)
        y = np.repeat(np.arange(starty, starty + ydist*nrows, ydist), repeats = ncols) - np.sin(x)*(shapesize)
    elif template == "cosine":
        x = np.tile(np.arange(startx, startx + xdist*ncols, xdist), reps = nrows)
        y = np.repeat(np.arange(starty, starty + ydist*nrows, ydist), repeats = ncols) - np.cos(x)*(shapesize)
    elif template == "circle":
        x = startx + xdist * np.cos(2*np.pi*np.arange(1, ncols+1, 1)/ncols)
        y = starty + xdist * np.sin(2*np.pi*np.arange(1, ncols+1, 1)/ncols)
    elif template == "unity":
        x = np.repeat(startx, repeats = nrows*ncols)
        y = np.repeat(starty, repeats = nrows*ncols)

    # Calculate dimensions resulting image
    max_x = float(max(x) + xdist)
    max_y = float(max(y) + ydist)
      
    # BACKGROUND COLOR 
#    dwg.add(dwg.rect(insert=(0, 0), size=('1530', '530'), rx=None, ry=None, fill='lightgrey'))
    
    ### COMPLEXITY ###
    
    ## IN LOCATION ##
    
    # ADD JITTER
    xjitter = np.random.normal(loc = 0, scale = jitterscale, size = nrows*ncols)
    x = x + xjitter
    yjitter = np.random.normal(loc = 0, scale = jitterscale, size = nrows*ncols)
    y = y + yjitter
    
    ## IN COLOUR ##
    
    # COLOUR
    if colourpattern == "gradient":
        
        startcol = colour.Color(shapecolour[0])
        endcol = colour.Color(shapecolour[1])
        
        if colourdim == "element":
            gradient = list(startcol.range_to(endcol, int((nrows * ncols))))
            colors = {}
            for i in range(len(gradient)):
                colors[i] = gradient[i].hex
            col = list(colors.values())
            
        elif colourdim == "row":
            gradient = list(startcol.range_to(endcol, int(nrows)))
            colors = {}
            for i in range(len(gradient)):
                colors[i] = gradient[i].hex
            col = np.repeat(list(colors.values()), repeats = ncols)      
            
        elif colourdim == "col":
            gradient = list(startcol.range_to(endcol, int(ncols)))
            colors = {}
            for i in range(len(gradient)):
                colors[i] = gradient[i].hex
            col = np.tile(list(colors.values()), reps = nrows)
            
        elif colourdim == "rightdiag":
            gradient = list(startcol.range_to(endcol, int((nrows+ncols)-1)))
            colors = {}
            for i in range(len(gradient)):
                colors[i] = gradient[i].hex
            
            col = np.array(list(colors.values())[:ncols])
            for i in range(1,nrows):
                col = np.append(col, np.roll(list(colors.values()), -i)[:ncols])
                
        elif colourdim == "leftdiag":
            gradient = list(startcol.range_to(endcol, int((nrows+ncols)-1)))
            colors = {}
            for i in range(len(gradient)):
                colors[i] = gradient[i].hex
            
            col = np.array(list(colors.values())[:ncols])[::-1]
            for i in range(1,nrows):
                col = np.append(col, np.roll(list(colors.values()), -i)[:ncols][::-1])
        
    elif colourpattern == "repeateach":
        shapecolour = list(np.repeat(shapecolour, repeateachcolor))
        
        if colourdim == "element":
            # create list that is as long as number of elements in grid (nrows * ncols)
            col = np.array(shapecolour * int((nrows * ncols) / len(shapecolour)))
            if ((nrows * ncols) % len(shapecolour) != 0):
                col = np.append(col, shapecolour[0:(nrows * ncols) % len(shapecolour)]) 
            
        elif colourdim == "row":
            # create list that is as long as number of elements in grid (nrows * ncols)
            col = np.array(shapecolour * int((ncols) / len(shapecolour)))
            if ((ncols) % len(shapecolour) != 0):
                col = np.append(col, shapecolour[0:(ncols) % len(shapecolour)]) 
                
            col = np.tile(col, reps = nrows)
            
        elif colourdim == "col":
            # create list that is as long as number of elements in grid (nrows * ncols)
            col = np.array(shapecolour * int((nrows) / len(shapecolour)))
            if ((nrows) % len(shapecolour) != 0):
                col = np.append(col, shapecolour[0:(nrows) % len(shapecolour)]) 
                
            col = np.repeat(col, repeats = ncols)

        elif colourdim == "rightdiag":
            colors = np.array(shapecolour * int((nrows+ncols)-1 / len(shapecolour)))
            if (((nrows+ncols)-1) % len(shapecolour) != 0):
                colors = np.append(colors, shapecolour[0:((nrows+ncols)-1) % len(shapecolour)]) 
                     
            col = colors[:ncols]
            for i in range(1,nrows):
                col = np.append(col, np.roll(colors, -i)[:ncols])
                
        elif colourdim == "leftdiag":
            colors = np.array(shapecolour * int((nrows+ncols)-1 / len(shapecolour)))
            if (((nrows+ncols)-1) % len(shapecolour) != 0):
                colors = np.append(colors, shapecolour[0:((nrows+ncols)-1) % len(shapecolour)]) 
                     
            col = colors[:ncols][::-1]
            for i in range(1,nrows):
                col = np.append(col, np.roll(colors, -i)[:ncols][::-1])
                
    elif colourpattern == "symmetric":
        shapecolour = list(np.repeat(shapecolour, repeateachcolor))
        
        if colourdim == "element":
            shapecolour = np.concatenate((shapecolour, shapecolour[:-1][::-1]))
            col = np.array(list(shapecolour) * int((nrows * ncols) / len(shapecolour)))
            if ((nrows * ncols) % len(shapecolour) != 0):
                col = np.append(col, shapecolour[0:(nrows * ncols) % len(shapecolour)]) 
            
        elif colourdim == "row":
            if ncols % 2 != 0:
                shapecolour = list(np.concatenate((
                    shapecolour *int((int(((ncols)/2)+1) / len(shapecolour)) ), 
                    shapecolour[0:int(((ncols)/2)+1) % len(shapecolour)],
                    list(shapecolour[0:int(((ncols)/2)) % len(shapecolour)])[::-1],
                    list(shapecolour * (int(((ncols)/2) / len(shapecolour)) ))[::-1])))
            else:
                shapecolour = list(np.concatenate((
                    shapecolour *(int(((ncols)/2) / len(shapecolour)) ), 
                    shapecolour[0:int(((ncols)/2)) % len(shapecolour)],
                    list(shapecolour[0:int(((ncols)/2)) % len(shapecolour)])[::-1],
                    list(shapecolour * (int(((ncols)/2) / len(shapecolour)) ))[::-1])))
            col = np.array(list(shapecolour) * int((ncols) / len(shapecolour)))
            if ((ncols) % len(shapecolour) != 0):
                col = np.append(col, shapecolour[0:(ncols) % len(shapecolour)]) 
                
            col = np.tile(col, reps = nrows)
            
        elif colourdim == "col":
            if nrows % 2 != 0:
                shapecolour = list(np.concatenate((
                    shapecolour *int((int(((nrows)/2)+1) / len(shapecolour)) ), 
                    shapecolour[0:int(((nrows)/2)+1) % len(shapecolour)],
                    list(shapecolour[0:int(((nrows)/2)) % len(shapecolour)])[::-1],
                    list(shapecolour * (int(((nrows)/2) / len(shapecolour)) ))[::-1])))
            else:
                shapecolour = list(np.concatenate((
                    shapecolour *(int(((nrows)/2) / len(shapecolour)) ), 
                    shapecolour[0:int(((nrows)/2)) % len(shapecolour)],
                    list(shapecolour[0:int(((nrows)/2)) % len(shapecolour)])[::-1],
                    list(shapecolour * (int(((nrows)/2) / len(shapecolour)) ))[::-1])))
                
            col = np.array(list(shapecolour) * int((nrows) / len(shapecolour)))
            if ((nrows) % len(shapecolour) != 0):
                col = np.append(col, shapecolour[0:(nrows) % len(shapecolour)]) 
                
            col = np.repeat(col, repeats = ncols)

        elif colourdim == "rightdiag":
               
            if ((nrows+ncols)-1) % 2 != 0:
                shapecolour = list(np.concatenate((
                        shapecolour *int(int(((nrows+ncols-1)/2)+1) / len(shapecolour) ), 
                        shapecolour[0:int(((nrows+ncols-1)/2)+1) % len(shapecolour)],
                        list(shapecolour[0:int(((nrows+ncols-1)/2)) % len(shapecolour)])[::-1],
                        list(shapecolour * (int(((nrows+ncols-1)/2) / len(shapecolour)) ))[::-1])))
                colors = np.array(shapecolour * int(((nrows+ncols)-1)/ len(shapecolour)))
            else:
                shapecolour = list(np.concatenate((
                        shapecolour *(int(((nrows+ncols-1)/2) / len(shapecolour)) ), 
                        shapecolour[0:int(((nrows+ncols-1)/2)) % len(shapecolour)],
                        list(shapecolour[0:int(((nrows+ncols-1)/2)) % len(shapecolour)])[::-1],
                        list(shapecolour * (int(((nrows+ncols-1)/2) / len(shapecolour)) ))[::-1])))
                colors = np.array(shapecolour * int(((nrows+ncols)-1)/ len(shapecolour)))
                     
            col = colors[:ncols]
            for i in range(1,nrows):
                col = np.append(col, np.roll(colors, -i)[:ncols])
                
        elif colourdim == "leftdiag":
                           
            if ((nrows+ncols)-1) % 2 != 0:
                shapecolour = list(np.concatenate((
                        shapecolour *int(int(((nrows+ncols-1)/2)+1) / len(shapecolour) ), 
                        shapecolour[0:int(((nrows+ncols-1)/2)+1) % len(shapecolour)],
                        list(shapecolour[0:int(((nrows+ncols-1)/2)) % len(shapecolour)])[::-1],
                        list(shapecolour * (int(((nrows+ncols-1)/2) / len(shapecolour)) ))[::-1])))
                colors = np.array(shapecolour * int(((nrows+ncols)-1)/ len(shapecolour)))
            else:
                shapecolour = list(np.concatenate((
                        shapecolour *(int(((nrows+ncols-1)/2) / len(shapecolour)) ), 
                        shapecolour[0:int(((nrows+ncols-1)/2)) % len(shapecolour)],
                        list(shapecolour[0:int(((nrows+ncols-1)/2)) % len(shapecolour)])[::-1],
                        list(shapecolour * (int(((nrows+ncols-1)/2) / len(shapecolour)) ))[::-1])))
                colors = np.array(shapecolour * int(((nrows+ncols)-1)/ len(shapecolour)))
                     
            col = colors[:ncols][::-1]
            for i in range(1,nrows):
                col = np.append(col, np.roll(colors, -i)[:ncols][::-1])
               
    
    elif colourpattern == "identity":
        # create list that is as long as number of elements in grid (nrows * ncols)
        col = np.resize(shapecolour, [nrows*ncols,1]).flatten()
        
    elif colourpattern == "random":
        # create list that is as long as number of elements in grid (nrows * ncols)
        col = np.resize(shapecolour, [nrows*ncols,1]).flatten()
        np.random.shuffle(col)

    ## IN SIZE ##
    
    # SIZE
    # create list that is as long as number of elements in grid (nrows * ncols)
    size = np.resize(shapesize, [nrows*ncols,1]).flatten()
        
    ## IN shapeorientation ##
    
    # shapeorientation
        
    if shapeorientationpattern == "repeateach":
        orientation = list(np.repeat(orientation, repeateachshapeorientation))
        
        if shapeorientationdim == "element":
            # create list that is as long as number of elements in grid (nrows * ncols)
            shapeorientation = np.array(orientation * int((nrows * ncols) / len(orientation)))
            if ((nrows * ncols) % len(orientation) != 0):
                shapeorientation = np.append(shapeorientation, orientation[0:(nrows * ncols) % len(orientation)]) 
            
        elif shapeorientationdim == "row":
            # create list that is as long as number of elements in grid (nrows * ncols)
            shapeorientation = np.array(orientation * int((ncols) / len(orientation)))
            if ((ncols) % len(orientation) != 0):
                shapeorientation = np.append(shapeorientation, orientation[0:(ncols) % len(orientation)]) 
                
            shapeorientation = np.tile(shapeorientation, reps = nrows)
            
        elif shapeorientationdim == "col":
            # create list that is as long as number of elements in grid (nrows * ncols)
            shapeorientation = np.array(orientation * int((nrows) / len(orientation)))
            if ((nrows) % len(orientation) != 0):
                shapeorientation = np.append(shapeorientation, orientation[0:(nrows) % len(orientation)]) 
                
            shapeorientation = np.repeat(shapeorientation, repeats = ncols)

        elif shapeorientationdim == "rightdiag":
            elementshapeorientations = np.array(orientation * int((nrows+ncols)-1 / len(orientation)))
            if (((nrows+ncols)-1) % len(orientation) != 0):
                elementshapeorientations = np.append(elementshapeorientations, orientation[0:((nrows+ncols)-1) % len(orientation)]) 
                     
            shapeorientation = elementshapeorientations[:ncols]
            for i in range(1,nrows):
                shapeorientation = np.append(shapeorientation, np.roll(elementshapeorientations, -i)[:ncols])
                
        elif shapeorientationdim == "leftdiag":
            elementshapeorientations = np.array(orientation * int((nrows+ncols)-1 / len(orientation)))
            if (((nrows+ncols)-1) % len(orientation) != 0):
                elementshapeorientations = np.append(elementshapeorientations, orientation[0:((nrows+ncols)-1) % len(orientation)]) 
                     
            shapeorientation = elementshapeorientations[:ncols][::-1]
            for i in range(1,nrows):
                shapeorientation = np.append(shapeorientation, np.roll(elementshapeorientations, -i)[:ncols][::-1])
                
    elif shapeorientationpattern == "symmetric":
        orientation = list(np.repeat(orientation, repeateachshapeorientation))
        
        if shapeorientationdim == "element":
            orientation = np.concatenate((orientation, orientation[:-1][::-1]))
            shapeorientation = np.array(list(orientation) * int((nrows * ncols) / len(orientation)))
            if ((nrows * ncols) % len(orientation) != 0):
                shapeorientation = np.append(shapeorientation, orientation[0:(nrows * ncols) % len(orientation)]) 
            
        elif shapeorientationdim == "row":
            if ncols % 2 != 0:
                orientation = list(np.concatenate((
                    orientation *int((int(((ncols)/2)+1) / len(orientation)) ), 
                    orientation[0:int(((ncols)/2)+1) % len(orientation)],
                    list(orientation[0:int(((ncols)/2)) % len(orientation)])[::-1],
                    list(orientation * (int(((ncols)/2) / len(orientation)) ))[::-1])))
            else:
                orientation = list(np.concatenate((
                    orientation *(int(((ncols)/2) / len(orientation)) ), 
                    orientation[0:int(((ncols)/2)) % len(orientation)],
                    list(orientation[0:int(((ncols)/2)) % len(orientation)])[::-1],
                    list(orientation * (int(((ncols)/2) / len(orientation)) ))[::-1])))
            shapeorientation = np.array(list(orientation) * int((ncols) / len(orientation)))
            if ((ncols) % len(orientation) != 0):
                shapeorientation = np.append(shapeorientation, orientation[0:(ncols) % len(orientation)]) 
                
            shapeorientation = np.tile(shapeorientation, reps = nrows)
            
        elif shapeorientationdim == "col":
            if nrows % 2 != 0:
                orientation = list(np.concatenate((
                    orientation *int((int(((nrows)/2)+1) / len(orientation)) ), 
                    orientation[0:int(((nrows)/2)+1) % len(orientation)],
                    list(orientation[0:int(((nrows)/2)) % len(orientation)])[::-1],
                    list(orientation * (int(((nrows)/2) / len(orientation)) ))[::-1])))
            else:
                orientation = list(np.concatenate((
                    orientation *(int(((nrows)/2) / len(orientation)) ), 
                    orientation[0:int(((nrows)/2)) % len(orientation)],
                    list(orientation[0:int(((nrows)/2)) % len(orientation)])[::-1],
                    list(orientation * (int(((nrows)/2) / len(orientation)) ))[::-1])))
                
            shapeorientation = np.array(list(orientation) * int((nrows) / len(orientation)))
            if ((nrows) % len(orientation) != 0):
                shapeorientation = np.append(shapeorientation, orientation[0:(nrows) % len(orientation)]) 
                
            shapeorientation = np.repeat(shapeorientation, repeats = ncols)

        elif shapeorientationdim == "rightdiag":
               
            if ((nrows+ncols)-1) % 2 != 0:
                orientation = list(np.concatenate((
                        orientation *int(int(((nrows+ncols-1)/2)+1) / len(orientation) ), 
                        orientation[0:int(((nrows+ncols-1)/2)+1) % len(orientation)],
                        list(orientation[0:int(((nrows+ncols-1)/2)) % len(orientation)])[::-1],
                        list(orientation * (int(((nrows+ncols-1)/2) / len(orientation)) ))[::-1])))
                elementshapeorientations = np.array(orientation * int(((nrows+ncols)-1)/ len(orientation)))
            else:
                orientation = list(np.concatenate((
                        orientation *(int(((nrows+ncols-1)/2) / len(orientation)) ), 
                        orientation[0:int(((nrows+ncols-1)/2)) % len(orientation)],
                        list(orientation[0:int(((nrows+ncols-1)/2)) % len(orientation)])[::-1],
                        list(orientation * (int(((nrows+ncols-1)/2) / len(orientation)) ))[::-1])))
                elementshapeorientations = np.array(orientation * int(((nrows+ncols)-1)/ len(orientation)))
                     
            shapeorientation = elementshapeorientations[:ncols]
            for i in range(1,nrows):
                shapeorientation = np.append(shapeorientation, np.roll(elementshapeorientations, -i)[:ncols])
                
        elif shapeorientationdim == "leftdiag":
                           
            if ((nrows+ncols)-1) % 2 != 0:
                orientation = list(np.concatenate((
                        orientation *int(int(((nrows+ncols-1)/2)+1) / len(orientation) ), 
                        orientation[0:int(((nrows+ncols-1)/2)+1) % len(orientation)],
                        list(orientation[0:int(((nrows+ncols-1)/2)) % len(orientation)])[::-1],
                        list(orientation * (int(((nrows+ncols-1)/2) / len(orientation)) ))[::-1])))
                elementshapeorientations = np.array(orientation * int(((nrows+ncols)-1)/ len(orientation)))
            else:
                orientation = list(np.concatenate((
                        orientation *(int(((nrows+ncols-1)/2) / len(orientation)) ), 
                        orientation[0:int(((nrows+ncols-1)/2)) % len(orientation)],
                        list(orientation[0:int(((nrows+ncols-1)/2)) % len(orientation)])[::-1],
                        list(orientation * (int(((nrows+ncols-1)/2) / len(orientation)) ))[::-1])))
                elementshapeorientations = np.array(orientation * int(((nrows+ncols)-1)/ len(orientation)))
                     
            shapeorientation = elementshapeorientations[:ncols][::-1]
            for i in range(1,nrows):
                shapeorientation = np.append(shapeorientation, np.roll(elementshapeorientations, -i)[:ncols][::-1])
               
    
    elif shapeorientationpattern == "identity":
        # create list that is as long as number of elements in grid (nrows * ncols)
        shapeorientation = np.resize(orientation, [nrows*ncols,1]).flatten()
        
    elif shapeorientationpattern == "random":
        # create list that is as long as number of elements in grid (nrows * ncols)
        shapeorientation = np.resize(orientation, [nrows*ncols,1]).flatten()
        np.random.shuffle(shapeorientation)
        
    ## IN SHAPE ##
    
    if shapepattern == "repeateach":
        shape = list(np.repeat(shape, repeateachshape))
        
        if shapedim == "element":
            # create list that is as long as number of elements in grid (nrows * ncols)
            elementshape = np.array(shape * int((nrows * ncols) / len(shape)))
            if ((nrows * ncols) % len(shape) != 0):
                elementshape = np.append(elementshape, shape[0:(nrows * ncols) % len(shape)]) 
            
        elif shapedim == "row":
            # create list that is as long as number of elements in grid (nrows * ncols)
            elementshape = np.array(shape * int((ncols) / len(shape)))
            if ((ncols) % len(shape) != 0):
                elementshape = np.append(elementshape, shape[0:(ncols) % len(shape)]) 
                
            elementshape = np.tile(elementshape, reps = nrows)
            
        elif shapedim == "col":
            # create list that is as long as number of elements in grid (nrows * ncols)
            elementshape = np.array(shape * int((nrows) / len(shape)))
            if ((nrows) % len(shape) != 0):
                elementshape = np.append(elementshape, shape[0:(nrows) % len(shape)]) 
                
            elementshape = np.repeat(elementshape, repeats = ncols)

        elif shapedim == "rightdiag":
            elementshapes = np.array(shape * int((nrows+ncols)-1 / len(shape)))
            if (((nrows+ncols)-1) % len(shape) != 0):
                elementshapes = np.append(elementshapes, shape[0:((nrows+ncols)-1) % len(shape)]) 
                     
            elementshape = elementshapes[:ncols]
            for i in range(1,nrows):
                elementshape = np.append(elementshape, np.roll(elementshapes, -i)[:ncols])
                
        elif shapedim == "leftdiag":
            elementshapes = np.array(shape * int((nrows+ncols)-1 / len(shape)))
            if (((nrows+ncols)-1) % len(shape) != 0):
                elementshapes = np.append(elementshapes, shape[0:((nrows+ncols)-1) % len(shape)]) 
                     
            elementshape = elementshapes[:ncols][::-1]
            for i in range(1,nrows):
                elementshape = np.append(elementshape, np.roll(elementshapes, -i)[:ncols][::-1])
                
    elif shapepattern == "symmetric":
        shape = list(np.repeat(shape, repeateachshape))
        
        if shapedim == "element":
            shape = np.concatenate((shape, shape[:-1][::-1]))
            elementshape = np.array(list(shape) * int((nrows * ncols) / len(shape)))
            if ((nrows * ncols) % len(shape) != 0):
                elementshape = np.append(elementshape, shape[0:(nrows * ncols) % len(shape)]) 
            
        elif shapedim == "row":
            if ncols % 2 != 0:
                shape = list(np.concatenate((
                    shape *int((int(((ncols)/2)+1) / len(shape)) ), 
                    shape[0:int(((ncols)/2)+1) % len(shape)],
                    list(shape[0:int(((ncols)/2)) % len(shape)])[::-1],
                    list(shape * (int(((ncols)/2) / len(shape)) ))[::-1])))
            else:
                shape = list(np.concatenate((
                    shape *(int(((ncols)/2) / len(shape)) ), 
                    shape[0:int(((ncols)/2)) % len(shape)],
                    list(shape[0:int(((ncols)/2)) % len(shape)])[::-1],
                    list(shape * (int(((ncols)/2) / len(shape)) ))[::-1])))
            elementshape = np.array(list(shape) * int((ncols) / len(shape)))
            if ((ncols) % len(shape) != 0):
                elementshape = np.append(elementshape, shape[0:(ncols) % len(shape)]) 
                
            elementshape = np.tile(elementshape, reps = nrows)
            
        elif shapedim == "col":
            if nrows % 2 != 0:
                shape = list(np.concatenate((
                    shape *int((int(((nrows)/2)+1) / len(shape)) ), 
                    shape[0:int(((nrows)/2)+1) % len(shape)],
                    list(shape[0:int(((nrows)/2)) % len(shape)])[::-1],
                    list(shape * (int(((nrows)/2) / len(shape)) ))[::-1])))
            else:
                shape = list(np.concatenate((
                    shape *(int(((nrows)/2) / len(shape)) ), 
                    shape[0:int(((nrows)/2)) % len(shape)],
                    list(shape[0:int(((nrows)/2)) % len(shape)])[::-1],
                    list(shape * (int(((nrows)/2) / len(shape)) ))[::-1])))
                
            elementshape = np.array(list(shape) * int((nrows) / len(shape)))
            if ((nrows) % len(shape) != 0):
                elementshape = np.append(elementshape, shape[0:(nrows) % len(shape)]) 
                
            elementshape = np.repeat(elementshape, repeats = ncols)

        elif shapedim == "rightdiag":
               
            if ((nrows+ncols)-1) % 2 != 0:
                shape = list(np.concatenate((
                        shape *int(int(((nrows+ncols-1)/2)+1) / len(shape) ), 
                        shape[0:int(((nrows+ncols-1)/2)+1) % len(shape)],
                        list(shape[0:int(((nrows+ncols-1)/2)) % len(shape)])[::-1],
                        list(shape * (int(((nrows+ncols-1)/2) / len(shape)) ))[::-1])))
                elementshapes = np.array(shape * int(((nrows+ncols)-1)/ len(shape)))
            else:
                shape = list(np.concatenate((
                        shape *(int(((nrows+ncols-1)/2) / len(shape)) ), 
                        shape[0:int(((nrows+ncols-1)/2)) % len(shape)],
                        list(shape[0:int(((nrows+ncols-1)/2)) % len(shape)])[::-1],
                        list(shape * (int(((nrows+ncols-1)/2) / len(shape)) ))[::-1])))
                elementshapes = np.array(shape * int(((nrows+ncols)-1)/ len(shape)))
                     
            elementshape = elementshapes[:ncols]
            for i in range(1,nrows):
                elementshape = np.append(elementshape, np.roll(elementshapes, -i)[:ncols])
                
        elif shapedim == "leftdiag":
                           
            if ((nrows+ncols)-1) % 2 != 0:
                shape = list(np.concatenate((
                        shape *int(int(((nrows+ncols-1)/2)+1) / len(shape) ), 
                        shape[0:int(((nrows+ncols-1)/2)+1) % len(shape)],
                        list(shape[0:int(((nrows+ncols-1)/2)) % len(shape)])[::-1],
                        list(shape * (int(((nrows+ncols-1)/2) / len(shape)) ))[::-1])))
                elementshapes = np.array(shape * int(((nrows+ncols)-1)/ len(shape)))
            else:
                shape = list(np.concatenate((
                        shape *(int(((nrows+ncols-1)/2) / len(shape)) ), 
                        shape[0:int(((nrows+ncols-1)/2)) % len(shape)],
                        list(shape[0:int(((nrows+ncols-1)/2)) % len(shape)])[::-1],
                        list(shape * (int(((nrows+ncols-1)/2) / len(shape)) ))[::-1])))
                elementshapes = np.array(shape * int(((nrows+ncols)-1)/ len(shape)))
                     
            elementshape = elementshapes[:ncols][::-1]
            for i in range(1,nrows):
                elementshape = np.append(elementshape, np.roll(elementshapes, -i)[:ncols][::-1])
               
    
    elif shapepattern == "identity":
        # create list that is as long as number of elements in grid (nrows * ncols)
        elementshape = np.resize(shape, [nrows*ncols,1]).flatten()
    
    elif shapepattern == "random":
        # create list that is as long as number of elements in grid (nrows * ncols)
        elementshape = np.resize(shape, [nrows*ncols,1]).flatten()
        np.random.shuffle(elementshape)
        
    text = np.resize(text, [nrows*ncols,1]).flatten()
    
    image = np.resize(image, [nrows*ncols,1]).flatten()
    
    # add image info
    
    n = 0
    img = np.repeat(None, (nrows*ncols))
    for i in range(nrows*ncols):
        if elementshape[i] == 'image': 
            img[i] = image[n]
            n += 1
    
    # add text info
    
    n = 0
    txt = np.repeat(None, (nrows*ncols))
    for i in range(nrows*ncols):
        if elementshape[i] == 'text': 
            txt[i] = text[n]
            n += 1
    
    # create list that is as long as number of elements in grid (nrows * ncols)    
    xyratioshape = np.resize(shapexyratio, [nrows*ncols,1]).flatten()
        
    ## TRANSLATION (HORIZONTAL, VERTICAL, HORIZONTALVERTICAL)
    
    # create list that is as long as number of elements in grid (nrows * ncols)
    mirror = np.resize(shapemirror, [nrows*ncols,1]).flatten() 
    
    # https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
    data = {}
    data['display'] = []
    data['display'].append({
                       'template': template, 
                       'max_x': max_x,
                       'max_y': max_y,
                       'xdist': xdist,
                       'ydist': ydist,
                       'shaperepeat': repeateachshape,
                       'colourpattern': colourpattern,
                       'colourdim': colourdim,
                       'colourrepeat': repeateachcolor})
    
    data['elements'] = []
#    df = pd.DataFrame({
#                   'number': range(1,nrows*ncols+1), 
#                   'column': np.array(list(np.arange(1, ncols+1, 1)) * nrows),
#                   'row': np.repeat(np.arange(1, nrows+1, 1), repeats = ncols),
#                   'x': x,
#                   'y': y,
#                   'xjitter': xjitter,
#                   'yjitter': yjitter,
#                   'shape': elementshape,
#                   'img': img,
#                   'txt': txt,
#                   'xyratio': xyratioshape,
#                   'colour': col,
#                   'size': size,
#                   'shapeorientation': shapeorientation,
#                   'mirror': mirror
#                   })
#    data['elements'] = df.to_json(orient='index')
#    # https://stackoverflow.com/questions/11942364/typeerror-integer-is-not-json-serializable-when-serializing-json-in-python
    data['elements'].append({
                       'number': list(range(1,nrows*ncols+1)), 
                       'column': list(map(int, np.array(list(np.arange(1, ncols+1, 1)) * nrows))),
                       'row': list(map( int, np.repeat(np.arange(1, nrows+1, 1), repeats = ncols))),
                       'x': list(x),
                       'y': list(y),
                       'xjitter': list(xjitter),
                       'yjitter': list(yjitter),
                       'shape': list(elementshape),
                       'img': list(img),
                       'txt': list(txt),
                       'xyratio': list(map(float, xyratioshape)),
                       'colour': list(col),
                       'size': list(map(int, size)),
                       'shapeorientation': list(map(int,shapeorientation)),
                       'mirror': list(mirror)})  
        
    # return JSON      
    return data

    #data.to_csv(txtfilename, index = False, header = True, sep = "|")
    
#    data = pd.read_csv(writedir + '/txt/' + str(len(imgs)+1).zfill(8) +'.txt', sep='|')
    


### CREATE SVG FILE FROM JSON FILE
def create_pattern_fromjson(file, viewbox = True, writedir = "OCTA_stimuli"):
    
    # If folder for .svg-files does not exist yet, create folder
    if not os.path.exists(writedir + '/svg/'):
        os.makedirs(writedir + '/svg/')
            
    # Get .svg img directory
    imgs = os.listdir(writedir + '/svg/')
    
    # Read .txt file
    with open(file) as json_file:
        data = json.load(json_file)  
#    data = pd.read_csv(file, sep='|')

    # Read parameter info from .txt file
    max_x = np.unique(data['display'][0]['max_x'])[0]
    max_y = np.unique(data['display'][0]['max_y'])[0]
    x = list(data['elements'][0]['x'])
    y = list(data['elements'][0]['y'])
    elementshape = list(data['elements'][0]['shape'])
    img = list(data['elements'][0]['img'])
    txt = list(data['elements'][0]['txt'])
    xyratioshape = list(data['elements'][0]['xyratio'])    
    col = list(data['elements'][0]['colour'])
    size = list(data['elements'][0]['size'])
    shapeorientation = list(data['elements'][0]['shapeorientation'])
    mirror = list(data['elements'][0]['mirror'])
    
    # Naming of output image
    filename = writedir + '/svg/test.svg'
    if viewbox == True:
        dwg = svgwrite.Drawing(filename, size = (max_x, max_y), viewBox = ('0 0 {} {}'.format(max_x, max_y)))
    
    else: 
        dwg = svgwrite.Drawing(filename)

    # BACKGROUND COLOR
#    dwg.add(dwg.rect(insert=(0, 0), size=('1530', '530'), rx=None, ry=None, fill='lightgrey'))

         
    # for every element in the grid:
    for i in range(len(data['elements'][0]['shape'])):
        
        # mirror/translate if required
        
        no_mirror = " "
    
        mirror_horizontalvertical = str("scale(" + str(-1) + ", " + str(-1) + ")"+
                                    "translate(" + str(-2*x[i]) + ", " + str(-2*y[i]) + ")")
        mirror_horizontal = str("scale(" + str(-1) + ", " + str(1) + ")" +
                                "translate(" + str(-2*x[i]) + ", " + str(0) + ")" )            
        mirror_vertical = str("scale(" + str(1) + ", " + str(-1) + ")" +
                              "translate(" + str(0) + ", " + str(-2*y[i]) + ")")         
        
        if mirror[i] == "none":
            mirrortype = no_mirror
        elif mirror[i] == "horizontal":
            mirrortype = mirror_horizontal
        elif mirror[i]  == "vertical":
            mirrortype = mirror_vertical
        elif mirror[i]  == "horizontalvertical":
            mirrortype = mirror_horizontalvertical
        else:
            mirrortype = no_mirror
        
        # draw element shape 
        if elementshape[i] == "none":
        
            # NO SHAPE
            continue

            
        elif elementshape[i] == "circle":
        
            # CIRCLES
            dwg.add(dwg.circle(center=(str(x[i]),str(y[i])),
                r = str(size[i]/2), 
                fill = col[i],
                transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")" )
            )
        
        elif elementshape[i] == "ellipse":
        
            # ELLIPSES
            dwg.add(dwg.ellipse(center=(str(x[i]),str(y[i])),
                r = (str((xyratioshape[i]*size[i])/2), str(size[i]/2)), 
                fill = col[i],
                transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")" )  #'white')
            )
        
        elif elementshape[i] == "rectangle":
        
            # RECTANGLES
            dwg.add(dwg.rect((str(x[i] - (xyratioshape[i]*size[i])/2) , str(y[i] - size[i]/2)), (str(xyratioshape[i]*size[i]), str(size[i])),
                fill = col[i],
                transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
    
        elif elementshape[i] == "rounded_rectangle":
        
            # ROUNDED RECTANGLES
            dwg.add(dwg.rect((str(x[i] - (xyratioshape[i]*size[i])/2) , str(y[i] - size[i]/2)), (str(xyratioshape[i]*size[i]), str(size[i])),
                rx = 5, ry = 5, fill = col[i],
                transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
    
        
        elif elementshape[i] == "triangle":
               
            # EQUILATERAL TRIANGLES
            dwg.add(dwg.polygon(points = [(str(x[i]), str(y[i] - size[i]/2)), 
                                          (str(x[i] - (xyratioshape[i]*size[i])/2), str(y[i] + size[i]/2)), 
                                          (str(x[i] + (xyratioshape[i]*size[i])/2), str(y[i] + size[i]/2))], 
                                fill = col[i],
                                transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
        
        elif elementshape[i] == "curve":
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - size[i]/2)+','+ str(y[i] - (size[i]/4))+
                             ' C'+str(x[i] - size[i]/2 + size[i]/5)+ ','+ str(y[i]+(size[i]/4))+', '+
                             str(x[i] + size[i]/2 - size[i]/5)+', '+str(y[i]+(size[i]/4))+', '+
                             str(x[i] + size[i]/2)+','+ str(y[i] - (size[i]/4)),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 12,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
        
        elif elementshape[i] == "infinity":
            
            # inspired by https://medium.com/@batkin/making-an-infinity-symbol-with-svg-6ec50cc8074d
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8))+' C'+str(x[i] - ((2/3)*size[i]))+ ','+ str(y[i] - (((2/3)*size[i])/2))+', '+str(x[i] - ((2/3)*size[i]))+', '+str(y[i] + (((2/3)*size[i])/2))+', '+str(x[i] - (size[i]/4))+','+ str(y[i] + (size[i]/8)),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            dwg.add(dwg.path( d='M '+str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8))+' L'+str(x[i] + (size[i]/4))+ ','+ str(y[i] + (size[i]/8)),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            dwg.add(dwg.path( d='M '+str(x[i] - (size[i]/4))+','+ str(y[i] + (size[i]/8))+' L'+str(x[i] + (size[i]/4))+ ','+ str(y[i] - (size[i]/8)),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            dwg.add(dwg.path( d='M'+str(x[i] + (size[i]/4))+','+ str(y[i] - (size[i]/8))+' C'+str(x[i] + ((2/3)*size[i]))+ ','+ str(y[i] - (((2/3)*size[i])/2))+', '+str(x[i] + ((2/3)*size[i]))+', '+str(y[i] + (((2/3)*size[i])/2))+', '+str(x[i] + (size[i]/4))+','+ str(y[i] + (size[i]/8)),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
    
        elif elementshape[i] == "flowerleave":
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8))+' C'+str(x[i] - ((2/3)*size[i]))+ ','+ str(y[i] - (((2/3)*size[i])/2))+', '+str(x[i] - ((2/3)*size[i]))+', '+str(y[i] + (((2/3)*size[i])/2))+', '+str(x[i] - (size[i]/4))+','+ str(y[i] + (size[i]/8))+
                             ' L' +str(x[i])+ ','+ str(y[i]) +
                             ' L' +str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8)),
                             
                    stroke = "none",
                    fill = col[i],
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            
        elif elementshape[i] == "flowerleavecontour":
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8))+' C'+str(x[i] - ((2/3)*size[i]))+ ','+ str(y[i] - (((2/3)*size[i])/2))+', '+str(x[i] - ((2/3)*size[i]))+', '+str(y[i] + (((2/3)*size[i])/2))+', '+str(x[i] - (size[i]/4))+','+ str(y[i] + (size[i]/8))+
                             ' L' +str(x[i])+ ','+ str(y[i]) +
                             ' L' +str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8)),
                             
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            
        elif elementshape[i] == "droplet":
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - (size[i]/4))+','+ str(y[i])+' C'+str(x[i] - ((2/3)*size[i]))+ ','+ str(y[i] + ((10/12)*size[i]))+', '+str(x[i] + ((2/3)*size[i]))+', '+str(y[i] + ((10/12)*size[i]))+', '+str(x[i] + (size[i]/4))+','+ str(y[i])+
                             ' L' + str(x[i]) + ','+ str(y[i] - (size[i]/2)) +
                             ' L'+str(x[i] - (size[i]/4))+','+ str(y[i]),
                    stroke = "none",
                    fill = col[i],
                    stroke_width = 1,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            
        elif elementshape[i] == "dropletcontour":
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - (size[i]/4))+','+ str(y[i])+' C'+str(x[i] - ((2/3)*size[i]))+ ','+ str(y[i] + ((10/12)*size[i]))+', '+str(x[i] + ((2/3)*size[i]))+', '+str(y[i] + ((10/12)*size[i]))+', '+str(x[i] + (size[i]/4))+','+ str(y[i])+
                             ' L' + str(x[i]) + ','+ str(y[i] - (size[i]/2)) +
                             ' L'+str(x[i] - (size[i]/4))+','+ str(y[i]),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            
        elif elementshape[i] == "text":
            
            text = txt[i]
            dwg.add(dwg.text(text = text, insert = (str(x[i]-(xyratioshape[i]*size[i])/2),
                                                      str(y[i]+size[i]/16)),
                             fill = col[i],
                             style = 'text-align = "middle";',
                             textLength = str(size[i]),
                             font_size = str(size[i]/4), font_weight = str(700), font_family = 'Trebuchet MS',
                             transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
                

        elif elementshape[i] == "image":
            
            image = img[i]
            dwg.add(dwg.image(href = image, insert = (str(x[i]-(xyratioshape[i]*size[i])/2),
                                                      str(y[i]- size[i]/2)),
                              size = (str(xyratioshape[i]*size[i]), str(size[i])),
                              transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
                      
        elif elementshape[i].endswith(".svg"):
            dwg.add(dwg.image(href = elementshape[i], insert = (str(x[i]-(xyratioshape[i]*size[i])/2),
                                                      str(y[i]- size[i]/2)),
                              size = (str(xyratioshape[i]*size[i]), str(size[i])),
                              transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
        
        elif elementshape[i].endswith(".png"):
            dwg.add(dwg.image(href = elementshape[i], insert = (str(x[i]-(xyratioshape[i]*size[i])/2),
                                                      str(y[i]- size[i]/2)),
                              size = (str(xyratioshape[i]*size[i]), str(size[i])),
                              transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
        
        else:
            dwg.add(dwg.text(text = elementshape[i], insert = (str(x[i]-(xyratioshape[i]*size[i])/2),
                                                      str(y[i]+size[i]/16)),
                             fill = col[i],
                             style = 'text-align = "middle";',
                             textLength = str(size[i]),
                             font_size = str(size[i]/4), font_weight = str(700), font_family = 'Trebuchet MS',
                             transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
    
    # write svg file to disk
    dwg.save()
    
### CREATE SVG FROM JSON
def create_pattern_fromjson_inline(data, viewbox = True, writedir = "OCTA_stimuli"):
    
    # Read parameter info from .txt file
    max_x = np.unique(data['display'][0]['max_x'])[0]
    max_y = np.unique(data['display'][0]['max_y'])[0]
    x = list(data['elements'][0]['x'])
    y = list(data['elements'][0]['y'])
    elementshape = list(data['elements'][0]['shape'])
    img = list(data['elements'][0]['img'])
    txt = list(data['elements'][0]['txt'])
    xyratioshape = list(data['elements'][0]['xyratio'])    
    col = list(data['elements'][0]['colour'])
    size = list(data['elements'][0]['size'])
    shapeorientation = list(data['elements'][0]['shapeorientation'])
    mirror = list(data['elements'][0]['mirror'])
    
    # Naming of output image
    if viewbox == True:
        dwg = svgwrite.Drawing(size = (max_x, max_y), viewBox = ('0 0 {} {}'.format(max_x, max_y)))
    
    else: 
        dwg = svgwrite.Drawing()

    # BACKGROUND COLOR
#    dwg.add(dwg.rect(insert=(0, 0), size=('1530', '530'), rx=None, ry=None, fill='lightgrey'))

         
    # for every element in the grid:
    for i in range(len(data['elements'][0]['shape'])):
        
        # mirror/translate if required
        
        no_mirror = " "
    
        mirror_horizontalvertical = str("scale(" + str(-1) + ", " + str(-1) + ")"+
                                    "translate(" + str(-2*x[i]) + ", " + str(-2*y[i]) + ")")
        mirror_horizontal = str("scale(" + str(-1) + ", " + str(1) + ")" +
                                "translate(" + str(-2*x[i]) + ", " + str(0) + ")" )            
        mirror_vertical = str("scale(" + str(1) + ", " + str(-1) + ")" +
                              "translate(" + str(0) + ", " + str(-2*y[i]) + ")")         
        
        if mirror[i] == "none":
            mirrortype = no_mirror
        elif mirror[i] == "horizontal":
            mirrortype = mirror_horizontal
        elif mirror[i]  == "vertical":
            mirrortype = mirror_vertical
        elif mirror[i]  == "horizontalvertical":
            mirrortype = mirror_horizontalvertical
        else:
            mirrortype = no_mirror
        
        # draw element shape 
        if elementshape[i] == "none":
        
            # NO SHAPE
            continue

            
        elif elementshape[i] == "circle":
        
            # CIRCLES
            dwg.add(dwg.circle(center=(str(x[i]),str(y[i])),
                r = str(size[i]/2), 
                fill = col[i],
                transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")" )
            )
        
        elif elementshape[i] == "ellipse":
        
            # ELLIPSES
            dwg.add(dwg.ellipse(center=(str(x[i]),str(y[i])),
                r = (str((xyratioshape[i]*size[i])/2), str(size[i]/2)), 
                fill = col[i],
                transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")" )  #'white')
            )
        
        elif elementshape[i] == "rectangle":
        
            # RECTANGLES
            dwg.add(dwg.rect((str(x[i] - (xyratioshape[i]*size[i])/2) , str(y[i] - size[i]/2)), (str(xyratioshape[i]*size[i]), str(size[i])),
                fill = col[i],
                transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
    
        elif elementshape[i] == "rounded_rectangle":
        
            # ROUNDED RECTANGLES
            dwg.add(dwg.rect((str(x[i] - (xyratioshape[i]*size[i])/2) , str(y[i] - size[i]/2)), (str(xyratioshape[i]*size[i]), str(size[i])),
                rx = 5, ry = 5, fill = col[i],
                transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
    
        
        elif elementshape[i] == "triangle":
               
            # EQUILATERAL TRIANGLES
            dwg.add(dwg.polygon(points = [(str(x[i]), str(y[i] - size[i]/2)), 
                                          (str(x[i] - (xyratioshape[i]*size[i])/2), str(y[i] + size[i]/2)), 
                                          (str(x[i] + (xyratioshape[i]*size[i])/2), str(y[i] + size[i]/2))], 
                                fill = col[i],
                                transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
        
        elif elementshape[i] == "curve":
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - size[i]/2)+','+ str(y[i] - (size[i]/4))+
                             ' C'+str(x[i] - size[i]/2 + size[i]/5)+ ','+ str(y[i]+(size[i]/4))+', '+
                             str(x[i] + size[i]/2 - size[i]/5)+', '+str(y[i]+(size[i]/4))+', '+
                             str(x[i] + size[i]/2)+','+ str(y[i] - (size[i]/4)),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 12,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
        
        elif elementshape[i] == "infinity":
            
            # inspired by https://medium.com/@batkin/making-an-infinity-symbol-with-svg-6ec50cc8074d
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8))+' C'+str(x[i] - ((2/3)*size[i]))+ ','+ str(y[i] - (((2/3)*size[i])/2))+', '+str(x[i] - ((2/3)*size[i]))+', '+str(y[i] + (((2/3)*size[i])/2))+', '+str(x[i] - (size[i]/4))+','+ str(y[i] + (size[i]/8)),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            dwg.add(dwg.path( d='M '+str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8))+' L'+str(x[i] + (size[i]/4))+ ','+ str(y[i] + (size[i]/8)),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            dwg.add(dwg.path( d='M '+str(x[i] - (size[i]/4))+','+ str(y[i] + (size[i]/8))+' L'+str(x[i] + (size[i]/4))+ ','+ str(y[i] - (size[i]/8)),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            dwg.add(dwg.path( d='M'+str(x[i] + (size[i]/4))+','+ str(y[i] - (size[i]/8))+' C'+str(x[i] + ((2/3)*size[i]))+ ','+ str(y[i] - (((2/3)*size[i])/2))+', '+str(x[i] + ((2/3)*size[i]))+', '+str(y[i] + (((2/3)*size[i])/2))+', '+str(x[i] + (size[i]/4))+','+ str(y[i] + (size[i]/8)),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
    
        elif elementshape[i] == "flowerleave":
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8))+' C'+str(x[i] - ((2/3)*size[i]))+ ','+ str(y[i] - (((2/3)*size[i])/2))+', '+str(x[i] - ((2/3)*size[i]))+', '+str(y[i] + (((2/3)*size[i])/2))+', '+str(x[i] - (size[i]/4))+','+ str(y[i] + (size[i]/8))+
                             ' L' +str(x[i])+ ','+ str(y[i]) +
                             ' L' +str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8)),
                             
                    stroke = "none",
                    fill = col[i],
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            
        elif elementshape[i] == "flowerleavecontour":
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8))+' C'+str(x[i] - ((2/3)*size[i]))+ ','+ str(y[i] - (((2/3)*size[i])/2))+', '+str(x[i] - ((2/3)*size[i]))+', '+str(y[i] + (((2/3)*size[i])/2))+', '+str(x[i] - (size[i]/4))+','+ str(y[i] + (size[i]/8))+
                             ' L' +str(x[i])+ ','+ str(y[i]) +
                             ' L' +str(x[i] - (size[i]/4))+','+ str(y[i] - (size[i]/8)),
                             
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            
        elif elementshape[i] == "droplet":
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - (size[i]/4))+','+ str(y[i])+' C'+str(x[i] - ((2/3)*size[i]))+ ','+ str(y[i] + ((10/12)*size[i]))+', '+str(x[i] + ((2/3)*size[i]))+', '+str(y[i] + ((10/12)*size[i]))+', '+str(x[i] + (size[i]/4))+','+ str(y[i])+
                             ' L' + str(x[i]) + ','+ str(y[i] - (size[i]/2)) +
                             ' L'+str(x[i] - (size[i]/4))+','+ str(y[i]),
                    stroke = "none",
                    fill = col[i],
                    stroke_width = 1,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            
        elif elementshape[i] == "dropletcontour":
               
            # CURVES
            dwg.add(dwg.path( d='M'+str(x[i] - (size[i]/4))+','+ str(y[i])+' C'+str(x[i] - ((2/3)*size[i]))+ ','+ str(y[i] + ((10/12)*size[i]))+', '+str(x[i] + ((2/3)*size[i]))+', '+str(y[i] + ((10/12)*size[i]))+', '+str(x[i] + (size[i]/4))+','+ str(y[i])+
                             ' L' + str(x[i]) + ','+ str(y[i] - (size[i]/2)) +
                             ' L'+str(x[i] - (size[i]/4))+','+ str(y[i]),
                    stroke = col[i],
                    fill = "none",
                    stroke_width = 3,
                    transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
            
        elif elementshape[i] == "text":
            
            text = txt[i]
            dwg.add(dwg.text(text = text, insert = (str(x[i]-(xyratioshape[i]*size[i])/2),
                                                      str(y[i]+size[i]/16)),
                             fill = col[i],
                             style = 'text-align = "middle";',
                             textLength = str(size[i]),
                             font_size = str(size[i]/4), font_weight = str(700), font_family = 'Trebuchet MS',
                             transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
                

        elif elementshape[i] == "image":
            
            image = img[i]
            dwg.add(dwg.image(href = image, insert = (str(x[i]-(xyratioshape[i]*size[i])/2),
                                                      str(y[i]- size[i]/2)),
                              size = (str(xyratioshape[i]*size[i]), str(size[i])),
                              transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
                      
        elif elementshape[i].endswith(".svg"):
            dwg.add(dwg.image(href = elementshape[i], insert = (str(x[i]-(xyratioshape[i]*size[i])/2),
                                                      str(y[i]- size[i]/2)),
                              size = (str(xyratioshape[i]*size[i]), str(size[i])),
                              transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
        
        elif elementshape[i].endswith(".png"):
            dwg.add(dwg.image(href = elementshape[i], insert = (str(x[i]-(xyratioshape[i]*size[i])/2),
                                                      str(y[i]- size[i]/2)),
                              size = (str(xyratioshape[i]*size[i]), str(size[i])),
                              transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
        
        else:
            dwg.add(dwg.text(text = elementshape[i], insert = (str(x[i]-(xyratioshape[i]*size[i])/2),
                                                      str(y[i]+size[i]/16)),
                             fill = col[i],
                             style = 'text-align = "middle";',
                             textLength = str(size[i]),
                             font_size = str(size[i]/4), font_weight = str(700), font_family = 'Trebuchet MS',
                             transform = mirrortype + "rotate(" + str(shapeorientation[i]) + ", " + str(x[i]) + " " + str(y[i]) + ")")
            )
    
    # return svg
    return dwg
    
### MERGE .SVG-FILES TOGETHER
def merge_svg(file1, file2, writedir = "OCTA_stimuli/svg/"):
    
    svg1 = st.fromfile(writedir + file1)
    svg2 = st.fromfile(writedir + file2)
    svg1.append(svg2)
    svg1.save(writedir + file1.replace(".svg", "") + file2.replace(".svg", "") + 'merged.svg')
    
### CREATE PNG FILE FROM SVG FILE   
def create_png(svgfile, bg = 0xFFFFFF, writedir = "OCTA_stimuli"):
    
    # If folder for .svg-files does not exist yet, create folder
    if not os.path.exists(writedir + '/png/'):
        os.makedirs(writedir + '/png/')
        
    pngfile = svgfile.replace("svg", "png")
    pngfilename = pngfile.replace(".png", "_bg"+str(bg)+".png")
    figure = svg2rlg(svgfile)
    renderPM.drawToFile(figure, pngfilename, fmt="PNG", bg=bg)
    
### !!! ERROR WHEN WORKING WITH TEXT !!! 
### not enough values to unpack (expected 2, got 1)
    

### CREATE .JSON & .SVG FILE
def create_pattern(template = "grid",
                   shape = ['rectangle'], 
                   image = "none", #'../vector_images/hotdog.svg',
                   text = "none",
                   nrows = 5, ncols = 5,
                   startx = 30, starty = 30,
                   xdist = 30, ydist = 30,
                   shapemirror = ['none'],
                   orientation = [0],
                   shapecolour = ["blue"],
                   repeateachcolor = 1,
                   colourpattern = 'identity',
                   colourdim = 'element',
                   repeateachshape = 1,
                   shapepattern = 'identity',
                   shapedim = 'element',
                   repeateachshapeorientation = 1,
                   shapeorientationpattern = 'identity',
                   shapeorientationdim = 'element',
                   shapesize = [20],
                   shapexyratio = [1],
                   jitterscale = [0],
                   viewbox = True,
                   writedir = "OCTA_stimuli"):
    
    # Create json
    create_pattern_json(template,
                   shape, 
                   image, 
                   text,
                   nrows, ncols,
                   startx, starty,
                   xdist, ydist,
                   shapemirror,
                   orientation,
                   shapecolour,
                   repeateachcolor,
                   colourpattern,
                   colourdim,
                   repeateachshape,
                   shapepattern,
                   shapedim,
                   repeateachshapeorientation,
                   shapeorientationpattern,
                   shapeorientationdim,
                   shapesize,
                   shapexyratio,
                   jitterscale,
                   writedir)
    
    # Create svg from txt
    txt = os.listdir(writedir + '/json/')
    jsonfilename = (writedir + '/json/' + str(len(txt)).zfill(8) + '.json')
    create_pattern_fromjson(jsonfilename, viewbox, writedir)
    
### CREATE INLINE .JSON & .SVG 
def create_pattern_inline(template = "grid",
                   shape = ['rectangle'], 
                   image = "none", #'../vector_images/hotdog.svg',
                   text = "none",
                   nrows = 5, ncols = 5,
                   startx = 30, starty = 30,
                   xdist = 30, ydist = 30,
                   shapemirror = ['none'],
                   orientation = [0],
                   shapecolour = ["blue"],
                   repeateachcolor = 1,
                   colourpattern = 'identity',
                   colourdim = 'element',
                   repeateachshape = 1,
                   shapepattern = 'identity',
                   shapedim = 'element',
                   repeateachshapeorientation = 1,
                   shapeorientationpattern = 'identity',
                   shapeorientationdim = 'element',
                   shapesize = [20],
                   shapexyratio = [1],
                   jitterscale = [0],
                   viewbox = True,
                   writedir = "OCTA_stimuli"):
    
    # Create json
    json = create_pattern_json_inline(template,
                   shape, 
                   image, 
                   text,
                   nrows, ncols,
                   startx, starty,
                   xdist, ydist,
                   shapemirror,
                   orientation,
                   shapecolour,
                   repeateachcolor,
                   colourpattern,
                   colourdim,
                   repeateachshape,
                   shapepattern,
                   shapedim,
                   repeateachshapeorientation,
                   shapeorientationpattern,
                   shapeorientationdim,
                   shapesize,
                   shapexyratio,
                   jitterscale,
                   writedir)
    
    # Create svg from json
    svg = create_pattern_fromjson_inline(json, viewbox, writedir)
    return svg.tostring()


#####################
#### EXAMPLE USE ####
#####################

## Create txt
create_pattern_json(shape = ["rectangle", "rectangle"], shapepattern = "symmetric", shapedim = "rightdiag",
                    colourpattern = "identity", colourdim = "leftdiag", orientation = [0, 45], 
                    shapeorientationpattern = "repeateach", shapeorientationdim = "row", shapecolour = ['red'])

create_pattern_fromjson(r'C:\Users\Christophe\Desktop\todo\octa\OCTA_stimuli\json\test.json')


#
## Create svg from txt
#txt = os.listdir('OCTA_stimuli/txt/')
#txtfilename = ('OCTA_stimuli/txt/' + str(len(txt)).zfill(8) + '.txt')
#create_pattern_fromtxt(txtfilename)
#
## Create png from svg
#svg = os.listdir('OCTA_stimuli/svg/')
#svgfilename = ('OCTA_stimuli/svg/' + str(len(svg)).zfill(8) + '.svg')
#create_png(svgfilename)
#
## Create txt and svg
#create_pattern(shape = ["droplet", "rectangle"], orientation = [60, 45], shapecolour = ['red', 'blue'], viewbox = True )

## Merge svgs
#merge_svg(file1 = "mergepart1.svg", file2 = "mergepart2.svg", writedir = "toolbox_examples/")

#merge_svg(file1 = "OCTAflower.svg", file2 = "OCTAletters1.svg", writedir = "")