#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 13:33:25 2018

@author: ribli
"""

  
        
#def scale_free_graph():
    
def fig34(N, k , M, mu, p0, lams = [0.02,0.03,0.04] , fig4=False):
    """
    Reproduce fig3 from paper.
    
    
    Density of infected nodes a sa function of time 
    in supercritical spreading experiments in the ER network.
    """ 
    for lam in lams:
        g = nx.fast_gnp_random_graph(N, float(k)/N, directed=True)  # net
        sis = SIS(g, lam, mu, p0)  # sis model
        
        p =[len(sis.inf)/float(N)]
        for j in range(M):
            sis.update()
            p.append(len(sis.inf)/float(N))
        plt.plot(p)
    
    if fig4:
        plt.yscale('log')
    else:
        plt.xscale('log')
    plt.xlabel('t')
    plt.ylabel('p')
    
    
# super critical spreading
# need to be 0.03 above threshold to make it happen
# runs for a minute

fig34(N=10000, k=10., M=1000, mu=0.1, lams=[0.013,0.015,0.02], p0=0.01)

# subcritical spreading, (much larger net, its faster...)
# only change lams for splitgly larger
# runs for a minute

fig34(N=100000, k=10., M=100, mu=0.1, lams=[0.005,0.007,0.009],
      p0=0.5, fig4=True)




def fig1(N, M, k = 3.8, mu = 0.038, lams = [0.005,0.01,0.02],  p0 = 0.5 ,
         gamma = 2.5, in_scale_free=True, out_scale_free=True):
    """
    Reproduce fig1 from paper.
    
    Density of infected nodes as a function of lamdba.
    """
    # scale free-ish directed network
    gs = scale_free_graph(N, gamma, in_scale_free, out_scale_free)
    # ER net
    g = nx.fast_gnp_random_graph(N, float(k)/N, directed=True)
    pe, ps = [], []
    for lam in lams:
        sis = SIS(g, lam, mu, p0)  # sis model
        for j in range(M):
            sis.update()
        pe.append(len(sis.inf)/float(N))
        
        sis = SIS(gs, lam, mu, p0)  # sis model
        for j in range(M):
            sis.update()
        ps.append(len(sis.inf)/float(N))
        
    plot(lams,pe,'o-',label='ER')
    plot(lams,ps,'x:',label='SF')
    plt.xlabel(r'$\lambda$')
    plt.ylabel('p')
    

# p from lambda
%%time
fig1(N=10000, M=1000, lams = [0.005,0.01,0.02,0.03,0.04])



from scale_free import scale_free_graph

def fig1b(N, M, k = 3.8, mu = 0.038, lams = [0.005,0.01,0.02],  p0 = 0.1 ,
         gamma = 2.5, in_scale_free=True, out_scale_free=True):
    """
    Reproduce fig1 from paper.
    
    Density of infected nodes as a function of lamdba.
    """
    # scale free-ish directed network
    gs = scale_free_graph(N, gamma, in_scale_free, out_scale_free)
    print 'k',sum(gs.degree().values())/float(N)
    pe, ps = [], []
    for lam in lams:
        
        sis = SIS(gs, lam, mu, p0)  # sis model
        for j in range(M):
            sis.update()
        ps.append(len(sis.inf)/float(N))
        
    plot(lams,ps,'x:',label='SF')
    plt.xlabel(r'$\lambda$')
    plt.ylabel('p')
    
    
%%time
fig1b(N=1000, M=1000, lams = [0.01,0.02,0.05,0.1,0.2])



g = scale_free_graph(N=10000, gamma = 2.9, in_scale_free=True, 
                         out_scale_free = True)




    
def fig9(N, M, lams = [0.1,0.2], p0 = 0.001 ,
         gamma = 2.1, in_scale_free=False, out_scale_free=False):
    """
    Reproduce fig9 from paper.
    
    
    Density of infected nodes a sa function of time 
    in supercritical spreading experiments in the SF network.
    """ 
    g = scale_free_graph(N, gamma, in_scale_free, out_scale_free)
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
        plt.plot(p)
    
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('t')
    plt.ylabel('p')

%%time
fig9(10000, 1000, lams = [0.2,0.3,0.4])


%%time
fig9(10000, 1000, lams = [0.00001,0.0001,0.01,0.09], p0=0.1)









    
if __name__ == '__main__':
    %pylab inline
    
    mu = 0.02
    lam = 0.1
    p0 = 0.2
    
    N = 1000
    k = 2.
    p = k/N
    
    
    g = nx.fast_gnp_random_graph(N, p, directed=True)
    #g = nx.scale_free_graph(N)
    

    sis = SIS(g, lam, mu, p0)
    p =[len(sis.inf)]
    for j in range(1000):
        sis.update()
        p.append(len(sis.inf))
    plot(p)
    xscale('log')
        
   