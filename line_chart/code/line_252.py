
import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(10,6))

# draw line chart
ax = plt.subplot()
ax.set_title('Cases Filed, Settled, and Dismissed in US Courts from 2000-2004')
ax.plot(np.arange(2000,2005),[2000,2250,2500,2700,3000],'-',label='Cases Filed')
ax.plot(np.arange(2000,2005),[1000,1250,1500,1750,2000],'-',label='Cases Settled')
ax.plot(np.arange(2000,2005),[500,600,800,900,1000],'-',label='Cases Dismissed')

# set xticks
ax.set_xticks(np.arange(2000,2005))

# set legend
ax.legend(loc='upper center',bbox_to_anchor=(0.5,1.1),ncol=3,fancybox=True,shadow=True,prop={'size':12})

# adjust layout
plt.tight_layout()

# save figure
plt.savefig('line chart/png/58.png')

# clear figure
plt.clf()