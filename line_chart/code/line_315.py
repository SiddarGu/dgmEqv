

import matplotlib.pyplot as plt
import pandas as pd

# Create figure before plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

# Read data
data = [[2018, 320000, 150000],
        [2019, 400000, 200000],
        [2020, 450000, 250000],
        [2021, 500000, 300000]]
df = pd.DataFrame(data, columns=['Year', 'Number of Domestic Visitors', 'Number of International Visitors'])

# Plot the data with the type of line chart
ax.plot(df['Year'], df['Number of Domestic Visitors'], color="blue", label="Number of Domestic Visitors")
ax.plot(df['Year'], df['Number of International Visitors'], color="red", label="Number of International Visitors")

# Set title
ax.set_title("Growth of Tourist Visits to London From 2018 to 2021", fontsize=16)

# Set x ticks
ax.set_xticks(df['Year'])

# Set legend
ax.legend(loc="best")

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save image
plt.savefig("line chart/png/219.png")

# Clear the current image state
plt.clf()