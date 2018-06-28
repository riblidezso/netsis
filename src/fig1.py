#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:32:24 2018

@author: ribli
"""

from sis import SIS
from scale_free import scale_free_graph
import matplotlib.pyplot as plt
import numpy as np


def fig1(N, M, title='', filename='',
         lams = [0.005,0.01,0.02],  p0 = 0.0001 ,
         gamma = 2.5, in_scale_free=True, out_scale_free=True):
    """
    Reproduce fig1 from paper.
    
    Density of infected nodes as a function of lamdba.
    """
    # scale free-ish directed network
    g0 = scale_free_graph(N, gamma, True, True)
    # get its average degree
    k = np.mean(g0.degree().values())/2
    mu = 0.1 * k
    print 'mu = ',mu
    # ER
    g1 = scale_free_graph(N, gamma, False, False, k)
    
    # starting sis models, to have uniform initial infections
    sis0 = SIS(g0, 0, 0, p0) 
    sis1 = SIS(g1, 0, 0, p0) 
    
    p0, p1 = [], []
    for lam in lams:
        sis = SIS(g0, lam, mu, p0)  # sis model
        sis.inf = set(sis0.inf)  # set infections 
        for j in range(M):
            sis.update()
        p0.append(len(sis.inf)/float(N))
        
        sis = SIS(g1, lam, mu, p0)  # sis model
        sis.inf = set(sis1.inf)  # set infections 
        for j in range(M):
            sis.update()
        p1.append(len(sis.inf)/float(N))
        

    plt.plot(lams,p0,'o-',label='SF')
    plt.plot(lams,p1,'x:',label='ER')
    plt.xlabel(r'$\lambda$')
    plt.ylabel('p')
    plt.title(title)
    plt.legend()
    plt.savefig('../figs/'+filename+'.png')

    
    
if __name__=='__main__':
    fig1(100000, 1000, lams = np.arange(0.01,0.4,0.01), 
         title='',filename='lamdba_p')