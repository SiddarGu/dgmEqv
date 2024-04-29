
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2001,50,200,100],
                [2002,75,220,125],
                [2003,90,250,150],
                [2004,80,275,175],
                [2005,85,300,200]])

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data[:,0], data[:,1], label="Movies released")
ax.plot(data[:,0], data[:,2], label="Books Published")
ax.plot(data[:,0], data[:,3], label="Music Albums Released")
ax.set_title('Changes in the number of creative works released in the Arts and Culture industry')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Creative Works Released')
ax.legend(loc='upper center')
ax.set_xticks(data[:,0])
plt.tight_layout()
plt.savefig('line chart/png/227.png')
plt.clf()