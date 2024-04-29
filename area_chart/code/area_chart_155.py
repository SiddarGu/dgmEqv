
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary
data = {'Category': ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'France', 'Germany', 'Spain', 'Italy', 'Japan', 'China', 'India', 'Australia'],
        'Soccer (Audience)': [50000, 25000, 30000, 40000, 30000, 40000, 45000, 35000, 30000, 20000, 35000, 30000, 20000],
        'Basketball (Audience)': [35000, 30000, 25000, 30000, 20000, 30000, 35000, 25000, 20000, 15000, 30000, 20000, 15000],
        'Football (Audience)': [30000, 20000, 35000, 20000, 10000, 25000, 20000, 30000, 35000, 25000, 20000, 15000, 10000],
        'Baseball (Audience)': [25000, 15000, 20000, 10000, 15000, 20000, 15000, 20000, 25000, 20000, 15000, 10000, 15000]
        }

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set x-axis and y-axis labels
ax.set_xlabel("Country")
ax.set_ylabel("Number of Audience")

# Set title
ax.set_title("Audience Distribution by Country and Sport")

# Set background grid lines
ax.grid(axis='y', linestyle='--')

# Set x-axis range
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and round up to nearest multiple of 1000
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y-axis range and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot area chart
ax.stackplot(df['Category'], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns)

# Set legend
ax.legend(loc='upper left')

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_73.png', bbox_inches='tight')

# Clear current image state
plt.clf()