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
import sys


def fig1(N, M, rep, title='', filename='', kavg=3.,
         lams = [0.005,0.01,0.02],  p0 = 0.0001 ,
         gamma = 2.3, in_scale_free=True, out_scale_free=True):
    """
    Reproduce fig1 from paper.
    
    Density of infected nodes as a function of lamdba.
    """
    p = np.zeros((2,len(lams),rep))  # data holder
    for i,lam in enumerate(lams):
        print '\n',lam,
        for j in range(rep):
            print j,;sys.stdout.flush()
            # scale-free
            g0 = scale_free_graph(N, gamma, True, True) 
            sis = SIS(g0, lam, p0)  # sis model
            for k in range(M):
                sis.update()
            p[0,i,j] = len(sis.inf)/float(len(g0))
            
            # er
            g1 = scale_free_graph(N, 0, False, False, kavg)
            sis = SIS(g1, lam, p0)  # sis model
            for k in range(M):
                sis.update()
            p[1,i,j] = len(sis.inf)/float(len(g1))
        

    line, = plt.plot(lams,p[0].mean(axis=1),'+--',label='SF')
    plt.fill_between(lams,np.percentile(p[0],16,axis=1),
                     np.percentile(p[0],84,axis=1),
                     color=line.get_color(), alpha=0.2)
    
    line, = plt.plot(lams,p[1].mean(axis=1),'x:',label='ER')
    plt.fill_between(lams,np.percentile(p[1],16,axis=1),
                     np.percentile(p[1],84,axis=1),
                     color=line.get_color(), alpha=0.2)

    plt.xlabel(r'$\lambda$')
    plt.ylabel('p')
    plt.title(title)
    plt.legend()
    plt.savefig('../figs/'+filename+'.png')

    
    
if __name__=='__main__':
    fig1(1000, 1000, rep=30, p0 = -1,
         lams = np.arange(0.001,0.61,0.03), 
         title='',filename='fig1')
