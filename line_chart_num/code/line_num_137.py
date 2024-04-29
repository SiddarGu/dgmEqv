
import matplotlib.pyplot as plt
import numpy as np

year = [2001, 2002, 2003, 2004, 2005]
Consumption = [200, 300, 350, 380, 400]
Price = [10, 15, 20, 25, 30]

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(year, Consumption, marker='o', color='red', label='Consumption')
ax.plot(year, Price, marker='o', color='blue', label='Price')

# Annotate the points
for x, y, label in zip(year, Consumption, Consumption):
    ax.annotate(label, xy=(x, y), xytext=(-5, 5), textcoords='offset points')

for x, y, label in zip(year, Price, Price):
    ax.annotate(label, xy=(x, y), xytext=(-5, 5), textcoords='offset points')

# Add Axes labels and Title
ax.set_xlabel('Year')
ax.set_ylabel('Consumption/Price')
ax.set_title('Annual Consumption and Price of Rice in the USA from 2001 to 2005')

# Create the legend
ax.legend(loc='best', fontsize='small')

# Set the ticks
ax.set_xticks(year)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/160.png')

# Clear the current image state
plt.clf()