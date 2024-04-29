
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Convert data to dictionary
data = {'2020': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'Electricity Usage (kWh)': [2500, 2400, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500],
        'Gas Usage (m3)': [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220],
        'Water Usage (m3)': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Set x and y ticks and ticklabels
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0])
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10

# Set y ticks and ticklabels
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_yticklabels([str(x) for x in ax.get_yticks()])

# Create background grid lines
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.5)

# Set colors and transparency
colors = ['#E69F00', '#56B4E9', '#009E73']
alpha = 0.7

# Plot area chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], labels=df.columns[1:], colors=colors, alpha=alpha)

# Set legend position
ax.legend(loc='upper left')

# Set title
ax.set_title('Monthly Energy and Utilities Usage for 2020')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_89.png', bbox_inches='tight')

# Clear current image state
plt.clf()