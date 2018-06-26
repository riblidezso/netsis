#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

Generate networks.

Created on Tue Jun 26 13:31:21 2018

@author: ribli
"""

import networkx as nx
import random
import numpy as np


N = 100
k = 2.
p = k/N


g = nx.fast_gnp_random_graph(N, p, directed=True)
# g = nx.barabasi_albert_graph(directed=True)

class SIS:
    """ Susceptible-Infected-Susceptible (SIS) Model."""
    def __init__(self, g, lam, mu, p0):
        """ Iniatialize model with graph and parameters."""
        self.g = g
        self.nodes = g.nodes()
        self.edge_d = {x[0]:[] for x in g.edges()}
        for x in g.edges():    
            self.edge_d[x[0]].append(x[1])
            
        self.inf = set(x for x in self.edge_d.keys() if (random.random()<p0) )
        
        self.lam = lam
        self.mu = mu
        
    
    def update(self):
        """Update the model."""
        k = list(self.inf)
        np.random.shuffle(k)
        # infect
        for ki in k:
            for ei in self.edge_d[ki]:
                if random.random() < self.lam:
                    self.inf.add(ei)
        # decay
        for ni in list(self.inf):
            if random.random() < self.mu:
                self.inf.remove(ni)
                
        
mu = 0.1
lam = 0.001
p0 = 0.2

sis = SIS(g, lam, mu, p0)
p =[]
for j in range(1000):
    sis.update()
    p.append(len(sis.inf))
plot(p)
    
%pylab inline