
import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)

region= ['West','East','South','North'] 
recycling = [30,25,35,40]
disposal = [10,20,15,18]

x = np.arange(len(region))
width = 0.35

rects1 = ax.bar(x,recycling,width,label = 'Recycling')
rects2 = ax.bar(x+width,disposal,width,label = 'Hazardous waste disposal')

ax.set_title('Rates of recycling and hazardous waste disposal in four regions in 2021')
ax.set_xticks(x+width/2)
ax.set_xticklabels(region, fontsize = 8, ha = 'center', rotation = 45)
ax.legend(loc = 'best')
ax.set_ylim(0,50)
plt.tight_layout()
plt.savefig('bar chart/png/141.png')
plt.clf()