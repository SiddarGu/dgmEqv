
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Data
Month = ["January","February","March","April"]
ProductionA = [100,120,130,140]
ProductionB = [150,140,160,170]
ProductionC = [100,90,80,90]

# Plot the data
ax.bar(Month,ProductionA, bottom=np.array(ProductionB)+np.array(ProductionC), label='Production A(million)')
ax.bar(Month,ProductionB, bottom=ProductionC, label='Production B(million)')
ax.bar(Month,ProductionC, label='Production C(million)')

# Set xticks
plt.xticks(Month)

# Set legend
ax.legend(loc='upper right')

# Add title
plt.title("Production Output in Three Categories from January to April 2021")

# Fit the figure size
plt.tight_layout()

# Save the figure
plt.savefig('bar chart/png/402.png')

# Clear the figure
plt.clf()