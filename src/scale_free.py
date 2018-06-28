#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Generate networks.

Created on Thu Jun 28 11:31:23 2018

@author: ribli
"""

import networkx as nx
import numpy as np
import random

def scale_free_graph(N, gamma, in_scale_free, out_scale_free, 
                     k=3., same_deg = True, verbose=False):
    """Create scale free pseudograph, with scale free in or/and out."""
    if in_scale_free:
        in_seq = np.random.zipf(gamma, N)
    else:
        in_seq = np.random.binomial(N-1, k/(N-1),N)
        
    if out_scale_free:
        if same_deg:
            out_seq = in_seq
        else:
            out_seq = np.random.zipf(gamma, N)
    else:
        out_seq = np.random.binomial(N-1, k/(N-1),N)
        
        
    diff = sum(out_seq) - sum(in_seq)
    for k in range(np.abs(diff)):
        out_seq[random.randint(0,N-1)] -= np.sign(diff)
        
    if verbose:
        print 'Generated graph',
        print 'in scale free:',str(in_scale_free),
        print 'out scale free:',str(out_scale_free)
        print '<kin> =',np.mean(in_seq),
        print '<kout> =',np.mean(out_seq)
        
        
    g = nx.directed_configuration_model(list(in_seq), list(out_seq))
    
    # only connected component?
    # gl = list(nx.components.strongly_connected_component_subgraphs(g))
    # gll = sorted(gl,key=lambda x:x.size())
    # g = gll[-1]
    
    return g
    