
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['Oil', 'Coal', 'Natural Gas', 'Nuclear', 'Renewables']
sizes = [30, 25, 20, 10, 15]

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
ax.pie(sizes,labels=labels, autopct='%1.1f%%',textprops={'fontsize': 10, 'wrap': True, 'rotation': 60})
ax.set_title('Global Energy Mix in 2023')
plt.tight_layout()
plt.xticks(rotation=60)
plt.savefig('pie chart/png/94.png')
plt.clf()