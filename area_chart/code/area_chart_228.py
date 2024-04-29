
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define data as a dictionary
data = {"Category": ["Primary School", "Middle School", "High School", "Undergraduate", "Graduate", "Doctorate"],
        "Math": [80, 100, 120, 140, 160, 180],
        "Science": [90, 80, 100, 120, 140, 160],
        "History": [70, 50, 80, 100, 120, 140],
        "English": [100, 90, 110, 130, 150, 170],
        "Art": [50, 60, 70, 60, 70, 80]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data with area chart
ax.stackplot(df["Category"], df["Math"], df["Science"], df["History"], df["English"], df["Art"],
             labels=["Math", "Science", "History", "English", "Art"], colors=["#FF7F0E", "#1F77B4", "#D62728", "#2CA02C", "#9467BD"], alpha=0.7)

# Set background grid lines
ax.grid(color="grey", linestyle="--", linewidth=0.5)

# Set x and y axis ticks and ticklabels with 70% probability
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df["Category"], rotation=45, ha="right", rotation_mode="anchor")
    ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10)
    ax.set_yticks(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set legend
ax.legend(loc="upper left", frameon=False)

# Set title
ax.set_title("Academic Performance in Different Education Levels")

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig("output/final/area_chart/png/20231228-145339_72.png", bbox_inches="tight")

# Clear current image state
plt.clf()