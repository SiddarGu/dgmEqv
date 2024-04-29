
import matplotlib.pyplot as plt
import numpy as np

# Prepare data
Region = ['North America', 'South America', 'Europe', 'Asia']
Donations = [100,80,90,70]
Volunteers = [20000,12000,25000,15000]

# Set figure size
plt.figure(figsize=(9,6))

# Plot data
ax=plt.subplot()
ax.bar(Region, Donations, color='b', label='Donations(million)', width=0.45)
ax.bar(Region, Volunteers, color='g', label='Volunteers', width=0.45,bottom=Donations)

# Set font
plt.rcParams['font.sans-serif']=['SimHei']

# Set labels
for x,y in zip(Region,Donations):
    ax.annotate('{}'.format(y),xy=(x,y+0.5),ha='center')
for x,y in zip(Region,Volunteers):
    ax.annotate('{}'.format(y),xy=(x,y+0.5),ha='center')

# Set title
plt.title('Financial donations and volunteers in four regions in 2021', fontsize=20)

# Set legend
ax.legend()

# Set xticks
ax.set_xticks(Region)

# Resize the image
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/29.png')

# Clear the current image state
plt.clf()