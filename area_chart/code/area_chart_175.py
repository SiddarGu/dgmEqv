
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
data = {'2019': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12'],
        'Air Travel (Thousands)': [200, 220, 250, 280, 300, 320, 350, 360, 380, 400, 420, 450],
        'Cruise Travel (Thousands)': [75, 80, 100, 150, 200, 220, 250, 280, 300, 320, 350, 380],
        'Hotel Bookings (Thousands)': [150, 170, 200, 250, 280, 300, 320, 350, 370, 400, 420, 450],
        'Restaurant Reservations (Thousands)': [300, 330, 350, 400, 450, 470, 500, 530, 550, 580, 600, 630]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10, 6))

# Set axis
ax = plt.subplot()

# Set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0])

# Calculate max total value and set y axis ticks and ticklabels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 10000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot the data with the type of area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=df.columns[1:])

# Set grid lines
ax.grid(True, alpha=0.5)

# Set legend position
ax.legend(loc='lower right')

# Set title
plt.title("Tourism and Hospitality Trends in 2019")

# Automatically resize the image
fig.tight_layout()

# Save the chart as a png file
plt.savefig('output/final/area_chart/png/20231228-140159_96.png', bbox_inches='tight')

# Clear current image state
plt.clf()