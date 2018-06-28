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


def fig1(N, M, rep, title='', filename='', kavg=3,
         lams = [0.005,0.01,0.02],  p0 = 0.0001 ,
         gamma = 2.5, in_scale_free=True, out_scale_free=True):
    """
    Reproduce fig1 from paper.
    
    Density of infected nodes as a function of lamdba.
    """
    # scale free-ish directed network
    g0 = scale_free_graph(N, gamma, True, True)
    # get its average degree
    kavg = np.mean(g0.degree().values())/2
    # ER
    g1 = scale_free_graph(N, gamma, False, False, kavg)
    
    # starting sis models, to have uniform initial infections
    sis0 = SIS(g0, 0, 0, p0) 
    sis1 = SIS(g1, 0, 0, p0) 
    
    p = np.zeros((2,len(lams),rep))
    for i,lam in enumerate(lams):
        for j in range(rep):
            sis = SIS(g0, lam, mu, p0)  # sis model
            sis.inf = set(sis0.inf)  # set infections 
            for k in range(M):
                sis.update()
            p[0,i,j] = len(sis.inf)/float(N)
            
            sis = SIS(g1, lam, mu, p0)  # sis model
            sis.inf = set(sis1.inf)  # set infections 
            for k in range(M):
                sis.update()
            p[1,i,j] = len(sis.inf)/float(N)
        

    #line, = plt.plot(lams,p[0].mean(axis=1),'+--',label='SF')
    line, = plt.plot(lams,np.median([0],axis=1),'+--',label='SF')
    plt.fill_between(lams,np.percentile(p[0],10,axis=1),
                     np.percentile(p[0],90,axis=1),
                     color=line.get_color(), alpha=0.2)
    
    #line, = plt.plot(lams,p[1].mean(axis=1),'x:',label='ER')
    line, = plt.plot(lams,np.median([0],axis=1),'x:',label='ER')
    plt.fill_between(lams,np.percentile(p[1],10,axis=1),
                     np.percentile(p[1],90,axis=1),
                     color=line.get_color(), alpha=0.2)

    plt.xlabel(r'$\lambda$')
    plt.ylabel('p')
    plt.title(title)
    plt.legend()
    plt.savefig('../figs/'+filename+'.png')

    
    
if __name__=='__main__':
    fig1(1000, 1000, rep=10, p0 = 1e-2,
         lams = np.arange(0.01,0.2,0.01), 
         title='',filename='lamdba_p')