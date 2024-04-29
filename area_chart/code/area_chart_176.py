
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
data = {"Category": ["Social Media", "E-learning", "Cloud Computing", "Online Gaming", "AI/ML", "Digital Marketing", "Mobile Apps", "E-commerce", "Streaming Services", "Cybersecurity", "Virtual Reality", "IoT", "Big Data"],
        "Application Downloads (Millions)": [100, 50, 80, 60, 40, 70, 90, 120, 200, 30, 20, 50, 40],
        "Number of Websites": [500, 250, 300, 200, 100, 400, 600, 800, 1000, 80, 50, 150, 100],
        "Internet Users (Millions)": [1000, 500, 800, 400, 200, 600, 1200, 1600, 1800, 150, 100, 300, 200],
        "E-commerce Revenue (Billions)": [200, 100, 150, 80, 50, 120, 250, 300, 500, 40, 30, 70, 50],
        "Data Usage (Petabytes)": [500, 200, 300, 150, 100, 250, 400, 500, 700, 100, 80, 150, 100]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Ceil max total value up to the nearest multiple of 10, 100 or 1000
if max_total_value // 1000 > 0:
    max_total_value = int(max_total_value // 1000) * 1000 + 1000
elif max_total_value // 100 > 0:
    max_total_value = int(max_total_value // 100) * 100 + 100
else:
    max_total_value = int(max_total_value // 10) * 10 + 10

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Set background grid lines
ax.grid(True, color='lightgrey', linestyle='--', linewidth=0.5)

# Plot data as area chart
ax.stackplot(df.index, df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=["#F2A947", "#F29147", "#F26C47", "#F24769", "#F247E6", "#B347F2"], alpha=0.8)

# Set x and y axis ticks and ticklabels
if np.random.uniform(0, 1) < 0.7:
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
    ax.set_xlim(0, len(df.index) - 1)
if np.random.uniform(0, 1) < 0.7:
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_ylim(0, max_total_value)

# Set legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Set title
ax.set_title("Technology and the Internet Statistics")

# Automatically resize the image
fig.tight_layout()

# Save image
fig.savefig("output/final/area_chart/png/20231228-140159_97.png", bbox_inches='tight')

# Clear current image state
plt.clf()