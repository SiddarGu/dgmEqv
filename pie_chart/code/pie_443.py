
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
labels = ['Crops','Dairy','Poultry','Fisheries','Livestock']
sizes = [40,20,20,10,10]
explode = [0.1,0,0,0,0]
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode, shadow=True, textprops={'fontsize': 6, 'rotation':45, 'wrap':True})
ax.axis('equal')
ax.set_title("Agriculture Production Distribution in the USA, 2023")
plt.tight_layout()
plt.savefig('pie chart/png/78.png')
plt.clf()