
import matplotlib.pyplot as plt
import numpy as np

labels = ['Education', 'Health', 'Defense', 'Social Security', 'Infrastructure', 'Other']
sizes = [15, 20, 25, 20, 10, 10]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 12})
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Breakdown of Government Spending in the USA, 2023")
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/474.png')
plt.clf()