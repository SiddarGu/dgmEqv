

import matplotlib.pyplot as plt
import numpy as np

# Creat figure
fig = plt.figure(figsize=(9,5))

# Set up the data
Organization = ['Red Cross','UNICEF','World Vision','World Food Programme']
Donations = [300,400,200,350]
Volunteers = [1400,1200,1000,1300]

# Set up the x-axis
x = np.arange(len(Organization))

# Set up the bar chart
ax1 = fig.add_subplot()
ax1.barh(x, Donations, color='#000000')
ax1.set_yticks(x)
ax1.set_yticklabels(Organization, fontsize=11, wrap=True)

# Set up the second bar chart
ax2 = fig.add_subplot()
ax2.barh(x, Volunteers, color='#000000', left=Donations)
ax2.set_yticks(x)
ax2.set_yticklabels(Organization, fontsize=11, wrap=True)

# Set up the legend
ax1.legend(['Donations (million)'], loc='upper left', fontsize=11)
ax2.legend(['Volunteers'], loc='upper right', fontsize=11)

# Set up the title
plt.title('Donations and volunteers of four charitable organizations in 2021', fontsize=14)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/325.png')

# Clear the current image state
plt.clf()