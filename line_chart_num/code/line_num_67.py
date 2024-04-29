
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

# Set data
year = np.array([2001, 2002, 2003, 2004, 2005])
tax_rate = np.array([20, 22, 25, 26, 28])
budget = np.array([2, 2.2, 2.5, 2.6, 2.8])

# Plot chart
ax.plot(year, tax_rate, color='blue', linestyle='dashed', marker='o', label='Tax Rate (%)')
ax.plot(year, budget, color='red', linestyle='dashed', marker='^', label='Budget (trillion dollars)')

# Add title
plt.title('Changes in Tax Rate and Federal Budget from 2001 to 2005')

# Annotate
for x, y in zip(year, tax_rate):
    plt.annotate(y, xy=(x, y), xytext=(-20, 10), textcoords='offset points')

for x, y in zip(year, budget):
    plt.annotate(y, xy=(x, y), xytext=(-20, 10), textcoords='offset points')

# Set xticks
plt.xticks(year, year)

# Set legend
plt.legend(loc='upper left')

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/577.png')

# Clear current state
plt.clf()