
import matplotlib.pyplot as plt
import numpy as np

#Data 
Region=['North America','Europe','Asia','South America']
Bar_1=[400,500,550,450]
Bar_2=[650,800,900,700]

# Create figure and axes
fig, ax = plt.subplots(figsize=(8,5))

# Plot Bar Chart
ax.bar(Region,Bar_1, color='#073642', label='STEM Graduates')
ax.bar(Region,Bar_2, bottom=Bar_1, color='#b58900', label='STEM Vacancies')

# Add Labels
for i in ax.patches:
    ax.annotate(format(i.get_height()), (i.get_x() + 0.2, i.get_height() + 10))

# Add Legend
ax.legend(loc='upper right', bbox_to_anchor=(1,1))

# Set Title
plt.title('STEM graduates and vacancies in four regions in 2021', fontsize=15)

# Resize the figure
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/448.png')

# Clear the current image state
plt.clf()