

import matplotlib.pyplot as plt
import numpy as np

labels = ['Automobiles', 'Electronics', 'Aircrafts', 'Household appliances', 'Medical equipment', 'Metals', 'Plastics', 'Textiles', 'Other']
sizes = [30, 25, 15, 10, 10, 5, 5, 5, 5]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()

ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.8, textprops={'fontsize': 14}, wedgeprops={'linewidth': 2, 'edgecolor': 'white'})
ax.set_title('Distribution of Manufacturing Production in 2023', fontsize=14)
ax.axis('equal')
ax.legend(bbox_to_anchor=(1, 0.5), loc='center left', fontsize=14)

plt.tight_layout()
plt.savefig('pie chart/png/272.png', bbox_inches='tight')
plt.clf()