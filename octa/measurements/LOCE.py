from collections import defaultdict

def CalculateElementsLOCE(self):
    """
    Calculate how many different elements are present in the display.

    Returns
    -------
    LOCE value.

    """     
    
    elements = [ "|".join([str(i), str(j), str(k), str(l), str(m)]) for i, j, k, l, m in zip(self.shapes.pattern, self.size.pattern, self.colour.pattern, self.orientation.pattern, self.data.pattern)] 
    
    d = defaultdict(list)
    for i, x in enumerate(elements):
        d[x].append(i)
        
    LOCE = len(d)
    
    return LOCE