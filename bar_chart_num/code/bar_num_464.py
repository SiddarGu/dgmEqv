
import matplotlib.pyplot as plt
import numpy as np

Platform = ['YouTube', 'Facebook', 'Twitter', 'Instagram']
Users = np.array([2.8, 2.5, 0.33, 1])

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()
ax.bar(Platform, Users, color = ['red', 'orange', 'green', 'blue'])

ax.set_title('Number of users of four social media platforms in 2021')
ax.set_xlabel('Platform')
ax.set_ylabel('Users (billion)')

for i, v in enumerate(Users):
    ax.text(i, v+0.2, str(v), va='center', ha='center', fontsize=14, color='black')

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('Bar Chart/png/406.png')
plt.clf()