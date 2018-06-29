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


def fig3(N, M, rep, title, filename ='',
        lams = [0.1,0.2], p0 = 0.0001 , kavg = 3.,
        gamma = 2.2, in_scale_free=False, out_scale_free=False,
        xscale_='log', yscale_='log', filter_runs=False):
    """
    Reproduce p evolution figures from paper.
    
    Density of infected nodes as the function of time 
    in spreading experiments in the ER/SF network.
    """   
    for i,lam in enumerate(lams):  # different spreading rate
        p = np.zeros((rep, M))  # data holder
        print '\n',lam,  # report
        for j in range(rep):  # iterate runs
            print j,;sys.stdout.flush()  # report
            p[j,:] = run_sis(N, M, lam, p0, kavg, gamma, 
                             in_scale_free, out_scale_free)
        if filter_runs:
            keep = p[:,2]!=0  # filter if immeadiately died
            plt.plot(range(1,M+1),p[keep,:].mean(axis=0),
                     label=r'$\lambda=$'+str(lam))
        else:
            plt.plot(range(1,M+1),p.mean(axis=0),label=r'$\lambda=$'+str(lam))
    
    plt.yscale(xscale_)
    plt.xscale(yscale_)
    plt.xlabel('t')
    plt.ylabel('p')
    plt.title(title)
    plt.legend()
    plt.savefig('../figs/'+filename+'.png')
    
    
if __name__=='__main__':
    # fig 3
    fig3(10000, 1000, rep=1000, lams = [0.35,0.36,0.37], p0=-1, kavg=3.,
         title='Spreading on ER graph',filename='fig3')
    