

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, aspect='equal')

labels = ['Air Travel','Car Rental','Hotels and Resorts','Cruise Lines','Tour Operators']
sizes = [30,20,25,15,10]
colors = ['lightcoral','gold','lightskyblue','violet','lightgreen']
explode = (0,0,0,0,0)

ax.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, colors=colors, explode=explode)
ax.axis('equal')
ax.set_title('Distribution of Tourism and Hospitality Spending in 2023')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('pie chart/png/135.png')
plt.clf()