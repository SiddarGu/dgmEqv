
import matplotlib.pyplot as plt
import numpy as np

data = [['Facebook',3200,2100],['Twitter',1000,400],['Instagram',800,200],['YouTube',1200,500]]
platform = [x[0] for x in data]
users = [x[1] for x in data]
revenue = [x[2] for x in data]

x = np.arange(len(data))
width = 0.35

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
ax.bar(x-width/2, users, width, label='Users (million)', color='#2ecc71')
ax.bar(x+width/2, revenue, width, label='Ad revenue (million)', color='#3498db')
ax.set_xticks(x)
ax.set_xticklabels(platform)
ax.set_title('Number of users and ad revenue for four social media platforms in 2021')
ax.legend()

for i, v in enumerate(users):
    ax.text(x = i-0.2 , y = v+200, s = v, color='#2ecc71', fontweight='bold')

for i, v in enumerate(revenue):
    ax.text(x = i+0.2 , y = v+100, s = v, color='#3498db', fontweight='bold')

plt.tight_layout()
plt.savefig('Bar Chart/png/607.png', dpi = 600)
plt.clf()