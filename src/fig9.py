#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:34:16 2018

@author: ribli
"""


from fig3 import fig3 as fig9
    
    
if __name__=='__main__':
    # fig 9
    fig9(10000, 100, rep=1000, lams = [0.08,0.09,0.10], p0=-1, gamma=2.2,
         in_scale_free=True, out_scale_free=True, filter_runs=True,
         title='Spreading on scale-free graph',filename='fig9')
    