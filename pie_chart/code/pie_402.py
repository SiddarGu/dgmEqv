
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

labels = ['Flexible Work Hours', 'Remote Work', 'Paid Time Off', 'Benefits and Wellness Programs', 'Onsite Childcare']
sizes = [30, 30, 20, 10, 10]

ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize':14, 'wrap':True, 'rotation':90}, shadow=True)
ax.axis('equal')
ax.set_title("Employee Benefits and Flexibility in the U.S., 2023", fontsize=16)

plt.tight_layout()
plt.xticks([])
plt.savefig('pie chart/png/398.png')
plt.clf()