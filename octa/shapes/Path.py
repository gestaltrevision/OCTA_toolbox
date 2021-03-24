# -*- coding: utf-8 -*-
"""

"""
import svgwrite
import svgpathtools

def Path(path, xsize, ysize, name = None):
    if name == None:
        name = "Path_" #+ str(path) + "_" + str(xsize) + "_" + str(ysize)
    return type(str(name), (Path_,), {'path': path, 'xsizepath': xsize, 'ysizepath': ysize, 'name': name})

class Path_:
    parameters = ['position', 'bounding_box', 'data', 'orientation' ,'bordercolor', 'borderwidth', 'fillcolor', 'opacity', 'class_label', 'id_label', 'mirror_value']
    
    def __init__(self, **kwargs):
        for p in Path_.parameters:
            set_method = getattr(self, 'set_%s'%p)
            if p in kwargs:
                set_method(kwargs[p])
            else:
                set_method(None)


    def set_position(self, position):
        if position == None:
            position = (0, 0)
        
        self.position = position
    
    
    def set_bounding_box(self, bounding_box):
        if bounding_box == None:
            bounding_box = (10, 10)
        
        self.bounding_box = bounding_box
    
    
    def set_orientation(self, orientation):
        if orientation == None:
            orientation = 0
            
        self.orientation = orientation
        
        self.xsize = self.data[1]
        self.ysize = self.data[2]
        
        if type(self.orientation) == int:
            self.rotation_animation = ""
            self.rotation_transform = "rotate(%d, %d, %d)"%(self.orientation, self.xsize/2, self.ysize/2)
        elif type(self.orientation) == list:
            self.rotation_animation = "svgwrite.animate.AnimateTransform('rotate','transform', from_= '" + self.orientation[1] + " " + str(self.xsize/2) + " " + str(self.ysize/2) + "', to = '" + self.orientation[2] + " " + str(self.xsize/2) + " " + str(self.ysize/2) + "', " + self.orientation[3] + ")"
            self.rotation_transform = "rotate(%d, %d, %d)"%(int(self.orientation[1]), self.xsize/2, self.ysize/2)    
                
    def set_bordercolor(self, bordercolor):
        if bordercolor == None:
            bordercolor = "green"
            
        self.bordercolor = bordercolor
    
    
    def set_borderwidth(self, borderwidth):
        if borderwidth == None:
            borderwidth = 4
            
        self.borderwidth = borderwidth
        
        
    def set_fillcolor(self, fillcolor):
        if fillcolor == None:
            fillcolor = "gray"
            
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
        
    def set_class_label(self, class_label):
        if class_label == None:
            class_label = ""
            
        self.class_label = class_label
    
    def set_id_label(self, id_label):
        if id_label == None:
            id_label = ""
            
        self.id_label = id_label
    
    def set_mirror_value(self, mirror_value):
        if mirror_value == None:
            mirror_value = ""
            
        self.mirror_value = mirror_value
        
    def set_data(self, data):
        if data == None:
            data = ""
            
        if(hasattr(self, "path")):
            data = [self.path, self.xsizepath, self.ysizepath]
            
        self.data = data
    

    def create_mirror_transform(self):
        mirror_transform = ""
        if self.mirror_value == "vertical":
            mirror_transform = "scale(-1, 1) translate(%f, 0)"%(-2*self.position[0])
        elif self.mirror_value == "horizontal":
            mirror_transform = "scale(1, -1), translate(0, %f)"%(-2*self.position[1])
        elif self.mirror_value == "horizontalvertical":
            mirror_transform = "scale(-1, -1) translate(%f, %f)"%(-2*self.position[0], -2*self.position[1])
                
        return mirror_transform
    
    def __str__(self):
        result = "Path object with params:\n"
        for p in Path_.parameters:
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
        topleft = (self.position[0] - self.bounding_box[0]/2 , self.position[1] - self.bounding_box[1]/2)
                          
        scale_x_parameter = self.bounding_box[0] / self.xsize
        scale_y_parameter = self.bounding_box[1] / self.ysize
        
        sizeposition_transform = "scale(%f, %f) translate(%f, %f)"%(scale_x_parameter, scale_y_parameter, (topleft[0]/scale_x_parameter), (topleft[1]/scale_y_parameter))

        mirror_transform = self.create_mirror_transform()  
               
        svg = dwg.path(
                d            = self.data[0],              
                fill         = self.create_fillcolor(dwg),
                opacity      = self.opacity,
                stroke       = self.create_bordercolor(dwg),
                stroke_width = self.borderwidth,
                transform    = " ".join([mirror_transform, sizeposition_transform,  self.rotation_transform]))#,
#                insert      = topleft,
#                size        = self.bounding_box)
                
#                extra = 
                
#                transform   = " ".join([mirror_transform, rotation_transform]))
        
        if self.class_label != "":
            svg['class']         = self.class_label
        if self.id_label != "":
            svg['id']        = self.id_label
            
        if self.fillcolor_animation != "":
            svg.add(eval(self.fillcolor_animation))
            
        if self.rotation_animation != "":
            svg.add(eval(self.rotation_animation))  
            
#        link = dwg.add(dwg.a(href = "#", onmouseover="audio = new Audio('alarm.ogg'); audio.play(); audio.loop=true;", onmouseout="audio.pause(); try { audio.currentTime=0; } catch(e) {} audio.loop=false;"))
#        link = dwg.add(dwg.a(href = "#", target="_self", onclick="audio = new Audio('lyricchords.mp3');  try { audio.currentTime=0; } catch(e) {} audio.play()"))
#        link.add(svg)

        return svg
    
    
if __name__ == '__main__':
    c = Path_(x = 3, y = 4, size = 10,  color = "blue", orientation = 30, data = 'hello')
    print(c)