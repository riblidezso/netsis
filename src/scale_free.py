#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 11:31:23 2018

@author: ribli
"""

import networkx as nx
import numpy as np
import random

def scale_free_graph(N, gamma, in_scale_free, out_scale_free, k=3.):
    """Create scale free pseudograph, with scale free in or/and out."""
    if in_scale_free:
        in_seq = np.random.zipf(gamma, N)
    else:
        in_seq = np.random.binomial(N-1, k/(N-1),N)
        
    if out_scale_free:
        out_seq = np.random.zipf(gamma, N)
    else:
        out_seq = np.random.binomial(N-1, k/(N-1),N)
        
        
    diff = sum(out_seq) - sum(in_seq)
    for k in range(np.abs(diff)):
        out_seq[random.randint(0,N-1)] -= np.sign(diff)
        
    print 'Generated graph',
    print 'in scale free:',str(in_scale_free),
    print 'out scale free:',str(out_scale_free)
    print '<kin> =',np.mean(in_seq),
    print '<kout> =',np.mean(out_seq)
        
        
    g = nx.directed_configuration_model(list(in_seq), list(out_seq))
    return g
    