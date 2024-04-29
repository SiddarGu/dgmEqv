
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(10,7))
ax = fig.add_subplot()

country = np.arange(4)
theater = [50, 30, 40, 20]
museum = [60, 40, 50, 30]
gallery = [70, 50, 60, 40]

ax.bar(country, theater, width=0.2, bottom=0, label='Theater')
ax.bar(country+0.2, museum, width=0.2, bottom=0, label='Museum')
ax.bar(country+0.4, gallery, width=0.2, bottom=0, label='Gallery')

ax.set_xticks(country+0.2)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'], fontsize=12, rotation=20)
ax.set_title('Number of theater, museum, and gallery visits in four countries in 2021', fontsize=16)
ax.set_xlabel('Country', fontsize=14)
ax.set_ylabel('Number of visits', fontsize=14)
ax.legend(loc=2, fontsize=12)

plt.tight_layout()
plt.savefig('bar chart/png/137.png')
plt.clf()