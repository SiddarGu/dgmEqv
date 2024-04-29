
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA','UK','Germany','France']
GDP_billion = [20,15,12,10]
Gov_Spending_billion = [15,12,10,8]

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
width = 0.2

ax.bar(np.arange(len(Country))-width, GDP_billion, width, color='b', label='GDP')
ax.bar(np.arange(len(Country)), Gov_Spending_billion, width, color='g', label='Gov_Spending')

ax.set_xticks(np.arange(len(Country)))
ax.set_xticklabels(Country)

ax.set_title('GDP and government spending in four countries in 2021')
ax.set_ylabel('billions')
ax.legend()

for x_pos, y_val in enumerate(GDP_billion):
    ax.annotate('{}'.format(y_val), xy=(x_pos-width, y_val+0.5), xytext=(x_pos-width, y_val+0.5), rotation=90)

for x_pos, y_val in enumerate(Gov_Spending_billion):
    ax.annotate('{}'.format(y_val), xy=(x_pos, y_val+0.5), xytext=(x_pos, y_val+0.5), rotation=90)

plt.tight_layout()
plt.savefig('Bar Chart/png/98.png')
plt.clf()