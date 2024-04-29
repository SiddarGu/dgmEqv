
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10, 6))

# Define x-axis and y-axis
x = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021])
y = np.array([45, 47, 50, 55, 60, 65, 70])
z = np.array([100, 120, 130, 140, 150, 160, 170])

# Plot data
plt.plot(x, y, label="Voter Participation Rate(%)")
plt.plot(x, z, color="orange", label="Government Spending(billion dollars)")

# Set title
plt.title("Relationship between Voter Participation Rate and Government Spending in the United States from 2015 to 2021")

# Set label
plt.xlabel("Year")

# Set legend
plt.legend(loc="upper left")

# Set xticks
plt.xticks(x)

# Resize the image
plt.tight_layout()

# Save image
plt.savefig("line chart/png/399.png")

# Clear current image state
plt.clf()