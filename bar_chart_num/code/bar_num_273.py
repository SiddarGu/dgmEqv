
import matplotlib.pyplot as plt
import numpy as np

Platform = [ 'Facebook', 'YouTube', 'Twitter', 'Instagram' ]
Users = [ 2.00, 2.50, 0.80, 1.20 ]
Revenue = [ 65, 20, 7, 15 ]

x = np.arange(len(Platform))
width = 0.35

fig, ax = plt.subplots(figsize=(7,6))
ax.bar(x - width/2, Users, width, label='Users (millions)')
ax.bar(x + width/2, Revenue, width, label='Revenue (million USD)')

ax.set_xticks(x)
ax.set_xticklabels(Platform)
ax.set_ylabel('Number of users and revenue')
ax.set_title('Number of users and revenue of four major social media platforms in 2021')
ax.legend(loc='upper center',bbox_to_anchor=(0.5,-0.2),ncol=2)
ax.autoscale_view()

for i, v in enumerate(Users):
    ax.text(x[i] - width/2, v + 0.5, str(v), color='blue', fontweight='bold')

for i, v in enumerate(Revenue):
    ax.text(x[i] + width/2, v + 0.5, str(v), color='red', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/575.png')

plt.clf()