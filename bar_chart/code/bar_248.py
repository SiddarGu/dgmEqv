
import matplotlib.pyplot as plt 
import numpy as np 
x=np.arange(4) 
xlabels=['East','West','North','South'] 
y1=[20,25,30,35] 
y2=[30,35,40,45] 
y3=[25,30,35,40] 

plt.figure(figsize=(10,6)) 
ax=plt.subplot() 
ax.bar(x-0.2,y1,width=0.2,label='Wind Energy(GWh)') 
ax.bar(x,y2,width=0.2,label='Solar Energy(GWh)') 
ax.bar(x+0.2,y3,width=0.2,label='Hydro Energy(GWh)') 

plt.xticks(x,xlabels,rotation=60) 
ax.set_title('Energy production from wind, solar and hydro sources in four regions in 2021') 
ax.legend(loc='upper center') 
plt.tight_layout() 
plt.savefig('bar chart/png/485.png') 
plt.clf()