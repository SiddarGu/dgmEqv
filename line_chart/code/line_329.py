
import matplotlib.pyplot as plt 
import numpy as np 

fig=plt.figure(figsize=(6,4))
ax=fig.add_subplot()
x=np.array([2015,2016,2017,2018,2019,2020])
y1=[3000,4500,6000,7500,9500,11000]
y2=[500,1000,1500,2000,2500,3000]

ax.plot(x,y1,label='Internet Users(millions)',ls='--',marker='o',color='#00A8A8')
ax.plot(x,y2,label='Number of Smartphones Sold(millions)',ls='--',marker='s',color='#FF0000')

ax.set_xlabel('Year')
ax.set_title('Growth of Internet Users and Smartphone Sales from 2015 to 2020', fontsize=12)
ax.grid(linestyle='--',color='gray',alpha=0.5)
ax.set_xticks(x)
ax.legend(loc='upper left',frameon=False)
plt.tight_layout()
plt.savefig('line chart/png/495.png')
plt.clf()