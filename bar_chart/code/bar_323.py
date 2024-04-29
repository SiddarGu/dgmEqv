

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(14,6))
ax = fig.add_subplot()
ind = np.arange(4)
width = 0.30
x_label = ('USA','UK','Germany','France')
ax.bar(ind, [3000,2500,2000,1500], width, label='Fruits')
ax.bar(ind+width, [4000,4500,3500,2500], width, label='Vegetables')
plt.xticks(ind+width/2, x_label, rotation=45)
ax.legend(loc='upper center')
plt.title('Food production of fruits and vegetables in four countries in 2021')
plt.tight_layout()
plt.savefig('bar chart/png/107.png')
plt.clf()