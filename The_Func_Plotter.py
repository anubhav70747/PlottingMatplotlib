import numpy as np
import matplotlib.pyplot as plt
import pickle
# this code is an attempt to plot functions.

# define the functions one wants to plot
def eval_eta_avg(x):
    return (1+x)/2
def eval_a(x):
    return 0.5*(1+1/(1+x))
def eval_b(x):
    ans=[]
    for i in x:
        if i <= 1/3.0:
            ans.append( 1/(1+i))
        else:
            ans.append(3/4.0)
    return ans
def eval_c(x):
    angle=np.arctan((1-x)/(1+x))
    return 0.25*(2+np.cos(angle)+((1-x)/(1+x))*np.sin(angle))

def eval_eta_avg3(x):
    return (1+2*x)/3
def eval_a3(x):
    ans=[]
    for i in x:
        val=0.5*(1+1/(1+2*i))
        if val >= 3/4.0:
            ans.append(val)
        else:
            ans.append(3/4.0)
    return ans

def eval_b3(x):
    ans=[]
    for i in x:
        if i <= 0.3:
            ans.append(1/3.0*(1+2/(1+2*i)))
        else:
            ans.append(3/4.0)
    return ans
def eval_c3(x):
    ans=[]
    for i in x:
        N=  (2*(1-i))/(1+2*i)
        a= np.arccos(1/(N*N-1))
        b= np.arctan(np.tan(a)/N)
        phi=0.125*(4+(1+np.cos(a))*np.cos(b)+N*np.sin(a)*np.sin(b))
        if phi >= 3/4.0:
            ans.append(phi)
        else:
            ans.append(3/4.0)
    return ans
# x limit?
plt.xlim(0.5,1)
#plt.xlim(0.5,1)
# ask matplotlib to use latex
plt.rc('text', usetex=True)
# plot stuff already
# first the x axis
x=np.arange(0.0,1.0,0.01)
plt.xlabel('$\eta_{avg}$',size=16)
# next up the y axis
#plt.plot(eval_eta_avg3(x),eval_a3(x),ls='-',linewidth=4)
#plt.plot(eval_eta_avg3(x),eval_b3(x),ls=':',linewidth=4)
#plt.plot(eval_eta_avg3(x),eval_c3(x),ls='--',linewidth=4)
plt.plot(eval_eta_avg(x),eval_a(x),ls='-',linewidth=4)
plt.plot(eval_eta_avg(x),eval_c(x),ls='--',linewidth=4)
plt.axhline((2+2**0.5)/4, linestyle='--', color='k')
#plt.axhline((3+3**0.5)/6, linestyle='--', color='k')
plt.ylabel('$P_B^{\mathcal{C}}(\eta)$',size=16)
#set tick label size
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
# legendary
plt.legend(('(a)','(b)'))
plt.grid()
plt.show()

