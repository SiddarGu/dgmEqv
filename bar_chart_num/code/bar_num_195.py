

import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes
fig = plt.figure()
ax = fig.add_subplot()

# Set font size
plt.rcParams.update({'font.size': 11})

# Set data
countries = ['USA', 'UK', 'Germany', 'France']
twitter_users = [330, 50, 70, 60]
youtube_users = [250, 60, 90, 80]
instagram_users = [300, 100, 110, 120]

# Plot the bars
barWidth = 0.25
r1 = np.arange(len(twitter_users))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Draw the bars
ax.bar(r1, twitter_users, width=barWidth, color='#008080', edgecolor='black', label='Twitter Users')
ax.bar(r2, youtube_users, width=barWidth, color='#00FF00', edgecolor='black', label='YouTube Users')
ax.bar(r3, instagram_users, width=barWidth, color='#FF0000', edgecolor='black', label='Instagram Users')

# Set ticks on x-axis
plt.xticks([r + barWidth for r in range(len(twitter_users))], countries)

# Set title
ax.set_title('Number of Social Media Users in four countries in 2021')

# Add legend
ax.legend(loc='lower center', ncol=3, bbox_to_anchor=(0.5, -0.12), frameon=False)

# auto adjust the size of the figure
fig.tight_layout()

# Add value labels
def autolabel(rects):
    """Attach a text label above each bar displaying its height"""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

# Call functions to implement the function of adding labels
autolabel(ax.patches)

# Save the figure
plt.savefig('Bar Chart/png/14.png')

# Clear the figure
plt.clf()