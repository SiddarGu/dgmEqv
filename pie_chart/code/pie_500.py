
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)
labels = ['Road','Rail','Air','Water','Pipeline']
sizes=[45,20,25,5,5]

ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
       textprops={'fontsize': 12}, 
       wedgeprops={'linewidth': 2, 'edgecolor': 'white'})

ax.set_title('Distribution of Transportation Mode in the USA, 2023', fontsize=15)
ax.axis('equal')
ax.legend(loc='upper left', bbox_to_anchor=(1, 0.5))
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig('pie chart/png/334.png')
plt.clf()