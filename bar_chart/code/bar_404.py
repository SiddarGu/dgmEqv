
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))
ax = plt.subplot()
region = ['North America', 'South America', 'Europe', 'Asia']
football_matches = np.array([160, 180, 140, 200])
cinema_viewers = np.array([200, 220, 190, 250])

width = 0.35
ax.bar(region, football_matches, width, label='Football Matches')
ax.bar(region, cinema_viewers, width, bottom=football_matches, label='Cinema Viewers')

ax.set_title('Number of football matches and cinema viewers in four regions in 2021')
ax.set_ylabel('Number of Events')
ax.set_xticks(region)
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/35.png')
plt.clf()