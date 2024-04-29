
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot()

# Plot the data
x = np.array([ 2021, 2022, 2023, 2024])
y1 = np.array([25000000, 30000000, 35000000, 40000000])
y2 = np.array([50, 60, 70, 80])

ax.plot(x, y1, label="Number of users")
ax.plot(x, y2, label="Average download speed")

# Set the legend's position
ax.legend(loc='upper left')

# Set the title of the figure
ax.set_title("Increase in Online User Base and Average Download Speeds from 2021-2024")

# Set the x ticks
ax.set_xticks(x)

# Set the y ticks
ax.set_yticks(np.arange(25000000, 40000000, 5000000))

# Set the background grid
ax.grid(color='lightgray', linestyle='-', linewidth=1)

# Set the annotation
for a, b in zip(x, y1):
    plt.annotate('{}'.format(b), xy=(a, b), xytext=(-15, -15), textcoords="offset points")
for a, b in zip(x, y2):
    plt.annotate('{}'.format(b), xy=(a, b), xytext=(-15, 15), textcoords="offset points")

# Set the figure layout
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/140.png')

# Clear the current image state
plt.clf()