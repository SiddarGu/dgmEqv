
import matplotlib.pyplot as plt
import numpy as np

labels = ['Television', 'Social Media', 'Streaming Services', 'Radio', 'Print Media']
percentages = [45, 25, 15, 10, 5]

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
ax.pie(percentages, labels=labels, autopct='%.2f%%', textprops={'rotation': 0, 'wrap': True})
ax.set_title('Popularity of Sports Platforms in the US in 2023')
plt.tight_layout()
plt.xticks(rotation=90)
plt.savefig('pie chart/png/333.png')
plt.clf()