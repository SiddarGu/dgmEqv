
import matplotlib.pyplot as plt
import numpy as np

# Create figure before plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# Plot the data with the type of bar chart
Country = ['USA', 'UK', 'Germany', 'France']
Restaurants = [20, 15, 18, 17]
Cafes = [30, 25, 32, 27]
Takeaways = [10, 12, 14, 13]

# Set the bottom parameter in the bar command
x = np.arange(len(Country))
width = 0.2

rects1 = ax.bar(x-width, Restaurants, width, label='Restaurants')
rects2 = ax.bar(x, Cafes, width, label='Cafes')
rects3 = ax.bar(x+width, Takeaways, width, label='Takeaways')

# xticks to prevent interpolation
ax.set_xticks(x)
ax.set_xticklabels(Country, rotation=45, wrap=True)

# Set the title of the figure
plt.title('Number of restaurants, cafes and takeaways in four countries in 2021')

# Set the legend location without interfering the chart
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image as bar chart/png/410.png
plt.savefig('bar chart/png/410.png')

# Clear the current image state at the end of the code
plt.clf()