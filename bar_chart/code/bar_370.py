
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12, 8)) 
ax = fig.add_subplot()
ax.bar(['Facebook', 'Twitter', 'Instagram', 'YouTube'], [2.5, 0.5, 1.5, 2.0], color = 'b', width = 0.4, label='Number of Daily Users (millions)')
ax.set_title('Number of Daily Users of Popular Social Media Platforms in 2021')
plt.xticks(rotation=45, ha='right', wrap=True)
ax.legend(loc='upper left')
plt.tight_layout()
plt.savefig('bar chart/png/7.png')
plt.clf()