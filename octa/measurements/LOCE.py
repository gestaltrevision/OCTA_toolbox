from collections import defaultdict

def CalculateElementsLOCE(self):
    """
    Calculate how many different types of elements are present in the display.

    Returns
    -------
    LOCE value.

    """     
    
    elements = [ "|".join([str(i), str(j), str(k), str(l), str(m), str(n)]) for i, j, k, l, m, n in zip(self.shapes, self.bounding_boxes, self.fillcolors, self.bordercolors, self.orientations, self.data)] 
    
    d = defaultdict(list)
    for i, x in enumerate(elements):
        d[x].append(i)
        
    LOCE = len(d)
    
    return LOCE

#def CalculateElementsLOC(self):
#    """
#    Calculate how many different features are present across all dimensions.
#
#    Returns
#    -------
#    LOC value.
#
#    """     
#    
#    shape_values = defaultdict(list)
#    for i, x in enumerate(self.shapes):
#        shape_values[x].append(i)
#
#    size_values = defaultdict(list)
#    for i, x in enumerate(self.bounding_boxes):
#        size_values[x].append(i)
#        
#    fillcolor_values = defaultdict(list)
#    for i, x in enumerate(self.fillcolors):
#        fillcolor_values[x].append(i)
#        
#    bordercolor_values = defaultdict(list)
#    for i, x in enumerate(self.bordercolors):
#        bordercolor_values[x].append(i)
#        
#    orientation_values = defaultdict(list)
#    for i, x in enumerate(self.orientations):
#        orientation_values[x].append(i)
#        
#    data_values = defaultdict(list)
#    for i, x in enumerate(self.data):
#        data_values[x].append(i)       
#        
#    LOC = len(shape_values) + len(size_values) + len(fillcolor_values) #+ len(bordercolor_values) + len(orientation_values) + len(data_values)   
#    
#    return LOC