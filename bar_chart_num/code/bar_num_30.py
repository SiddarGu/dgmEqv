
import numpy as np
import matplotlib.pyplot as plt

data = [['USA', 300, 50],
        ['UK', 100, 40],
        ['Germany', 200, 60],
        ['France', 150, 45]]

country, users, speed = zip(*data)
x_pos = np.arange(len(data))

fig, ax = plt.subplots(figsize=(10,6))
ax.bar(x_pos, users, bottom=speed, color='red', label='Internet Users (million)', width=0.4)
ax.bar(x_pos, speed, color='green', label='Internet Speed (Mb/s)', width=0.4)

ax.set_title('Internet users and speed in four countries in 2021')
ax.set_xticks(x_pos)
ax.set_xticklabels(country)

ax.legend(loc='upper center')

for i, v in enumerate(zip(users, speed)):
    ax.text(i-0.2, v[0] + v[1]/2, str(v[0] + v[1]), color='black', fontweight='bold')
plt.tight_layout()
plt.savefig('Bar Chart/png/93.png')
plt.clf()