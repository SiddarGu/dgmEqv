
import matplotlib.pyplot as plt
import numpy as np

Country = np.array(['USA', 'UK', 'Germany', 'France'])
Universities = np.array([200, 150, 180, 140])
Students = np.array([15000, 12000, 17000, 13000])

x = np.arange(len(Country))
width = 0.35

fig, ax = plt.subplots(figsize=(10,6))
u_bar = ax.bar(x, Universities, width=width, label='Universities')
s_bar = ax.bar(x + width, Students, width=width, label='Students')

ax.set_xticks(x + width/2)
ax.set_xticklabels(Country, rotation=90, wrap=True)
ax.set_title('Number of universities and students in four countries in 2021')
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/318.png')
plt.clf()