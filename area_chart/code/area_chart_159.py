


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Represent data using a dictionary
data_dict = {"Category": ["Social Media", "Web"], "Facebook (Users)": [200, 100], "Twitter (Users)": [150, 120], "Instagram (Users)": [180, 150], "LinkedIn (Users)": [130, 100], "YouTube (Users)": [250, 200]}

# Process data using pandas
df = pd.DataFrame(data_dict)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with an area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], labels=["Facebook", "Twitter", "Instagram", "LinkedIn", "YouTube"], colors=["#3b5998", "#1da1f2", "#e1306c", "#0077b5", "#c4302b"], alpha=0.8)

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10)
ax.set_xticks(np.arange(0, len(df.index)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticks(np.linspace(0, df.iloc[:, 1:].sum(axis=1).max(), np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
ax.grid(color="#cccccc", linestyle="--")

# Set legend
ax.legend(loc="upper left")

# Set title
ax.set_title("Social Media and Web Usage by Platform")

# Automatically resize image
plt.tight_layout()

# Save the image
plt.savefig("output/final/area_chart/png/20231228-140159_8.png", bbox_inches="tight")

# Clear current image state
plt.clf()