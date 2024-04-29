
import matplotlib.pyplot as plt
import numpy as np

labels = ['Cars','Trucks','Aircraft','Rail','Ship']
sizes = [50, 20, 15, 10, 5]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 12, 'color':'black'}, shadow=True, startangle=90, labeldistance=1.1)
ax.axis('equal')
ax.set_title('Distribution of Transportation Modes in the USA, 2023', fontsize='14')
plt.tight_layout()
plt.savefig('pie chart/png/8.png')
plt.clf()