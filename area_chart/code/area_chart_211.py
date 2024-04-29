
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data dictionary
data = {'Category': ['Legal Aid Services (%)', 'Law Firms (%)', 'Government Agencies (%)', 'Courts (%)', 'Legal Education (%)'],
        '2020': [30, 20, 25, 15, 10],
        '2021': [35, 25, 20, 10, 10],
        '2022': [40, 30, 15, 10, 5],
        '2023': [45, 35, 10, 5, 5]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set up figure and axes
fig, ax = plt.subplots(figsize=(10, 6)) # Use larger figsize to prevent content from being cut off
ax.set_title('Legal Services Distribution by Sector')

# Set up x-axis
ax.set_xticks(np.arange(len(df.index))) # Set ticks at every index
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor') # Rotate labels at 45 degrees and align to the right

# Set up y-axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max() # Calculate max total value
max_total_value = np.ceil(max_total_value / 10) * 10 # Round up to nearest multiple of 10
ax.set_ylim(0, max_total_value) # Set y-axis limit
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) # Set y-axis ticks at random intervals
ax.set_ylabel('Percentage') # Set y-axis label

# Plot area chart
ax.stackplot(df.index, df['2020'], df['2021'], df['2022'], df['2023'], labels=['2020', '2021', '2022', '2023'], colors=['#2b9c85', '#e79e30', '#f05b4a', '#8f57e7'], alpha=0.8) # Set colors and transparency

# Add grid lines
ax.grid(color='#e7e7e7', linestyle='-', linewidth=0.5)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[::-1], labels[::-1], loc='upper right')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-145339_49.png', bbox_inches='tight')

# Clear current image state
plt.clf()