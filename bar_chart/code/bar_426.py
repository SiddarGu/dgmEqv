
import matplotlib.pyplot as plt
import numpy as np

platforms = ['Facebook', 'YouTube', 'Instagram', 'Twitter']
users = [2.3, 1.9, 1.2, 0.9]
usage_time = [10, 8, 6, 4]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.bar(platforms, users, label='Users(million)', width=0.4, bottom=0)
ax.bar(platforms, usage_time, label='Usage Time(hours)', width=0.4, bottom=users)

ax.set_title('Number of users and usage time on four popular social media platforms in 2021')
ax.set_ylabel('Quantity')
ax.set_xlabel('Platform')
ax.set_xticks(platforms)
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/316.png')
plt.clf()