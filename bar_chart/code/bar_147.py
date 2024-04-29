
import numpy as np
import matplotlib.pyplot as plt

# data
Country = ['USA', 'UK', 'Germany', 'France']
Painting = [200, 180, 230, 270]
Sculpture = [350, 370, 320, 350]
Photography = [400, 450, 390, 410]

# create figure
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot()

# plot bar chart
ax.bar(Country, Painting, label="Painting", width=0.2)
ax.bar(Country, Sculpture, bottom=Painting, label="Sculpture", width=0.2)
ax.bar(Country, Photography, bottom=np.add(Painting, Sculpture), label="Photography", width=0.2)

# set xticks
plt.xticks(Country)

# set legend
ax.legend()

# set title
ax.set_title('Number of artworks in four countries in 2021')

# set tight layout
plt.tight_layout()

# save image
plt.savefig('bar chart/png/311.png',dpi=200)

# clear current image state
plt.clf()