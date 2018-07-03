#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:32:24 2018

@author: ribli
"""

from sis import run_sis
import matplotlib.pyplot as plt
import numpy as np
import sys


def fig1(N, M, rep, title='', filename='', kavg=3.,
         lams = [0.005,0.01,0.02],  p0 = 0.0001 ,
         gamma = 2.3, in_scale_free=True, out_scale_free=True,
         show_intervals=True):
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
            p[0,i,j] = run_sis(N, M, lam, p0, kavg, gamma, in_scale_free=True, 
                               out_scale_free=True, same_deg=False)[-1]
            # er
            p[1,i,j] = run_sis(N, M, lam, p0, kavg, gamma, in_scale_free=False, 
                               out_scale_free=False, same_deg=False)[-1]

    line, = plt.plot(lams,p[0].mean(axis=1),'+--',label='SF')
    line, = plt.plot(lams,p[1].mean(axis=1),'x:',label='ER')

    plt.xlabel(r'$\lambda$')
    plt.ylabel('p')
    plt.title(title)
    plt.legend()
    plt.savefig('../figs/'+filename+'.png')

    
    
if __name__=='__main__':
    fig1(1000, 1000, rep=100, p0 = -1, lams = np.arange(0.001,0.61,0.03), 
         show_intervals = False, title='', filename='fig1_nocorr')