import matplotlib.pyplot as plt
import pickle
# this code is an attempt to get good quality graphs in rather smooth way.

# FIRST PLOT
data_file='data/alphaQ1vsd.plot'  # enter the name of your data file
with open (data_file, 'rb') as fp: # load the file up
    itemlist = pickle.load(fp) # store the shite it in a variable
x=itemlist[0]
y=itemlist[1]
#plt.plot(x,y,linewidth=4,ls='--')
plt.plot(x,y,markersize=10,marker='D')

# SECOND PLOT
data_file='data/alphaQvsd.plot'  # enter the name of your data file
with open (data_file, 'rb') as fp: # load the file up
    itemlist = pickle.load(fp) # store the shite it in a variable
x=itemlist[0]
y=itemlist[1]
#plt.plot(x,y,linewidth=4,ls='--')
plt.plot(x,y,markersize=10,marker='o')

# THIRD PLOT
data_file='data/classicalvsd.plot'  # enter the name of your data file
with open (data_file, 'rb') as fp: # load the file up
    itemlist = pickle.load(fp) # store the shite it in a variable
x=itemlist[0]
y=itemlist[1]
#plt.plot(x,y,linewidth=4)
#plt.plot(x,y,markersize=10,marker='*')
#set axes limits
plt.xlim(2,10)
plt.ylim(1.4,5)
# ask matplotlib to use latex
plt.rc('text', usetex=True)
# label axes
plt.ylabel("$\Theta$",size=16)
plt.xlabel('$d$',size=16)
# add legend
plt.legend(('quantum upper bound level=$1$','quantum lower bound','classical'))
#set tick label size
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
# annotate some points

#plt.annotate(r'$p(S_n^i)=\frac{3}{4},p(S_k^j)=1$',xy=(0.75, 1), xytext=(30, 10),textcoords='offset points', va='bottom',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

#plt.annotate(r'$p(S_n^i)=\frac{7}{8},p(S_k^j)=\frac{3}{4}$',xy=(0.875, 0.75), xytext=(0, 20),textcoords='offset points', va='bottom',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

#plt.annotate(r'$p(S_n^i)\approx 0.68,p(S_k^j)= \frac{2+\sqrt{2}}{4}$',xy=(0.68,0.8535), xytext=(-80, -30),textcoords='offset points', va='top',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

#plt.annotate(r'$p(S_n^i)\approx \frac{4}{5},p(S_k^j)= \frac{3}{4}$',xy=(0.8,0.75), xytext=(-90, -40),textcoords='offset points', va='top',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

#plt.annotate(r'$p(S_n^i)= \frac{3}{4},p(S_n^j)= \frac{3}{4}$',xy=(0.75,0.75), xytext=(-90, -40),textcoords='offset points', va='bottom',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

#plt.annotate(r'$p(S_3)= \frac{5}{6},\\p_{A_1A_2}(S_2)+p_{A_1A_3}(S_2)= \frac{3}{2}$',xy=(0.834,1.5), xytext=(20, -7),textcoords='offset points', va='top',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

#plt.annotate(r'$p(S_3)= \frac{3}{4},\\p_{A_1A_2}(S_2)+p_{A_1A_3}(S_2)= \frac{3}{2}$',xy=(0.75,1.5), xytext=(-110, -45),textcoords='offset points', va='top',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

#plt.annotate(r'$p_{A_1A_2A_3}(M_3)= \frac{3}{4},p(S_2)= 1$',xy=(0.75,1.5), xytext=(-110, -45),textcoords='offset points', va='top',bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))

# add grid to make shite look profess!
plt.grid()

# save the figure!
plt.savefig('../../../alphavs_d.pdf',bbox_inches='tight')

#display graph
plt.show()

