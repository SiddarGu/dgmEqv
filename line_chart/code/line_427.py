
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2001,100,80,90,95],
                 [2002,105,85,95,100],
                 [2003,95,90,85,105],
                 [2004,100,95,90,110]])

plt.figure(figsize = (8, 6))
ax = plt.subplot()
ax.plot(data[:,0],data[:,1], marker='o', label='Grain Output (million tons)')
ax.plot(data[:,0],data[:,2], marker='o', label='Cereal Output (million tons)')
ax.plot(data[:,0],data[:,3], marker='o', label='Vegetable Output (million tons)')
ax.plot(data[:,0],data[:,4], marker='o', label='Fruit Output (million tons)')
ax.set_xticks(data[:,0])
ax.set_xlabel('Year')
ax.set_ylabel('Output (million tons)')
ax.legend(loc='upper left',bbox_to_anchor=(1,1))
plt.title('Global Output of Grains, Cereals, Vegetables, and Fruits from 2001 to 2004')
plt.tight_layout()
plt.savefig('line chart/png/381.png')
plt.clf()