
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(8,8))

# Get data
genres = ['Pop Music','Rock Music','R&B Music','Country Music','Jazz Music','Classical Music','Blues Music']
percentage = [35,20,15,10,10,5,5]

# Plot pie chart
plt.pie(percentage, labels=genres, autopct='%1.1f%%', textprops={'wrap': True, 'rotation': 45})

# Set title
plt.title('Popular Music Genre Distribution in the USA, 2023')

# Adjust the size and spacing of the chart
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/49.png')

# Clear the figure
plt.clf()