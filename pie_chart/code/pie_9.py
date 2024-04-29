
import matplotlib.pyplot as plt

labels = ['Education', 'Social Sciences', 'Arts', 'Humanities', 'Business', 'Media', 'Technology']
sizes = [25, 20, 15, 15, 10, 10, 5]

plt.figure(figsize=(10,10))
ax = plt.subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=90)
plt.title('Popular Career Fields in the USA, 2023')
ax.legend(fontsize=14, bbox_to_anchor=(1,0.8))
plt.axis('equal')
plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/441.png')
plt.clf()