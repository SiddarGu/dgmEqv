
import matplotlib.pyplot as plt
import numpy as np

#Create figure
fig = plt.figure(figsize=(10, 10))

# Create data
Energy_Sources = ['Renewable', 'Fossil Fuels', 'Nuclear', 'Other']
Percentage = [45, 40, 10, 5]

# Create a pie chart
plt.pie(Percentage, labels=Energy_Sources, autopct='%.1f%%', startangle=90, shadow=True)

# Add title
plt.title('Renewable and Non-Renewable Energy Sources Distribution in the USA, 2023', fontsize=14, fontweight='bold')

# Set x,y axis ticks
plt.xticks(np.arange(0,110,10), fontsize=10, rotation=0)
plt.yticks([])

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/319.png')

# Clear the current image state
plt.clf()