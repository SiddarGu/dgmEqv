
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111)

labels = ['Netflix', 'Hulu', 'Amazon Prime', 'Disney+', 'Crackle', 'HBO Max', 'Others']
sizes = [40, 20, 10, 15, 5, 5, 5]

ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90, textprops={'fontsize': 14, 'wrap': True})

ax.axis('equal')
ax.set_title('Popular Streaming Services Usage in the USA, 2023', fontsize = 14)

plt.tight_layout()
plt.savefig('pie chart/png/324.png')
plt.clf()