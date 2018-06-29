#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:32:24 2018

@author: ribli
"""


from fig3 import fig3
    
    
if __name__=='__main__':
    # fig 3
    fig3(10000, 1000, rep=1000, lams = [0.3, 0.31,0.32], p0=-1, kavg=3., gamma=2.2,
         in_scale_free=False, out_scale_free=True,
         title='Spreading on SF-out graph',filename='fig3a')