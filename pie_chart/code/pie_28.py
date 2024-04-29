
import matplotlib.pyplot as plt
import numpy as np

data = {'Components':['Raw Materials','Machinery','Labor','Utilities','Other'],
        'Percentage':[20,25,35,10,10]}

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

labels = data['Components']
sizes = data['Percentage']
colors = ['#66b3ff','#99ff99','#ff9999','#ffcc99','#b3b3cc']

ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
ax.set_title("Distribution of Resources in Manufacturing Production, 2023")
ax.axis('equal')

plt.tight_layout()
plt.savefig('pie chart/png/318.png')
plt.show()
plt.clf()