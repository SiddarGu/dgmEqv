

import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ax.axis('equal')

labels = ['Livestock','Dairy','Fruits and Vegetables','Grains','Aquaculture']
data = [25,20,30,15,10]

ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=0, textprops={'fontsize':12})

ax.set_title('Agriculture Production Distribution in the USA, 2023')
plt.legend(labels, loc="center left", bbox_to_anchor=(1.0, 0, 0.5, 1))

plt.tight_layout()
plt.xticks(rotation=-45)
plt.savefig('pie chart/png/439.png')
plt.clf()