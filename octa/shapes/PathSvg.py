# -*- coding: utf-8 -*-
"""

"""
import svgwrite
from svg.path import parse_path
import svgpathtools

def PathSvg(src, name = None):
    if name == None:
        name = "PathSvg_" #+ str(src)
    return type(str(name), (PathSvg_,), {'source': src, 'name': name})

class PathSvg_:
    parameters = ['position', 'boundingbox', 'data', 'orientation' ,'bordercolor', 'borderwidth', 'fillcolor', 'opacity', 'classlabel', 'idlabel', 'mirrorvalue', 'link']
    
    def __init__(self, **kwargs):
        for p in PathSvg_.parameters:
            set_method = getattr(self, 'set_%s'%p)
            if p in kwargs:
                set_method(kwargs[p])
            else:
                set_method(None)


    def set_position(self, position):
        if position == None:
            position = (0, 0)
        
        self.position = position
    
    
    def set_boundingbox(self, boundingbox):
        if boundingbox == None:
            boundingbox = (10, 10)
        
        self.boundingbox = boundingbox
    
    
    def set_orientation(self, orientation):
        if orientation == None:
            orientation = 0
            
        self.orientation = orientation
               
        paths, self.attributes = svgpathtools.svg2paths(self.data)
        n_paths = len(paths)
        allpaths = []

        for i in range(0,n_paths):
            mypath = paths[i]
            xmin, xmax, ymin, ymax = mypath.bbox()
            allpaths.append([xmin, xmax, ymin, ymax])
            
        self.min_x = min([item[0] for item in allpaths])
        self.max_x = max([item[1] for item in allpaths])        
        self.min_y = min([item[2] for item in allpaths])
        self.max_y = max([item[3] for item in allpaths])  
        self.max_xsize = (self.max_x + self.min_x)
        self.max_ysize = (self.max_y + self.min_y) 

        if (type(self.orientation) == int) or (type(self.orientation) == float):
            self.rotation_animation = ""
            self.rotation_transform = "rotate(%d, %d, %d)"%(self.orientation, self.max_xsize/2, self.max_ysize/2)
        elif type(self.orientation) == list:
            self.rotation_animation = "svgwrite.animate.AnimateTransform('rotate','transform', from_= '" + self.orientation[1] + " " + str(self.max_xsize/2) + " " + str(self.max_ysize/2) + "', to = '" + self.orientation[2] + " " + str(self.max_xsize/2) + " " + str(self.max_ysize/2) + "', " + self.orientation[3] + ")"
            self.rotation_transform = "rotate(%d, %d, %d)"%(int(self.orientation[1]), self.max_xsize/2, self.max_ysize/2)    
            
    def set_bordercolor(self, bordercolor):
        if bordercolor == None:
            bordercolor = "none"
            
        self.bordercolor = bordercolor
        
        if type(self.bordercolor) == str:
            self.bordercolor_animation = ""
        elif type(self.bordercolor) == list:
            if self.bordercolor[0] == "set":                
                self.bordercolor_animation = "svgwrite.animate.Set(attributeName = 'stroke'," + self.bordercolor[2] + ")"
                self.bordercolor = self.bordercolor[1]
            elif self.bordercolor[0] == "animate":
                self.bordercolor_animation = "svgwrite.animate.Animate(attributeName = 'stroke'," + self.bordercolor[2] + ")"
                self.bordercolor = self.bordercolor[1]
            else:
                self.bordercolor_animation = ""    
    
    def set_borderwidth(self, borderwidth):
        if borderwidth == None:
            borderwidth = 0
            
        self.borderwidth = borderwidth

        if (type(self.borderwidth) == int) or (type(self.borderwidth) == float):
            self.borderwidth_animation = ""
        elif type(self.borderwidth) == list:
            if self.borderwidth[0] == "set":                
                self.borderwidth_animation = "svgwrite.animate.Set(attributeName = 'stroke-width'," + self.borderwidth[2] + ")"
                self.borderwidth = self.borderwidth[1]
            elif self.borderwidth[0] == "animate":
                self.borderwidth_animation = "svgwrite.animate.Animate(attributeName = 'stroke-width'," + self.borderwidth[2] + ")"
                self.borderwidth = self.borderwidth[1]
            else:
                self.borderwidth_animation = ""
        
        
    def set_fillcolor(self, fillcolor):
        if fillcolor == None:
            fillcolor = "none"
            
        self.fillcolor = fillcolor
        
        if type(self.fillcolor) == str:
            self.fillcolor_animation = ""
        elif type(self.fillcolor) == list:
            if self.fillcolor[0] == "set":                
                self.fillcolor_animation = "svgwrite.animate.Set(attributeName = 'fill'," + self.fillcolor[2] + ")"
                self.fillcolor = self.fillcolor[1]
            elif self.fillcolor[0] == "animate":
                self.fillcolor_animation = "svgwrite.animate.Animate(attributeName = 'fill'," + self.fillcolor[2] + ")"
                self.fillcolor = self.fillcolor[1]
            else:
                self.fillcolor_animation = ""
    
    def set_opacity(self, opacity):
        if opacity == None:
            opacity = 1
            
        self.opacity = opacity   
        
        if (type(self.opacity) == int) or (type(self.opacity) == float):
            self.opacity_animation = ""
        elif type(self.opacity) == list:
            if self.opacity[0] == "set":                
                self.opacity_animation = "svgwrite.animate.Set(attributeName = 'opacity'," + self.opacity[2] + ")"
                self.opacity = self.opacity[1]
            elif self.opacity[0] == "animate":
                self.opacity_animation = "svgwrite.animate.Animate(attributeName = 'opacity'," + self.opacity[2] + ")"
                self.opacity = self.opacity[1]
            else:
                self.opacity_animation = ""  
        
    def set_classlabel(self, classlabel):
        if classlabel == None:
            classlabel = ""
            
        self.classlabel = classlabel
    
    def set_idlabel(self, idlabel):
        if idlabel == None:
            idlabel = ""
            
        self.idlabel = idlabel
    
    def set_mirrorvalue(self, mirrorvalue):
        if mirrorvalue == None:
            mirrorvalue = ""
            
        self.mirrorvalue = mirrorvalue

    def set_link(self, link):
        if link == "":
            setlink = ""
        else:             
            setlink = 'dwg.add(dwg.a(href = "' + str(link) + '", target="_blank"' + '))'
            
        self.link = setlink
        
    def set_data(self, data):
        if data == None:
            data = ""

        if(hasattr(self, "source")):
            data = self.source
            
        self.data = data
    

    def create_mirror_transform(self):
        mirror_transform = ""
        if self.mirrorvalue == "vertical":
            mirror_transform = "scale(-1, 1) translate(%f, 0)"%(-2*self.position[0])
        elif self.mirrorvalue == "horizontal":
            mirror_transform = "scale(1, -1), translate(0, %f)"%(-2*self.position[1])
        elif self.mirrorvalue == "horizontalvertical":
            mirror_transform = "scale(-1, -1) translate(%f, %f)"%(-2*self.position[0], -2*self.position[1])
                
        return mirror_transform
    
    def __str__(self):
        result = "PathSvg object with params:\n"
        for p in PathSvg_.parameters:
            result += "%s: %s\n"%(p, getattr(self,p))
            
        return result
        
    def create_fillcolor(self, dwg):
        gradient = ""
        if len(self.fillcolor) < 2:
            return self.fillcolor
        elif self.fillcolor[0] == "radial":
            gradient = dwg.radialGradient()
        elif self.fillcolor[0] == "horizontal":
            gradient = dwg.linearGradient((0, 0), (1, 0))
        elif self.fillcolor[0] == "vertical":
            gradient = dwg.linearGradient((0, 0), (0, 1))
        elif self.fillcolor[0] == "diagonal":
            gradient = dwg.linearGradient((0, 0), (1, 1))
        else:
            return self.fillcolor
            
        dwg.defs.add(gradient)
        # define the gradient colors
        n_colors = len(self.fillcolor)-1
        stepsize = 1 / (n_colors - 1)
        for i in range(n_colors):
            gradient.add_stop_color(i*stepsize, self.fillcolor[i+1])
            
        return gradient.get_paint_server()  

    def create_bordercolor(self, dwg):
        gradient = ""
        if len(self.bordercolor) < 2:
            return self.bordercolor
        elif self.bordercolor[0] == "radial":
            gradient = dwg.radialGradient()
        elif self.bordercolor[0] == "horizontal":
            gradient = dwg.linearGradient((0, 0), (1, 0))
        elif self.bordercolor[0] == "vertical":
            gradient = dwg.linearGradient((0, 0), (0, 1))
        elif self.bordercolor[0] == "diagonal":
            gradient = dwg.linearGradient((0, 0), (1, 1))
        else:
            return self.bordercolor
            
        dwg.defs.add(gradient)
        # define the gradient colors
        n_colors = len(self.bordercolor)-1
        stepsize = 1 / (n_colors - 1)
        for i in range(n_colors):
            gradient.add_stop_color(i*stepsize, self.bordercolor[i+1])
            
        return gradient.get_paint_server() 

    def generate(self, dwg):
        topleft = (self.position[0] - self.boundingbox[0]/2 , self.position[1] - self.boundingbox[1]/2)
              
        scale_x_parameter = self.boundingbox[0] / self.max_xsize
        scale_y_parameter = self.boundingbox[1] / self.max_ysize
        
        # d = " ".join([item["d"] for item in self.attributes])
        keep = [i for i, x in enumerate(['d' in  self.attributes[i] for i in range(len(self.attributes))]) if x]
        d = " ".join([item["d"] for item in [self.attributes[i] for i in keep]])
        
        path = parse_path(d)
        
        sizeposition_transform = "scale(%f, %f) translate(%f, %f)"%(scale_x_parameter, scale_y_parameter, (topleft[0]/scale_x_parameter), (topleft[1]/scale_y_parameter))

        mirror_transform = self.create_mirror_transform() 
               
        svg = dwg.path(
                d            = path.d(),              
                fill         = self.create_fillcolor(dwg),
                opacity      = self.opacity,
                stroke       = self.create_bordercolor(dwg),
                stroke_width = self.borderwidth,
                transform    = " ".join([mirror_transform,sizeposition_transform, self.rotation_transform]))#,
#                insert      = topleft,
#                size        = self.boundingbox)
                
#                extra = 
                
#                transform   = " ".join([mirror_transform, rotation_transform]))

        if self.classlabel != "":
            svg['class']         = self.classlabel
        if self.idlabel != "":
            svg['id']        = self.idlabel
            
        if self.fillcolor_animation != "":
            svg.add(eval(self.fillcolor_animation))
            
        if self.rotation_animation != "":
            svg.add(eval(self.rotation_animation))   
            
        if self.borderwidth_animation != "":
            svg.add(eval(self.borderwidth_animation))    
             
        if self.bordercolor_animation != "":
            svg.add(eval(self.bordercolor_animation))    
              
        if self.opacity_animation != "":
            svg.add(eval(self.opacity_animation))    
            
        if self.link != "":            
            svg = eval(self.link).add(svg)
                        
        return svg
    
    
if __name__ == '__main__':
    c = PathSvg_(x = 3, y = 4, size = 10,  color = "blue", orientation = 30, data = 'hello')
    print(c)