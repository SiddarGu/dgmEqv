
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(15,5))
ax = fig.add_subplot(111)
region = ['Asia', 'Europe', 'Africa', 'South America']
recycling_rate = [30,35,25,32]
carbon_footprint = [10000,12000,13000,15000]
x_pos = np.arange(len(region))
bar1 = ax.bar(x_pos,recycling_rate,color='grey',width=0.4,label='Recycling Rate(%)')
bar2 = ax.bar(x_pos+0.4,carbon_footprint,color='green',width=0.4,label='Carbon Footprint(Kg)')
ax.set_xticks(x_pos+0.4/2)
ax.set_xticklabels(region)
ax.legend(loc='upper left')
ax.set_title('Recycling rate and carbon footprint across four regions in 2021')
for b1,b2 in zip(bar1,bar2):
    h1 = b1.get_height()
    h2 = b2.get_height()
    ax.annotate('{}'.format(h1),xy=(b1.get_x()+b1.get_width()/2,h1/2),ha='center',va='center',rotation=90,size=8)
    ax.annotate('{}'.format(h2),xy=(b2.get_x()+b2.get_width()/2,h2/2),ha='center',va='center',rotation=90,size=8)
plt.tight_layout()
plt.savefig('Bar Chart/png/60.png')
plt.clf()