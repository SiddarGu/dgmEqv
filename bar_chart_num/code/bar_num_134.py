
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[400, 500, 1000], [350, 450, 900], [380, 400, 800], [420, 500, 1100]])
x = np.arange(4)
fig, ax = plt.subplots(figsize=(8, 4))
p1 = ax.bar(x, data[:, 0], label='Civil Servants', color='#FFE4C4')
p2 = ax.bar(x, data[:, 1], bottom=data[:, 0], label='Policemen', color='#F0E68C')
p3 = ax.bar(x, data[:, 2], bottom=data[:, 0]+data[:, 1], label='Teachers', color='#FFD700')
ax.set_title('Number of government employees in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'])
ax.legend(loc='upper left')
for i, p in enumerate(p1+p2+p3):
    h = p.get_height()
    label = str(h)
    plt.annotate(label, (p.get_x() + p.get_width()/2., h+20),
                 ha='center', va='bottom', rotation=90, fontsize=11)
fig.tight_layout()
plt.savefig('Bar Chart/png/491.png', dpi=300)
plt.clf()