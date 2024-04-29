
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot()
labels = ['White','Asian','Hispanic or Latino','Black or African American','Native American','Pacific Islander']
sizes = [63,12,15,8,1,1]
explode = (0.1,0,0,0,0,0)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, shadow=True, startangle=90, textprops={'fontsize': 10, 'wrap': True, 'rotation': 0})
ax.set_title('Racial and Ethnic Distribution in the United States, 2023')
plt.axis('equal')
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/526.png')
plt.clf()