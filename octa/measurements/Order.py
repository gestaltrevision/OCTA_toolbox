def GetPatterns(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
     

    Returns
    -------
     

    """     
    patterntypes = []
    for f in features:
        patterntypes.append(eval("self._" + str(f) + ".patterntype"))
        
    patterndirections = []
    for f in features:
        patterndirections.append(eval("self._" + str(f) + ".patterndirection"))
      
    patterns = {}
    for i in range(len(features)):
        patterns[features[i]] = patterntypes[i] + patterndirections[i]
      
    return patterns

def GetPatternTypes(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
     

    Returns
    -------
     

    """     
    patterntypes = []
    for f in features:
        patterntypes.append(eval("self._" + str(f) + ".patterntype"))
      
    patterns = {}
    for i in range(len(features)):
        patterns[features[i]] = patterntypes[i] 
      
    return patterns

def GetPatternDirections(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
     

    Returns
    -------
     

    """             
    patterndirections = []
    for f in features:
        patterndirections.append(eval("self._" + str(f) + ".patterndirection"))
      
    patterns = {}
    for i in range(len(features)):
        patterns[features[i]] = patterndirections[i]
      
    return patterns

def CheckPatternCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
    Check whether all specified element features have congruent patterns.

    Returns
    -------
    value.

    """     
    
    patterntypes = []
    for f in features:
        patterntypes.append(eval("self._" + str(f) + ".patterntype"))
        
    patterndirections = []
    for f in features:
        patterndirections.append(eval("self._" + str(f) + ".patterndirection"))
      
    patterns = []
    for i in range(len(features)):
        patterns.append(patterntypes[i] + patterndirections[i])
        
    if len(set(patterns)) == 1:
        congruent = True
    else:
        congruent = False
    
    return congruent

def CalculatePatternCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many specified element features have congruent patterns.

    Returns
    -------
    value.

    """     
    
    patterntypes = []
    for f in features:
        patterntypes.append(eval("self._" + str(f) + ".patterntype"))
        
    patterndirections = []
    for f in features:
        patterndirections.append(eval("self._" + str(f) + ".patterndirection"))
      
    patterns = {}
    for i in range(len(features)):
        patterns[features[i]] = patterntypes[i] + patterndirections[i]
        
    patternnames = [patterns[f] for f in patterns.keys()]
    patterncount = {}    
    for p in patternnames:
        p_patterncount = 0
        for f in features:
            if patterns[f] == p:
                p_patterncount += 1
        patterncount[p] = p_patterncount
    
    return patterncount

def CheckPatternTypeCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many element features have congruent patterntypes.

    Returns
    -------
    value.

    """     
    
    patterntypes = []
    for f in features:
        patterntypes.append(eval("self._" + str(f) + ".patterntype"))
        
    if len(set(patterntypes)) == 1:
        congruent = True
    else:
        congruent = False
    
    return congruent

def CalculatePatternTypeCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many specified element features have congruent patterntypes.

    Returns
    -------
    value.

    """     
    
    patterntypes = []
    for f in features:
        patterntypes.append(eval("self._" + str(f) + ".patterntype"))
      
    patterns = {}
    for i in range(len(features)):
        patterns[features[i]] = patterntypes[i] 
        
    patternnames = [patterns[f] for f in patterns.keys()]
    patterncount = {}    
    for p in patternnames:
        p_patterncount = 0
        for f in features:
            if patterns[f] == p:
                p_patterncount += 1
        patterncount[p] = p_patterncount
    
    return patterncount

def CheckPatternDirectionCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many element features have congruent patterndirections.

    Returns
    -------
    value.

    """     
    
    patterndirections = []
    for f in features:
        patterndirections.append(eval("self._" + str(f) + ".patterndirection"))
        
    if len(set(patterndirections)) == 1:
        congruent = True
    else:
        congruent = False
    
    return congruent

def CalculatePatternDirectionCongruency(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many specified element features have congruent patterndirections.

    Returns
    -------
    value.

    """             
    patterndirections = []
    for f in features:
        patterndirections.append(eval("self._" + str(f) + ".patterndirection"))
      
    patterns = {}
    for i in range(len(features)):
        patterns[features[i]] = patterndirections[i]
        
    patternnames = [patterns[f] for f in patterns.keys()]
    patterncount = {}    
    for p in patternnames:
        p_patterncount = 0
        for f in features:
            if patterns[f] == p:
                p_patterncount += 1
        patterncount[p] = p_patterncount
    
    return patterncount

def CalculatePatternDeviants(self, distinction_features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many deviants are present given the specified distinction_features.

    Returns
    -------
    value.

    """             
    
    if self.dwg_elements is None:
        self.Render()
        
    features = []
    if 'shapes' in distinction_features:
        features.append("shape")
    if 'boundingboxes' in distinction_features:
        features.append("boundingbox")
    if 'fillcolors' in distinction_features:
        features.append("fillcolor")
    if 'orientations' in distinction_features:
        features.append("orientation")
    if 'data' in distinction_features:
        features.append("data")
    if 'borderwidths' in distinction_features:
        features.append("borderwidth")
    if 'bordercolors' in distinction_features:
        features.append("bordercolor")
    if 'opacities' in distinction_features:
        features.append("opacity")
    if 'mirrorvalues' in distinction_features:
        features.append("mirrorvalue")
    if 'links' in distinction_features:
        features.append("link")
    if 'classlabels' in distinction_features:
        features.append("classlabel")
    if 'idlabels' in distinction_features:
        features.append("idlabel")
        
    features = sorted(features)
    distinction_features = sorted(distinction_features)
        
    element_list = [{k: dic[k] for k in features} for dic in self.dwg_elements]
    feature_list = {k: [dic[k] for dic in element_list] for k in element_list[0]}
    
    
    pattern_list = {}
    for i in range(len(distinction_features)):
        pattern_list[features[i]] = getattr(self, distinction_features[i])
        
    deviants = []  
    for f in features:
        if feature_list[f] != pattern_list[f]:
            for i in range(len(element_list)):
                if feature_list[f][i] != pattern_list[f][i]:
                    if i not in deviants:
                        deviants.append(i) 
        
        
    return len(deviants)

def CalculatePositionDeviants(self):
    """
    Calculate how many deviants are present for position.

    Returns
    -------
    value.

    """   
    if self.dwg_elements is None:
        self.Render()          
    
    xpatternpositions = self.positions.x
    ypatternpositions = self.positions.y
    xactualpositions = self.positions.GetPositions()[0]
    yactualpositions = self.positions.GetPositions()[1]
    
    shapes = [dic['shape'] for dic in self.dwg_elements]
    
    deviants = []  
    if (xpatternpositions != xactualpositions) or (ypatternpositions != yactualpositions) or (None in shapes):
        
        for i in range(len(xactualpositions)):
            if xpatternpositions[i] != xactualpositions[i]:
                if i not in deviants:
                    deviants.append(i) 
            if ypatternpositions[i] != yactualpositions[i]:
                if i not in deviants:
                    deviants.append(i)   
            if shapes[i] is None:
                if i not in deviants:
                    deviants.append(i) 
        
    return len(deviants)