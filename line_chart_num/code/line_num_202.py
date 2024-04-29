
import matplotlib.pyplot as plt
import numpy as np

# Create figure before plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot the data
age = ['18-25','26-35','36-45','46-55','56-65','66-75']
health = [50,60,70,75,85,95]
satisfaction = [75,80,85,90,95,100]

ax.plot(age, health, color='b', label='Health Index', marker='o')
ax.plot(age, satisfaction, color='r', label='Satisfaction Index', marker='o')

# Label the value of each data point directly on the figure
for x, y in zip(age, health):
    ax.annotate(y, xy=(x, y), xytext=(-2,2), textcoords='offset points', fontsize=12)
for x, y in zip(age, satisfaction):
    ax.annotate(y, xy=(x, y), xytext=(-2,2), textcoords='offset points', fontsize=12)

# Add legend and title
ax.legend(loc='best')
plt.title("Health and Satisfaction Index of Different Age Groups in 2021")

# Prevent interpolation
plt.xticks(age)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig("line chart/png/447.png")

# Clear the current image state
plt.clf()