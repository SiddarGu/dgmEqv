
import matplotlib.pyplot as plt
import numpy as np

labels = ['Fashion','Electronics','Home and Kitchen','Beauty and Personal Care','Groceries','Other']
sizes = [25,20,15,20,10,10]

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 10, 'wrap': True, 'rotation': 0})
ax.axis('equal')

plt.title('Distribution of Retail Products in the US, 2023')
plt.tight_layout()

plt.xticks([])

plt.savefig('pie chart/png/379.png')

plt.clf()