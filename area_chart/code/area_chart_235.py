
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Convert data into dictionary
data = {"Department": ["Marketing", "Finance", "Education", "Healthcare", "Science", "Business", "Government", "E-commerce", "Gaming", "Mobile", "Retail", "Telecommunications", "Automotive"],
        "Administration (%)": [15, 10, 20, 10, 25, 20, 10, 25, 20, 15, 20, 25, 15],
        "Sales (%)": [20, 20, 30, 15, 20, 15, 15, 10, 10, 25, 25, 15, 30],
        "IT (%)": [10, 25, 25, 25, 10, 10, 20, 15, 30, 20, 15, 20, 25],
        "HR (%)": [15, 15, 10, 30, 30, 25, 25, 20, 25, 10, 30, 30, 10],
        "R&D (%)": [25, 30, 15, 20, 15, 30, 30, 30, 15, 30, 10, 10, 20]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot stacked area chart
ax.stackplot(df.index, df.iloc[:, 1:].T, labels=df.iloc[:, 0], colors=['#C7B2D5', '#7FBF7B', '#E9A3C9', '#FDB462', '#80B1D3'], alpha=0.7)

# Set x-axis ticks and ticklabels
ax.set_xticks(df.index)
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# Set y-axis ticks and ticklabels
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value)
if max_total_value < 10:
    yticks = np.linspace(0, max_total_value, 3, dtype=np.int32)
elif max_total_value < 100:
    yticks = np.linspace(0, max_total_value, 5, dtype=np.int32)
elif max_total_value < 1000:
    yticks = np.linspace(0, max_total_value, 7, dtype=np.int32)
else:
    yticks = np.linspace(0, max_total_value, 9, dtype=np.int32)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks)

# Set background grid lines
ax.grid(linestyle='dashed', color='gray', alpha=0.3)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Set title
plt.title("Employee Distribution by Department")

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig("output/final/area_chart/png/20231228-145339_80.png", bbox_inches='tight')

# Clear current image state
plt.clf()