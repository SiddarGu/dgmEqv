
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[4500,4000,3500,3000],[8,7,9,6]])

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111)
width = 0.4

ax.bar(np.arange(4)-width/2, data[0], width=width, align='center', color='#f9c3f3', label='Volunteers')
ax.bar(np.arange(4)+width/2, data[1], width=width, align='center', color='#f972f9', label='Donations(million)')
ax.set_xticks(np.arange(4))
ax.set_xticklabels(('North America','Europe','Asia','South America'))
ax.set_title('Donations and Volunteers of Nonprofit Organizations in four regions in 2021')
ax.legend(loc=2)

for i, v in enumerate(data[0]):
    ax.text(i - 0.2, v + 0.2, str(v), fontsize=12)
for i, v in enumerate(data[1]):
    ax.text(i + 0.2, v + 0.2, str(v), fontsize=12)

plt.tight_layout()
plt.savefig('Bar Chart/png/517.png')
plt.clf()