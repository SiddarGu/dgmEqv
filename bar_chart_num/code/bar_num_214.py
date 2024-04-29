
import matplotlib.pyplot as plt
import numpy as np

# Create figure and subplot
fig, ax = plt.subplots(figsize=(10,6))

# Define X and Y values
x = np.arange(4)
hotels = [200, 220, 180, 230]
restaurants = [400, 370, 320, 350]
tourists = [450, 500, 400, 470]

# Plot data
ax.bar(x, hotels, label='Hotels')
ax.bar(x, restaurants, bottom=hotels, label='Restaurants')
ax.bar(x, tourists, bottom=[i+j for i,j in zip(hotels, restaurants)], label='Tourists')

# Add Labels
ax.set_title('Number of Hotels, Restaurants and Tourists in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(['USA', 'UK', 'Germany', 'France'])
ax.set_ylabel('Number')

# Display legend
ax.legend()

# Display Values
for i in range(len(x)):
    ax.annotate(hotels[i], (x[i], hotels[i]/2))
    ax.annotate(restaurants[i], (x[i], hotels[i]+restaurants[i]/2))
    ax.annotate(tourists[i], (x[i], hotels[i]+restaurants[i]+tourists[i]/2))

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('Bar Chart/png/551.png')

# Clear figure
plt.clf()