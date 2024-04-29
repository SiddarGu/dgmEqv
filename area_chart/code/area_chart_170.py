
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data dictionary
data_dict = {'Year': [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033],
            'Web Development (Users)': [200, 100, 150, 100, 200, 150, 180, 130, 250, 120, 180, 150, 120, 100, 100],
            'Data Science (Users)': [150, 120, 180, 200, 250, 180, 200, 150, 100, 130, 100, 200, 180, 150, 200],
            'Cybersecurity (Users)': [180, 150, 150, 200, 250, 150, 100, 100, 150, 100, 200, 150, 200, 250, 250],
            'Artificial Intelligence (Users)': [130, 100, 100, 150, 180, 130, 250, 200, 180, 200, 180, 100, 170, 130, 150],
            'Social Media (Users)': [250, 200, 200, 250, 150, 100, 120, 170, 200, 150, 150, 250, 100, 180, 180]}

# Convert dictionary to dataframe
df = pd.DataFrame(data_dict)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set x and y axis ticks and ticklabels
ax.set_xticks(np.arange(len(df.index)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
ax.set_xlim(0, len(df.index) - 1)

# Calculate max total value and set y-axis ticks and ticklabels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Set y-axis labels
yticklabels = [str(i) + "K" for i in yticks]
ax.set_yticklabels(yticklabels)

# Set background grid lines
ax.grid(color='gray', linestyle='dotted', alpha=0.5)

# Plot the data
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.columns[1:], colors=['#ffc107', '#28a745', '#dc3545', '#007bff', '#17a2b8'], alpha=0.7)

# Add legend
ax.legend(loc='upper left')

# Set title
ax.set_title("User Distribution by Technology and the Internet Industry Categories")

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231228-140159_90.png', bbox_inches='tight')

# Clear current image state
plt.clf()