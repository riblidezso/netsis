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


def fig3(N, M, title, filename ='',
        lams = [0.1,0.2], p0 = 0.0001 , k = 3.,
        gamma = 2.1, in_scale_free=False, out_scale_free=False):
    """
    Reproduce p evolution figures from paper.
    
    
    Density of infected nodes as the function of time 
    in spreading experiments in the ER/SF network.
    """ 
    g = scale_free_graph(N, gamma, in_scale_free, out_scale_free, k)
    mu = 0.1 * np.mean(g.degree().values())/2
    print 'mu = ',mu
    
    # a starting sis model, to have uniform initial infections
    sis0 = SIS(g, 0, 0, p0)  
    
    for lam in lams:  
        sis = SIS(g, lam, mu, p0)  # sis model
        sis.inf = set(sis0.inf)  # set infections 
        p =[len(sis.inf)/float(N)]
        for j in range(M):
            sis.update()
            p.append(len(sis.inf)/float(N))
        plt.plot(p,label='lambda='+str(lam))
    
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('t')
    plt.ylabel('p')
    plt.title(title)
    plt.legend()
    plt.savefig('../figs/'+filename+'.png')
    
    
if __name__=='__main__':
    fig3(1000000, 10000, lams = [0.15,0.2,0.3], p0=1e-5,
         title='Spreading on ER graph ',filename='fig3_ER_pt')