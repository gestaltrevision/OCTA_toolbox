def CalculateElementsLOCE(self, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many different types of elements are present in the display based on the feature dimensions specified in distinction_features.

    Returns
    -------
    LOCE value.

    """     
    
    # Create a list of unique fingerprints for each element
    features = dict()
    for f in distinction_features:
        features[f] = getattr(self, f)
    
    element_fingerprints = []
    for idx in range(self.n_cols * self.n_rows):
        fingerprint = "|".join([str(features[f][idx]) for f in distinction_features])
        element_fingerprints.append(fingerprint)
     
    # Calculate number of different elements in display       
    LOCE = len(set(element_fingerprints))
    
    return LOCE

def CalculateElementsLOC(self, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many different features are present across all dimensions.

    Returns
    -------
    LOC value.

    """     
    
    n_shape_values = len(self._shapes.pattern)

    n_size_values = len(self._bounding_boxes.pattern)
        
    n_fillcolor_values = len(self._fillcolors.pattern)
        
    n_orientation_values = len(self._orientations.pattern)
        
    n_data_values = len(self._data.pattern)

    n_bordercolor_values = len(self._bordercolors.pattern)
        
    n_borderwidth_values = len(self._borderwidths.pattern)
        
    LOC = 0
    
    if 'shapes' in distinction_features:
        LOC += n_shape_values
    if 'bounding_boxes' in distinction_features:
        LOC += n_size_values
    if 'fillcolors' in distinction_features:
        LOC += n_fillcolor_values
    if 'orientations' in distinction_features:
        LOC += n_orientation_values
    if 'data' in distinction_features:
        LOC += n_data_values
    if 'bordercolors' in distinction_features:
        LOC += n_bordercolor_values
    if 'borderwidths' in distinction_features:
        LOC += n_borderwidth_values
        
    return LOC

def CalculateElementsLOCI(self, distinction_features = ['shapes', 'bounding_boxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many different feature dimensions have more than one feature value (i.e., have non-identical values).

    Returns
    -------
    LOCI value.

    """     
    
    id_shape_values = len(self._shapes.pattern) == 1

    id_size_values = len(self._bounding_boxes.pattern) == 1
        
    id_fillcolor_values = len(self._fillcolors.pattern) == 1
        
    id_orientation_values = len(self._orientations.pattern) == 1
        
    id_data_values = len(self._data.pattern) == 1

    id_bordercolor_values = len(self._bordercolors.pattern) == 1
        
    id_borderwidth_values = len(self._borderwidths.pattern) == 1
        
    LOCI = 0
    
    if ('shapes' in distinction_features) and (id_shape_values == True):
        LOCI += 1
    if ('bounding_boxes' in distinction_features) and (id_size_values == True):
        LOCI += 1
    if ('fillcolors' in distinction_features) and (id_fillcolor_values == True):
        LOCI += 1
    if ('orientations' in distinction_features) and (id_orientation_values == True):
        LOCI += 1
    if ('data' in distinction_features) and (id_data_values == True):
        LOCI += 1
    if ('bordercolors' in distinction_features) and (id_bordercolor_values == True):
        LOCI += 1
    if ('borderwidths' in distinction_features) and (id_borderwidth_values == True):
        LOCI += 1
        
    return LOCI