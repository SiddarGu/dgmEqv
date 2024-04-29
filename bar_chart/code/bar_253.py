
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[12, 30, 90],[14, 25, 85],[10, 28, 92],[18, 22, 87]])

x = np.arange(4)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()

ax.bar(x - 0.2, data[:,0], width=0.2, label='Trainings')
ax.bar(x, data[:,1], width=0.2, label='New Employees')
ax.bar(x + 0.2, data[:,2], width=0.2, label='Retention Rate')

ax.set_xticks(x)
ax.set_xticklabels(['Company A', 'Company B', 'Company C', 'Company D'], rotation=90)
ax.set_title('Employee management in four companies in 2021')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.savefig('bar chart/png/61.png')
plt.clf()