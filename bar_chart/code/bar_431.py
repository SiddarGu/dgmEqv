
import numpy as np
import matplotlib.pyplot as plt

#data
Region = ['North America','South America','Europe','Asia']
Dairy = [200, 300, 250, 280]
Fruits = [450, 500, 480, 520]
Meat = [300, 400, 320, 350]

#plot
fig, ax = plt.subplots(figsize=(10,8))
ax.bar(Region, Dairy, width=0.25, bottom=np.sum([Fruits, Meat], axis=0), label='Dairy')
ax.bar(Region, Fruits, width=0.25, bottom=Meat, label='Fruits')
ax.bar(Region, Meat, width=0.25, label='Meat')
ax.set_xticklabels(Region, rotation=45, wrap=True)
ax.legend()
ax.set_title('Sales of Dairy, Fruits and Meat in four regions in 2021')
plt.tight_layout()
plt.savefig('bar chart/png/313.png')
plt.clf()