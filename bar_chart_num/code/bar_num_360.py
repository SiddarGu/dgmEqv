
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 5)) 
ax = fig.add_subplot(111)

labels = ['Painting','Sculpture','Photography']
Modern_Art = [100, 50, 150]
Renaissance_Art = [80, 60, 120]
Baroque_Art = [90, 70, 130]
Neoclassicism = [120, 80, 140]

x = np.arange(len(labels))
width = 0.2

ax.bar(x - width, Modern_Art, width=width, color='#7D48DF', label='Modern Art')
ax.bar(x, Renaissance_Art, width=width, color='#F8D720', label='Renaissance Art')
ax.bar(x + width, Baroque_Art, width=width, color='#F81D22', label='Baroque Art')
ax.bar(x + (2 * width), Neoclassicism, width=width, color='#00AEEF', label='Neoclassicism')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.set_title('Number of artworks in four categories in 2021')

for i, val in enumerate(Modern_Art):
    ax.annotate(val, xy=(x[i]-width+0.03, val+5))
for i, val in enumerate(Renaissance_Art):
    ax.annotate(val, xy=(x[i]+0.03, val+5))
for i, val in enumerate(Baroque_Art):
    ax.annotate(val, xy=(x[i]+width+0.03, val+5))
for i, val in enumerate(Neoclassicism):
    ax.annotate(val, xy=(x[i]+(2*width)+0.03, val+5))

plt.tight_layout()
plt.savefig('Bar Chart/png/585.png')
plt.clf()