
import matplotlib.pyplot as plt
import pandas as pd

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

# Read data
data = [[2015, 1.4, 0.4, 0.3],
        [2016, 1.8, 0.6, 0.7],
        [2017, 2.2, 1.2, 1.2],
        [2018, 2.5, 1.7, 2.0],
        [2019, 2.9, 2.2, 2.5],
        [2020, 3.2, 2.7, 3.0]]
df = pd.DataFrame(data, columns=['Year', 'Facebook Users(million)', 'Twitter Users(million)', 'Instagram Users(million)'])

# Plot line chart
ax.plot(df['Year'], df['Facebook Users(million)'], linestyle='-', marker='o', color='r', label='Facebook')
ax.plot(df['Year'], df['Twitter Users(million)'], linestyle='-', marker='o', color='g', label='Twitter')
ax.plot(df['Year'], df['Instagram Users(million)'], linestyle='-', marker='o', color='b', label='Instagram')

# Set xticks
plt.xticks(df['Year'])

# Add title and legend
ax.set_title('Global Social Media User Growth from 2015 to 2020')
ax.legend(loc='best')

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/400.png')

# Clear
plt.clf()