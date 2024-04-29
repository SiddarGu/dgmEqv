
import matplotlib.pyplot as plt
import numpy as np

# define the data
country = ["USA", "UK", "Germany", "France"]
sports_viewers = [500, 480, 450, 470]
entertainment_viewers = [600, 620, 650, 630]

# create figure
fig = plt.figure(figsize=(10,6))

# define add_subplot
ax = fig.add_subplot()

# draw the bars
ax.bar(country, sports_viewers, label='Sports Viewers', bottom=entertainment_viewers)
ax.bar(country, entertainment_viewers, label='Entertainment Viewers')

# add title and legend
ax.set_title('Number of viewers for sports and entertainment in four countries in 2021')
ax.legend()

# set x ticks, y limits
ax.set_xticks(np.arange(4))
ax.set_xticklabels(country, rotation=45, ha='right')
ax.set_ylim(0, 1200)

plt.tight_layout()

# save the figure
plt.savefig('bar chart/png/522.png')

# clear the current figure
plt.clf()