#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:32:24 2018

@author: ribli
"""

from sis import run_sis
from custom_graph import custom_graph
import matplotlib.pyplot as plt
import numpy as np
import sys


def fig1a(N, M, rep, title='', filename='', kavg=3.,
         lams = [0.005,0.01,0.02],  p0 = 0.0001 , gamma = 2.2):
    """
    Reproduce fig1 from paper.
    
    Density of infected nodes as a function of lamdba.
    """
    p = np.zeros((4,len(lams),rep))  # data holder
    for i,lam in enumerate(lams):
        print '\n',lam,
        for j in range(rep):
            print j,;sys.stdout.flush()
            # scale-free, perfect degree correlation
            p[0,i,j] = run_sis(N, M, lam, p0=p0, kavg=kavg, gamma=gamma, 
                               in_scale_free=True, out_scale_free=True,
                               same_deg=True)[-1]
            # ER, perfect degree correlation
            p[1,i,j] = run_sis(N, M, lam, p0=p0, kavg=kavg, gamma=gamma, 
                               in_scale_free=False, out_scale_free=False,
                               same_deg=True)[-1]
            
            # scale-free in and out, no degree coreelation
            # get a graph
            g = custom_graph(N,gamma,in_scale_free=True, out_scale_free=False,
                             same_deg=False, k=kavg)
            # scale-free in,no degree coreelation
            p[2,i,j] = run_sis(N, M, lam, g=g, p0=p0)[-1]
            # scale free out, no degree coreelation, 
            # same net with reverted edges
            p[3,i,j] = run_sis(N, M, lam, g=g.reverse(), p0=p0)[-1]
            
            
    line, = plt.plot(lams,p[0].mean(axis=1),'+--',label='SF')
    line, = plt.plot(lams,p[1].mean(axis=1),'x:',label='ER')
    line, = plt.plot(lams,p[2].mean(axis=1),'o-',label='SF in')    
    line, = plt.plot(lams,p[3].mean(axis=1),'v-.',label='SF out')
    
    plt.xlabel(r'$\lambda$')
    plt.ylabel('p')
    plt.title(title)
    plt.legend(loc='upper left')
    plt.savefig('../figs/'+filename+'.png')

    
    
if __name__=='__main__':
    fig1a(1000, 1000, rep = 30, p0 = -1,
         lams = np.arange(0.001,0.61,0.03), 
         title='',filename='fig1b_rev')
