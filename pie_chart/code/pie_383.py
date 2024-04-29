
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 8))
plt.title("Popularity of Art Forms in the USA, 2023")

labels = ['Music', 'Visual Arts', 'Theatre', 'Literature', 'Dance', 'Film']
sizes = [25, 25, 15, 15, 10, 10]
colors = ['#FFB6C1', '#FFC0CB', '#FF1493', '#DB7093', '#C71585', '#8B008B']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, 
        wedgeprops={'linewidth': 1.5, 'edgecolor': 'black'})

#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.tight_layout()

plt.savefig('pie chart/png/67.png', format='png', dpi=300)
plt.show()
plt.clf()