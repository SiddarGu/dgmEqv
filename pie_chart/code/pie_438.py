
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

plt.figure(figsize=(9, 9))
labels = ['Full-time', 'Part-time', 'Contractors', 'Interns']
sizes = [50, 25, 15, 10]
colors = ['#00e600', '#ff8c00', '#a180cc', '#ff0000']
explode = [0, 0.1, 0, 0]

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', explode=explode, shadow=True, startangle=90)
plt.title('Employee Distribution in the USA, 2023', fontsize=20)
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/98.png')
plt.gca().set_aspect('equal')
plt.xticks([])
plt.show()
plt.clf()