
import matplotlib.pyplot as plt
import numpy as np

labels = ['Paintings', 'Sculptures', 'Music', 'Theater', 'Dance', 'Film']
values = [25, 20, 25, 15, 10, 5]

fig = plt.figure(figsize=(11,7))
ax = fig.add_subplot(111)
ax.axis('equal')

wedges, texts, autotexts = ax.pie(values, labels=labels,
                                  autopct='%1.1f%%', shadow=False, 
                                  textprops={'fontsize': 14, 'wrap': True, 'rotation': 0} )

ax.set_title("Distribution of Different Artforms in the World, 2023", fontsize=24)

ax.legend(wedges, labels,
          title="Artforms",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.tight_layout()
plt.savefig('pie chart/png/363.png')
plt.clf()