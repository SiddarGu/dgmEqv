
import matplotlib.pyplot as plt
import numpy as np

# Create figure before plotting, i.e., add_subplot() follows plt.figure()
fig, ax = plt.subplots()

# Plot the data with the type of line chart
time = ["00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00"]
user = [1000000, 1200000, 1400000, 1300000, 1100000, 1200000, 1300000, 1500000]
ax.plot(time, user, color="blue", linestyle="-", marker="o", label="Users")

# Using 'annotate' command to label the value of each data point directly on the figure
for i in range(len(time)):
     ax.annotate(user[i], xy=(time[i], user[i]), xytext=(0,10), textcoords="offset points")

# Drawing techniques such as background grids can be used
ax.grid(color='black', linestyle='--', linewidth=0.3)

# The positioning of the legend should not interfere with the chart and title
ax.legend(loc='upper left', frameon=False)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# You must use xticks to prevent interpolation
plt.xticks(time)

# The title of the figure should be  Increase in social media users in the United States on April 15th, 2021
plt.title("Increase in social media users in the United States on April 15th, 2021")

# The image must be saved as line chart/png/512.png
plt.savefig("line chart/png/512.png")

# Clear the current image state at the end of the code
plt.clf()