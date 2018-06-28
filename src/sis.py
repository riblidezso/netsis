#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

SIS model.

Mu=1, as in the Satorras, Vespigniani paper.

Created on Tue Jun 26 13:31:21 2018

@author: ribli
"""

import random
import numpy as np


class SIS:
    """ Susceptible-Infected-Susceptible (SIS) Model."""
    def __init__(self, g, lam, p0):
        """ Iniatialize model with graph and parameters."""
        self.g = g
        self.nodes = g.nodes()
        self.edge_d = {x[0]:[] for x in g.edges()}
        for x in g.edges():    
            self.edge_d[x[0]].append(x[1])
            
        if p0 == -1:
            self.inf = set([random.choice(self.edge_d.keys())])
        else:
            self.inf = set(x for x in self.nodes if (random.random()<p0) )
        
        self.lam = lam
        # self.mu = mu
        
    
    def update(self):
        """Update the model."""
        k = [ ki for ki in self.inf if ki in self.edge_d]
        np.random.shuffle(k)
        
        # infect
        new_inf = set()
        for ki in k:
            for ei in self.edge_d[ki]:
                if random.random() < self.lam:
                    #self.new_inf.add(ei) 
                    new_inf.add(ei) 
        # decay    
        self.inf = new_inf
        #for ki in k:
        #    if random.random() < self.mu:
        #        self.inf.remove(ki)           