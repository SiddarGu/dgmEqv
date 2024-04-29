
import matplotlib.pyplot as plt
import numpy as np

labels = ['Drinking Water', 'Industrial Water', 'Irrigation Water', 'Recreational Water', 'Aquatic Ecosystems']
sizes = [25, 15, 30, 20, 10]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.75, labeldistance=1.05, rotatelabels=True, textprops={'fontsize': 11, 'color': 'black', 'wrap': True})
ax.axis('equal')
ax.set_title('Distribution of Water Resources in the US, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/477.png')
plt.clf()