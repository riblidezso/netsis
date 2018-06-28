#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:32:24 2018

@author: ribli
"""


from fig3 import fig3 as fig4
    
    
if __name__=='__main__':
    # fig 4
    fig4(1000, 60, rep=1000, lams = [0.3,0.31,0.32,0.33], p0=1e-2, kavg=3.0,
         yscale_='linear', 
         title='Going extict on ER graph',filename='fig4')
    