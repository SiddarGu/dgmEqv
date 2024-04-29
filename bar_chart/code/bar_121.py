
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

Type = ['Modern Art','Renaissance Art','Baroque Art','Gothic Art']
Painting = [100,90,80,70]
Sculpture = [120,130,140,150]
Photography =[140,150,160,180]

x = np.arange(len(Type)) 
width = 0.2

ax.bar(x, Painting, width, label='Painting', color='blue')
ax.bar(x + width, Sculpture, width, label='Sculpture', color='orange')
ax.bar(x + width + width, Photography, width, label='Photography', color='green')

ax.set_xticks(x + width / 3)
ax.set_xticklabels(Type, rotation='vertical', wrap=True)
ax.legend(loc='best')
ax.set_title('Number of artworks in four different types in 2021')

fig.tight_layout()
fig.savefig("bar chart/png/272.png")
plt.clf()