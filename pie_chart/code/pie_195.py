

import matplotlib.pyplot as plt
import numpy as np

labels = ['Automation', 'Robotics', 'Artificial Intelligence', '3D Printing', 'Human Labor']
percentage = [30, 25, 20, 15, 10]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.axis('equal')
ax.pie(percentage, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90, pctdistance=0.85,
        textprops={'fontsize': 14})

plt.title('Manufacturing Production Types Distribution in 2023', fontsize=20, y=1.08)
plt.legend(labels, bbox_to_anchor=(1,0.5), loc="center right", fontsize=14)

plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('pie chart/png/288.png', bbox_inches='tight')
plt.clf()