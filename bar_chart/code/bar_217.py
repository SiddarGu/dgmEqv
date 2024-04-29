
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

# Plot data
Country = ['USA', 'UK', 'Germany', 'France']
Online_Sales = [2.1, 1.7, 1.9, 1.3]
Offline_Sales = [1.5, 1.2, 1.4, 1.8]
x = np.arange(len(Country))
ax.bar(x-0.2, Online_Sales, width=0.4, label='Online Sales', color='green')
ax.bar(x+0.2, Offline_Sales, width=0.4, label='Offline Sales', color='orange')

# Set x ticks
plt.xticks(x, Country, rotation=45)

# Set title and legend
ax.set_title('Comparison of online and offline sales in four countries in 2021')
ax.legend()

# Resize the figure
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/170.png')

# Clear the figure
plt.clf()