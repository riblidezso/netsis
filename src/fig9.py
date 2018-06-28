#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:34:16 2018

@author: ribli
"""


from fig3 import fig3 as fig9
    
    
if __name__=='__main__':
    # fig 4
    fig9(10000, 100, rep=100, lams = [0.2,0.25], p0=-1,gamma=2.5,
         in_scale_free=True, out_scale_free=True,
         title='Spreading on scale-free graph',filename='fig9')
    