"""
Order measurements code for the OCTA toolbox

The Order & Complexity Toolbox for Aesthetics (OCTA) Python library is a tool for researchers 
to create stimuli varying in order and complexity on different dimensions. 
Copyright (C) 2021  Eline Van Geert, Christophe Bossens, and Johan Wagemans

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: eline.vangeert@kuleuven.be

"""
def GetPatterns(self, features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
    Provides a list of the applied pattern for each of the specified features
        
    Parameters
    ----------
    features: list
        Feature dimensions that will be taken into account. 
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']
     

    Returns
    -------
    Dictionary with pattern per feature

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
    Provides a list of the applied pattern types for each of the specified features
        
    Parameters
    ----------
    features: list
        Feature dimensions that will be taken into account. 
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']
     

    Returns
    -------
    Dictionary with patterntype per feature

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
    Provides a list of the applied pattern directions for each of the specified features
        
    Parameters
    ----------
    features: list
        Feature dimensions that will be taken into account. 
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']
     

    Returns
    -------
    Dictionary with patterndirection per feature

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
    
    Parameters
    ----------
    features: list
        Feature dimensions that will be taken into account. 
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']
     
    Returns
    -------
    Boolean

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

    Parameters
    ----------
    features: list
        Feature dimensions that will be taken into account. 
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']
     
    Returns
    -------
    Value indicating the maximal number of congruent patterns.

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
    Check whether all specified element features have congruent pattern types.

    Parameters
    ----------
    features: list
        Feature dimensions that will be taken into account. 
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']
     
    Returns
    -------
    Boolean

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
    Calculate how many specified element features have congruent pattern types.

    Parameters
    ----------
    features: list
        Feature dimensions that will be taken into account. 
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']
     
    Returns
    -------
    Value indicating the maximal number of congruent pattern types.

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
    Check whether all specified element features have congruent pattern directions.

    Parameters
    ----------
    features: list
        Feature dimensions that will be taken into account. 
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']
     
    Returns
    -------
    Boolean

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
    Calculate how many specified element features have congruent pattern directions.

    Parameters
    ----------
    features: list
        Feature dimensions that will be taken into account. 
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']
     
    Returns
    -------
    Value indicating the maximal number of congruent patterndirections.

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
    Calculate how many deviant elements are present given the specified distinction_features.

    Parameters
    ----------
    distinction_features: list
        Feature dimensions that will be taken into account. 
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']
     
    Returns
    -------
    Number of deviants

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
    Calculate how many deviant positions are present.

    Returns
    -------
    Number of deviant positions

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