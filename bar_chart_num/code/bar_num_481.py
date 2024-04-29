
import matplotlib.pyplot as plt
import numpy as np

data = [['Facebook',3.2,2.5],['Instagram',1.2,1.8],['Twitter',0.8,1.1],['YouTube',2.1,2.9]]

x, users, avg_time = zip(*data)

fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)
ax.bar(x, users, width=0.3, color="black", bottom=0, label="Users(million)")
ax.bar(x, avg_time, width=0.3, color="red", bottom=users, label="Average Time Spent")

ax.set_title("User Engagement on Social Media Platforms in 2021")
ax.set_xlabel("Platform")
ax.set_ylabel("Value")

ax.legend()

ax.set_xticks(x)
ax.set_yticks(np.arange(0, 6, 0.5))

for i, v in enumerate(zip(users, avg_time)):
    ax.text(i-0.15, v[0]+0.2, str(v[0]), fontsize=10, fontweight="bold")
    ax.text(i-0.15, v[0]+v[1]-0.2, str(v[1]), fontsize=10, fontweight="bold")

plt.tight_layout()
plt.savefig('Bar Chart/png/617.png')

plt.cla()