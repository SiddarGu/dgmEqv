
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

plt.figure(figsize=(15, 8))
ax = plt.subplot()

labels = 'Electrical Engineering', 'Computer Science', 'Mechanical Engineering', 'Biomedical Engineering', 'Civil Engineering', 'Chemical Engineering', 'Aerospace Engineering', 'Other'
sizes = [25, 20, 15, 15, 10, 10, 5, 10]
colors = ['#66b3ff','#99ff99','#ff9999','#ffcc99','#ffd11a','#7550b3','#ff66b3','#ffb384']
explode = (0, 0, 0, 0, 0, 0, 0, 0.1)

ax.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%.2f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.title('Percentage of STEM Degrees in the USA, 2023', fontsize=14)
plt.legend(labels, loc='lower left', bbox_to_anchor=(-0.1, -0.2, 1.2, 0), fontsize=12, ncol=2)
plt.tight_layout()
plt.savefig('pie chart/png/209.png')
plt.clf()