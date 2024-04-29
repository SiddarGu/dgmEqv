
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize = (18, 8))

# Data
Country = ["USA", "UK", "Germany", "France"]
Government_Spending = [800, 300, 450, 700]
Population = [3500, 1000, 2000, 1500]

# Plot bar chart
ax = fig.add_subplot()
x = np.arange(len(Country))
width = 0.2
ax.bar(x - width/2, Government_Spending, width, label="Government Spending(billion)")
ax.bar(x + width/2, Population, width, label="Population")

# Labels
ax.set_xticks(x)
ax.set_xticklabels(Country, rotation=45, ha="right", wrap=True)
ax.set_title("Government Spending and Population in four countries of 2021")
ax.legend()

# Adjust Figure
fig.tight_layout()

# Save Figure
fig.savefig('bar chart/png/259.png')

# Clear figure
plt.clf()