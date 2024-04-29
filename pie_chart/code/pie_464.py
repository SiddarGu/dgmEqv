
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(5,5))

# Data 
subcategories=['Instant Messaging','Video Streaming','Social Networks', 'Music Streaming', 'Online Gaming']
percentage=[20,30,25,15,10]

# Create Pie Chart
ax = fig.add_subplot()
ax.pie(percentage, labels=subcategories, autopct='%1.1f%%', shadow=True)
ax.axis('equal')

# Title
plt.title('Popular Online Activities Distribution in 2023', fontsize=20, wrap=True)

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/409.png')

# Clear figure
plt.clf()