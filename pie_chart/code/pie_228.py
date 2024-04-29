
import matplotlib.pyplot as plt
import numpy as np

labels = ['Solar Power','Wind Power','Hydroelectric','Geothermal','Biomass','Nuclear','Other']
sizes = [20,20,15,15,10,10,10]
explode = (0.1,0,0,0,0,0,0)

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)
ax.set_title("Distribution of Renewable Energy Sources in the US, 2023")
ax.pie(sizes,labels=labels,explode=explode,autopct='%1.1f%%',shadow=True)
ax.axis('equal')
ax.legend(loc='upper right',bbox_to_anchor=(1.3,1))
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('pie chart/png/321.png')
plt.clf()