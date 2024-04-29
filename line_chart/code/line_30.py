
import matplotlib.pyplot as plt
import numpy as np

# Create figure
plt.figure(figsize=(9,6))

# Plot the data
ax = plt.subplot()
ax.plot(np.arange(2015, 2021), [1000, 1200, 1400, 1600, 1800, 2000], label="Number of Restaurants")
ax.plot(np.arange(2015, 2021), [20, 22, 23, 26, 28, 30], label="Average Food Cost (USD)")
ax.plot(np.arange(2015, 2021), [10, 12, 13, 15, 16, 18], label="Average Beverage Cost (USD)")
ax.plot(np.arange(2015, 2021), [30, 32, 35, 40, 42, 45], label="Average Meal Cost (USD)")

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Cost (USD)')
ax.set_title("Food and Beverage Industry Trends in the United States from 2015-2020")
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_xticks(np.arange(2015, 2021))
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/318.png')

# Clear the current image state
plt.clf()