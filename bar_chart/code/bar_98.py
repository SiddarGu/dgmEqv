
import matplotlib.pyplot as plt
import numpy as np

data = [['USA', 400, 25000],
        ['UK', 250, 20000],
        ['Germany', 150, 15000],
        ['France', 200, 18000]]

fig=plt.figure()
ax = fig.add_subplot()
x = np.arange(len(data))
width = 0.2

ax.bar(x-width, [i[1] for i in data], width, label='Donation Amount(million)', color='lightblue')
ax.bar(x, [i[2] for i in data], width, label='Number of Donors', color='pink')
ax.set_xticks(x)
ax.set_xticklabels([i[0] for i in data], rotation=90, wrap=True)
ax.set_title('Total Donation Amount and Number of Donors in four countries in 2021')
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/19.png')
plt.clf()