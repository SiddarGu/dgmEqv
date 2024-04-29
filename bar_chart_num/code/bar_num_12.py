
import matplotlib.pyplot as plt
import numpy as np

# create the figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# define the data
country = np.array(['USA', 'UK', 'Germany', 'France'])
fb_users = np.array([200, 90, 120, 130])
ig_users = np.array([130, 50, 60, 70])
tw_users = np.array([160, 80, 70, 90])

# draw the plot
p1 = ax.bar(country, fb_users, color='#FFA500', label='Facebook')
p2 = ax.bar(country, ig_users, bottom=fb_users, color='#0099FF', label='Instagram')
p3 = ax.bar(country, tw_users, bottom=fb_users+ig_users, color='#66CC99', label='Twitter')


# set the title
plt.title("Number of social media users in four countries in 2021")

# set the legend
plt.legend(loc='upper left')

# set the xticks
plt.xticks(country, fontsize=9, rotation=45)

# automatically resize the image
plt.tight_layout()

# save the figure
plt.savefig('bar_12.png')

# clear the current image state
plt.clf()