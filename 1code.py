T     = 1000  
K     = 100
phi = .7
sigma = 1


import numpy as np

I = 10000

e = np.random.normal(0, sigma, [T+K,I]) #array of dimension T x I


Xt = np.copy(e)

for j in range(1,T+K):
	Xt[j:j+1,:]=phi*Xt[j-1:j,:]+e[j:j+1,:]

Xt=Xt[K:,:]