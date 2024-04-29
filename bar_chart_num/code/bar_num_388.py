
import matplotlib.pyplot as plt 
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()

# Define data
country = ['USA', 'UK', 'Germany', 'France']
hotels = [120, 180, 140, 150]
restaurants = [250, 300, 280, 290]
tourist_attractions = [400, 500, 450, 470]

# Create bar chart
x = np.arange(len(country))
ax.bar(x - 0.2, hotels, width = 0.2, label='Hotels', color = '#fcc321')
ax.bar(x, restaurants, width = 0.2, label='Restaurants', color = '#1ebcd3')
ax.bar(x + 0.2, tourist_attractions, width = 0.2, label='Tourist Attractions', color = '#f36c21')

# Set title and labels
plt.title("Number of hotels, restaurants and tourist attractions in four countries in 2021")
plt.xlabel("Country")
plt.ylabel("Number of Hotels, Restaurants and Tourist Attractions")

# Annotate the labels on the chart
for i, v in enumerate(hotels):
    ax.text(i - 0.2, v + 5, str(v), color='black', fontweight='bold')
for i, v in enumerate(restaurants):
    ax.text(i, v + 5, str(v), color='black', fontweight='bold')
for i, v in enumerate(tourist_attractions):
    ax.text(i + 0.2, v + 5, str(v), color='black', fontweight='bold')

# Set xticks
plt.xticks(x, country)

# Add legend
ax.legend()

# Resize the figure
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/456.png')

# Clear the current image state
plt.clf()