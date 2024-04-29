
import matplotlib.pyplot as plt
import numpy as np

Country = ["USA","UK","Germany","France"]
Internet_users = [350,250,200,180]
Mobile_users = [320,220,190,160]

x = np.arange(len(Country))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x - width/2, Internet_users, width, label='Internet users (million)')
ax.bar(x + width/2, Mobile_users, width, label='Mobile users (million)')
ax.set_ylabel('Number of users (million)')
ax.set_title('Number of Internet and Mobile users in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend()

for i in range(len(Country)):
    ax.annotate('%d' % Internet_users[i], xy=(x[i] - width/2, Internet_users[i]), xytext=(0, 3), textcoords='offset points', color='black')
    ax.annotate('%d' % Mobile_users[i], xy=(x[i] + width/2, Mobile_users[i]), xytext=(0, 3), textcoords='offset points', color='black')

plt.tight_layout()
plt.savefig('Bar Chart/png/205.png')
plt.clf()