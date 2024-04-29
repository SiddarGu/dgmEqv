
import matplotlib.pyplot as plt
import numpy as np

# Create figure and subplot
fig = plt.figure()
ax = fig.add_subplot()

# Set data
years = np.array(['2020', '2021', '2022', '2023'])
revenue_million = np.array([120, 130, 140, 150])
profit_million = np.array([20, 25, 30, 35])

# Plot data
ax.bar(years, revenue_million, label='Revenue(million)', bottom=profit_million)
ax.bar(years, profit_million, label='Profit(million)')

# Set x-axis
ax.set_xticks(years)

# Set title
ax.set_title('Revenue and Profit of a Business from 2020 to 2023')

# Annotate
for r, p in zip(revenue_million, profit_million):
    ax.annotate('{:.0f}'.format(r + p), xy=(years[np.where((revenue_million + profit_million) == r + p)[0]], r + p + 1))

# Show legend
ax.legend(loc='upper left')

# Resize figure
fig.tight_layout()

# Save figure
plt.savefig("Bar Chart/png/619.png")

# Clear figure
plt.clf()