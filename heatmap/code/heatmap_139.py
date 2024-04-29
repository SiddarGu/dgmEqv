
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Define data as a dictionary
data = {"Department": ["Human Resources", "Sales", "Marketing", "Finance", "Engineering", "IT"],
        "Training Costs ($)": [50000, 30000, 25000, 35000, 60000, 55000],
        "Employee Satisfaction (%)": [90, 85, 80, 95, 85, 90],
        "Turnover Rate (%)": [10, 15, 12, 8, 10, 7],
        "Promotion Rate (%)": [5, 8, 9, 4, 6, 5],
        "Diversity Ratio (%)": [65, 60, 55, 70, 75, 80],
        "Productivity Index": [100, 95, 90, 105, 110, 115]}

# Convert data to pandas dataframe
df = pd.DataFrame(data)

# Set figure size
plt.figure(figsize=(10, 8))

# Plot heatmap using seaborn
ax = sns.heatmap(df.iloc[:, 1:], annot=True, cmap="YlGnBu", linewidths=0.5, cbar=False)

# Set ticks and tick labels
ax.set_xticklabels(df.iloc[:, 1:].columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df["Department"], rotation=0)

# Add title and labels
plt.title("HR and Employee Performance Metrics")
plt.xlabel("Metrics")
plt.ylabel("Department")

# Automatically resize image and save as png file
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-131639_52.png", bbox_inches="tight")

# Clear current image state
plt.clf()