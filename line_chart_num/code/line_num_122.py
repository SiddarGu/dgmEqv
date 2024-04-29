
import matplotlib.pyplot as plt
import numpy as np

data = [[2.80, 330, 1000], [2.83, 335, 1020], [2.86, 340, 1040], [2.90, 345, 1060], [2.93, 350, 1080], [2.96, 355, 1100], [2.99, 360, 1120], [3.02, 365, 1140]]
months = ['January 2021', 'February 2021', 'March 2021', 'April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021']

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(months, [x[0] for x in data], label='Facebook Users (million)', color='r', marker='o')
ax.plot(months, [x[1] for x in data], label='Twitter Users (million)', color='b', marker='o')
ax.plot(months, [x[2] for x in data], label='Instagram Users (million)', color='g', marker='o')

ax.set_title('Social Media Users Growth in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Users (million)')
ax.legend(loc='best')
ax.grid(linestyle='-.', linewidth=0.5)
ax.set_xticks(months)
for i, txt in enumerate(data):
    ax.annotate(txt, (months[i], data[i][0]+1))
plt.tight_layout()
plt.savefig('line chart/png/325.png', dpi=300)
plt.clf()