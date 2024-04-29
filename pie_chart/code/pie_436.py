
import matplotlib.pyplot as plt
import numpy as np

labels = ["Personal Income Tax","Corporate Tax","Sales Tax","Property Tax"]
sizes = [45,35,15,5]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

ax.pie(sizes, labels = labels, autopct='%1.1f%%',
        startangle=90, pctdistance=0.85,
        wedgeprops=dict(width=0.5, edgecolor='w'))

centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Distribution of Tax Revenue in the USA, 2023")
plt.axis('equal')
plt.tight_layout()
plt.xticks([])
plt.savefig("pie chart/png/32.png")
plt.clf()