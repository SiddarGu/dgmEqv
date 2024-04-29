

import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(14,8))
ax = fig.add_subplot(111)

# Define data
Country = ('USA','UK','Germany','France')
Traditional_Food_Dishes = [150,100,130,120]
Cuisine_Restaurants = [200,170,180,160]

# Plot bar chart
ax.bar(Country, Traditional_Food_Dishes, color='#a1d2e6', label='Traditional Food Dishes')
ax.bar(Country, Cuisine_Restaurants, bottom=Traditional_Food_Dishes, color='#f5b7b1', label='Cuisine Restaurants')

# Set labels and title
ax.set_ylabel('Number of Restaurants')
ax.set_title('Number of Traditional Food Dishes and Cuisine Restaurants in Four Countries in 2021')
ax.set_xticklabels(Country, rotation=45, ha='right')
ax.grid(axis='y')
ax.legend(loc='upper right')

# Resize the image 
plt.tight_layout()

# Save the image
plt.savefig('bar chart/png/143.png')

# Clear the current image state 
plt.clf()