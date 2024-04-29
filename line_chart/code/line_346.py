
import matplotlib.pyplot as plt
import numpy as np

year = np.array([2015, 2016, 2017, 2018])
users_A = np.array([1000, 1200, 800, 1500])
users_B = np.array([800, 900, 1100, 1200])
users_C = np.array([1200, 1100, 1300, 1400])
users_D = np.array([1500, 1600, 1200, 800])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.set_title('Number of Users of four different websites from 2015 to 2018',
             fontsize=14)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Users (million)')

ax.plot(year, users_A, 'g-o', label='Users A')
ax.plot(year, users_B, 'b-o', label='Users B')
ax.plot(year, users_C, 'r-o', label='Users C')
ax.plot(year, users_D, 'y-o', label='Users D')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5),
          fontsize=12)
ax.grid(True, linestyle='--')
plt.xticks(year)
plt.tight_layout()
plt.savefig('line chart/png/424.png', dpi=300)
plt.clf()