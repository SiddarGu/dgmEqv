

import matplotlib.pyplot as plt
import numpy as np

data = np.array([[20000, 5000], [21000, 5500], [22000, 6000], [25000, 6500], [28000, 7000], [30000, 7500], [32000, 8000]])

fig = plt.figure(figsize=(10,6))
ax1 = fig.add_subplot(1,1,1)
ax1.plot(data[:,0], color='tab:blue', label='Number of Users')
ax1.plot(data[:,1], color='tab:orange', label='Number of Posts')

months = ["January", "February", "March", "April", "May", "June", "July"]
ax1.set_xticks(np.arange(len(months)))
ax1.set_xticklabels(months, rotation=45, ha="right", wrap=True)

plt.title('Monthly user and post growth on Social Media Platform')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/11.png')
plt.clf()