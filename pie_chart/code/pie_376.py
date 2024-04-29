
import matplotlib.pyplot as plt
import numpy as np

data = {'Age Group':['0-18','19-35','36-60','60+'],
        'Percentage':[20,35,35,10]}

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)

labels = data['Age Group']
sizes = data['Percentage']

ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 8},
       wedgeprops={'linewidth':2, 'edgecolor':'white'})

plt.title('Percentage of Healthcare Utilization by Age Group in the USA, 2023', fontsize=10, pad=10)
plt.tight_layout()
plt.savefig('pie chart/png/461.png')

plt.clf()