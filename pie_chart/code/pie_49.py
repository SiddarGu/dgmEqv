
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(10,8))
ax=fig.add_subplot(111)

plt.title('Popularity of Delivery Modes for Retail Shopping in the USA, 2023')

labels=['Pickup','Curbside','In-store','Home Delivery','Other']
sizes=[32,14,32,20,2]

ax.pie(sizes,labels=labels,autopct='%.2f%%',pctdistance=0.8,textprops={'fontsize': 14})

ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('pie chart/png/148.png')
plt.clf()