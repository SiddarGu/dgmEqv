
import matplotlib.pyplot as plt
import numpy as np

# Create figure 
fig = plt.figure(figsize=(8, 5))
ax = fig.add_subplot()

# Data
labels = ['Corporate Tax','Personal Income Tax','Sales Tax','Property Tax','Other']
sizes = [35,25,20,10,10]

# Pie chart
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

# Title
plt.title('Distribution of Government Revenue Sources in the USA, 2023')

# Tight layout prevent the text from overlapping
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/519.png')

# Clear the figure
plt.clf()