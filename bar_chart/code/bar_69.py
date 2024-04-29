
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)
plt.bar(['Football', 'Basketball', 'Tennis', 'Badminton'], [20, 18, 15, 15], color='#2196f3', label='Tournaments')
plt.bar(['Football', 'Basketball', 'Tennis', 'Badminton'], [20000, 15000, 10000, 8000], bottom=[20, 18, 15, 15], color='#ffc107', label='Viewers')
ax.set_xticks(range(4))
ax.set_xticklabels(['Football', 'Basketball', 'Tennis', 'Badminton'], rotation=0, wrap=True)
ax.set_title('Number of tournaments and viewers for four sports in 2021')
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/246.png')
plt.clf()