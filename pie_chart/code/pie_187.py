
import matplotlib.pyplot as plt
import numpy as np

labels = ['Soccer','Basketball','Baseball','Hockey','Golf','Tennis']
sizes = [30,25,20,15,5,5]

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14, 'color': 'black'}, explode=(0.1, 0, 0, 0, 0, 0))
plt.title('Popularity of Sports in the United States, 2023', fontsize=16, wrap=True)
ax.axis('equal')
plt.tight_layout()
fig.savefig("pie chart/png/343.png")
plt.clf()