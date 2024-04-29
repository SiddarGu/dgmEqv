

import matplotlib.pyplot as plt
import numpy as np

# Set the figure size
plt.figure(figsize=(10,6))

# Get the data
data = np.array([[2020, 300, 400],
                [2021, 320, 410],
                [2022, 340, 420],
                [2023, 360, 430],
                [2024, 380, 440]])

# Get the x and y values
x = data[:, 0]
y1 = data[:, 1]
y2 = data[:, 2]

# Add a subplot
ax = plt.subplot()

# Plot the line chart
ax.plot(x, y1, label="Organic Food Sales(billion dollars)", color="#f08080")
ax.plot(x, y2, label="GMO Food Sales(billion dollars)", color="#20b2aa")

# Set the title
ax.set_title("Organic and GMO Food Sales in the US from 2020 to 2024")

# Set the x ticks 
ax.set_xticks(x)

# Set the legend
ax.legend(loc="best")

# Set the labels
ax.set_xlabel("Year")
ax.set_ylabel("Sales(billion dollars)")

# Annotate
for i,j in zip(x,y1):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(x,y2):
    ax.annotate(str(j),xy=(i,j))

# Adjust the layout
plt.tight_layout()

# Save the figure
plt.savefig("line chart/png/201.png")

# Clear the current image state
plt.clf()