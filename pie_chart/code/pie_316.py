
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

labels = ['Treatment A', 'Treatment B', 'Treatment C', 'Treatment D', 'Treatment E']
percentages = [26, 24, 19, 16, 15]

explode = (0.1, 0, 0, 0, 0)
ax.pie(percentages, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
ax.set_title('Distribution of Healthcare Treatments in the USA, 2023')
fig.tight_layout()

plt.savefig('pie chart/png/388.png')
plt.clf()