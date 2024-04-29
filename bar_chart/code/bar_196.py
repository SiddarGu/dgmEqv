

import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(10, 6))

# Set y-axis label
plt.ylabel('Number')

# Set title
plt.title('Healthcare provision in four countries in 2021')

# Define the data
country = np.array(['USA', 'UK', 'Germany', 'France'])
Hospital_beds = np.array([2.8, 2.7, 3.2, 3.4])
Doctors = np.array([2.6, 2.5, 3.1, 3.2])

# Set x-axis
x = np.arange(len(country))

# Set width of each bar
width = 0.35

# Draw the bar chart
ax = plt.bar(x - width/2, Hospital_beds, width, label='Hospital beds/1000 people', color='#FF9900')
ax = plt.bar(x + width/2, Doctors, width, label='Doctors/1000 people', color='#99CCFF')

# Prevent bars from being interpolated
plt.xticks(x, country, rotation=45, wrap=True)

# Add legend
plt.legend()

# Adjust the size of image
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/184.png')

# Clear figure
plt.clf()