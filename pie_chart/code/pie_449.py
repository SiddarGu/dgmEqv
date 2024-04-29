
import matplotlib.pyplot as plt
import numpy as np

labels = ['Social Media', 'Television', 'Streaming Services', 'Radio', 'Print']
sizes = [45, 20, 18, 10, 7]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 12, 'rotation': 0})
ax.axis('equal')
plt.title("Popularity of Media Platforms in the USA, 2023")
plt.tight_layout()
plt.xticks(np.arange(0, 360, step=45))
plt.savefig('pie chart/png/370.png', bbox_inches='tight')
plt.clf()