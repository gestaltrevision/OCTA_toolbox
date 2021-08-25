"""
Complexity measurements code for the OCTA toolbox

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
def CalculateElementsN(self):
    """
    Calculate how many elements are present in the display.

    Returns
    -------
    N : int

    """     
    
    standard_n = len(self.shapes)
    noneshapes_n = 0
    
    for element_id in range(standard_n):
        if 'shape' in self._attribute_overrides[element_id]:
            if self._attribute_overrides[element_id]['shape'] is None:
                noneshapes_n = noneshapes_n + 1
     
    # Calculate number of elements in display       
    N = standard_n - noneshapes_n
    
    return N

def CalculateElementsLOCE(self, distinction_features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many different types of elements are present in the display based on the feature dimensions specified in distinction_features.
        
    Parameters
    ----------
    distinction_features: list
        Feature dimensions that will be inspected to decide if two elements
        are the same. Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']

    Returns
    -------
    LOCE : int

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
        
    element_list = [{k: dic[k] for k in features} for dic in self.dwg_elements]
    feature_list = {k: [dic[k] for dic in element_list] for k in element_list[0]}
    
    # Create a list of unique fingerprints for each element    
    element_fingerprints = []
    for idx in range(self.n_cols * self.n_rows):
        fingerprint = "|".join([str(feature_list[f][idx]) for f in features])
        element_fingerprints.append(fingerprint)
     
    # Calculate number of different elements in display       
    LOCE = len(set(element_fingerprints))
    
    return LOCE

def CalculateElementsLOC(self, distinction_features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many different features are present across all dimensions.
        
    Parameters
    ----------
    distinction_features: list
        Feature dimensions that will be taken into account.
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']

    Returns
    -------
    LOC: int

    """     
    
    if self.dwg_elements is None:
        self.Render()
        
    n_shape_values = len(set([d['shape'] for d in self.dwg_elements])) 

    n_size_values = len(set([d['boundingbox'] for d in self.dwg_elements])) 
        
    n_fillcolor_values = len(set([d['fillcolor'] for d in self.dwg_elements])) 
        
    n_orientation_values = len(set([d['orientation'] for d in self.dwg_elements])) 
        
    n_data_values = len(set([d['data'] for d in self.dwg_elements])) 
        
    n_borderwidth_values = len(set([d['borderwidth'] for d in self.dwg_elements])) 
    
    n_bordercolor_values = len(set([d['bordercolor'] for d in self.dwg_elements])) 
    
    n_opacity_values = len(set([d['opacity'] for d in self.dwg_elements]))   
    
    n_mirror_values = len(set([d['mirrorvalue'] for d in self.dwg_elements])) 
    
    n_link_values = len(set([d['link'] for d in self.dwg_elements])) 
    
    n_classlabel_values = len(set([d['classlabel'] for d in self.dwg_elements])) 
    
    n_idlabel_values = len(set([d['idlabel'] for d in self.dwg_elements])) 
        
    LOC = 0
    
    if 'shapes' in distinction_features:
        LOC += n_shape_values
    if 'boundingboxes' in distinction_features:
        LOC += n_size_values
    if 'fillcolors' in distinction_features:
        LOC += n_fillcolor_values
    if 'orientations' in distinction_features:
        LOC += n_orientation_values
    if 'data' in distinction_features:
        LOC += n_data_values
    if 'borderwidths' in distinction_features:
        LOC += n_borderwidth_values
    if 'bordercolors' in distinction_features:
        LOC += n_bordercolor_values
    if 'opacities' in distinction_features:
        LOC += n_opacity_values
    if 'mirrorvalues' in distinction_features:
        LOC += n_mirror_values
    if 'links' in distinction_features:
        LOC += n_link_values
    if 'classlabels' in distinction_features:
        LOC += n_classlabel_values
    if 'idlabels' in distinction_features:
        LOC += n_idlabel_values
        
    return LOC

def CalculateElementsLOCI(self, distinction_features = ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']):
    """
    Calculate how many different feature dimensions have more than one feature value (i.e., have non-identical values).
        
    Parameters
    ----------
    distinction_features: list
        Feature dimensions that will be taken into account.
        Default is ['shapes', 'boundingboxes', 'fillcolors', 'orientations', 'data']

    Returns
    -------
    LOCI: int

    """     
    
    if self.dwg_elements is None:
        self.Render()
        
    id_shape_values = len(set([d['shape'] for d in self.dwg_elements])) == 1

    id_size_values = len(set([d['boundingbox'] for d in self.dwg_elements])) == 1
        
    id_fillcolor_values = len(set([d['fillcolor'] for d in self.dwg_elements])) == 1
        
    id_orientation_values = len(set([d['orientation'] for d in self.dwg_elements])) == 1
        
    id_data_values = len(set([d['data'] for d in self.dwg_elements])) == 1
        
    id_borderwidth_values = len(set([d['borderwidth'] for d in self.dwg_elements])) == 1

    id_bordercolor_values = len(set([d['bordercolor'] for d in self.dwg_elements])) == 1
        
    id_opacity_values = len(set([d['opacity'] for d in self.dwg_elements])) == 1
        
    id_mirrorvalues = len(set([d['mirrorvalue'] for d in self.dwg_elements])) == 1
        
    id_link_values = len(set([d['link'] for d in self.dwg_elements])) == 1
        
    id_classlabel_values = len(set([d['classlabel'] for d in self.dwg_elements])) == 1
        
    id_idlabel_values = len(set([d['idlabel'] for d in self.dwg_elements])) == 1
        
    LOCI = 0
    
    if ('shapes' in distinction_features) and (id_shape_values == True):
        LOCI += 1
    if ('boundingboxes' in distinction_features) and (id_size_values == True):
        LOCI += 1
    if ('fillcolors' in distinction_features) and (id_fillcolor_values == True):
        LOCI += 1
    if ('orientations' in distinction_features) and (id_orientation_values == True):
        LOCI += 1
    if ('data' in distinction_features) and (id_data_values == True):
        LOCI += 1
    if ('borderwidths' in distinction_features) and (id_borderwidth_values == True):
        LOCI += 1
    if ('bordercolors' in distinction_features) and (id_bordercolor_values == True):
        LOCI += 1
    if ('opacities' in distinction_features) and (id_opacity_values == True):
        LOCI += 1
    if ('mirrorvalues' in distinction_features) and (id_mirrorvalues == True):
        LOCI += 1
    if ('links' in distinction_features) and (id_link_values == True):
        LOCI += 1
    if ('classlabels' in distinction_features) and (id_classlabel_values == True):
        LOCI += 1
    if ('idlabels' in distinction_features) and (id_idlabel_values == True):
        LOCI += 1
        
    return len(distinction_features) - LOCI