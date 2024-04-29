import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data_labels = ["Daily Internet Usage (Hours)", "Number of Users (Millions)"]
line_labels = [
    "0-1", "1-2", "2-3", "3-4", "4-5", "5-6", "6-7", "7-8", "8-9", "9-10"
]
data = [
    45, 60, 75, 50, 30, 20, 12, 8, 5, 3
]

# Create a DataFrame
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Plot configuration
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)
ax.bar(df["Daily Internet Usage (Hours)"], df["Number of Users (Millions)"], color='skyblue')

# Aesthetics
ax.set_title('Patterns of Daily Internet Usage among Internet Users', fontsize=14, fontweight='bold')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.set_xticklabels(df["Daily Internet Usage (Hours)"], rotation=45, ha="right")
plt.grid(True, linestyle='--', alpha=0.7)

# Resize and save the plot
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/103.png')

# Clear the current figure's state
plt.clf()
