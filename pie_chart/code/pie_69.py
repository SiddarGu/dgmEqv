
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('equal')

labels = ['Income Tax','Property Tax','Sales Tax','Social Security Tax','Corporate Tax','Other']
sizes = [30,25,15,10,10,10]
explode = np.zeros(len(labels))

plt.title('Distribution of Taxation in the USA, 2023')
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 10, 'rotation': 0, 'wrap': True})

plt.savefig('pie chart/png/243.png')
plt.tight_layout()
plt.show()
plt.clf()