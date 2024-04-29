

import matplotlib.pyplot as plt
import numpy as np
 
# Data to plot 
Platform = ['Instagram', 'YouTube', 'Twitter', 'Facebook'] 
Users_million = [1.5, 2.3, 1.2, 3.5]
Usage_time = [2, 3, 1.5, 4.5]
 
# Create figure
fig, ax = plt.subplots(figsize=(10,6))

# Plotting the Bars
ax.bar(Platform, Users_million, bottom=Usage_time, label="Users (million)")
ax.bar(Platform, Usage_time, label="Usage Time")
 
# Adding the legend and title
ax.legend(loc='upper left')
ax.set_title('Social media platform usage and user data in 2021') 

# Setting x-axis and y-axis limits
ax.set_xlim([-0.5,3.5])
ax.set_ylim([0,7])

# Setting xticks
plt.xticks(np.arange(len(Platform)), Platform)

# Labeling the bars
for x,y in zip(Platform,Usage_time):
    plt.annotate(y, # this is the text
                 (x,y+0.5), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

for x,y in zip(Platform,Users_million):
    plt.annotate(y, # this is the text
                 (x,y+0.5), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

# Auto adjust subplot parameters to give specified padding
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/580.png')

# Clear current image state 
plt.clf()