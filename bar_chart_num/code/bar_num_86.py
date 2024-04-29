
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
Country=['USA','UK','Canada','Germany']
Technology_Research=[120,130,110,100]
Engineering_Projects=[150,140,160,170]

# Setting up the figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Set the xticks
plt.xticks(np.arange(len(Country)), Country, rotation=0)

# Plot the data
ax.bar(Country, Technology_Research, label='Technology Research', bottom=Engineering_Projects)
ax.bar(Country, Engineering_Projects, label='Engineering Projects')

# Add labels to the data points
for i in range(len(Country)):
    ax.text(x=i-0.2, y=Technology_Research[i]+Engineering_Projects[i]+10, s=Technology_Research[i]+Engineering_Projects[i], size=10, color='black', horizontalalignment='center')

# Add legend
ax.legend(loc='upper left')

# Add title
plt.title('Science and Engineering investments in four countries in 2021')

# Adjust the figure size
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/238.png')

# Clear the current image state
plt.clf()