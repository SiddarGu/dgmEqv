
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data Processing
data = {"Sector": ["Technology", "Healthcare", "Financial Services", "Consumer Goods", "Energy"],
        "Stock Index Value": [500, 300, 400, 200, 100],
        "Revenue (Millions)": [50000, 35000, 40000, 30000, 20000],
        "Profit (Millions)": [10000, 8000, 9000, 7000, 5000],
        "Debt (Millions)": [25000, 20000, 30000, 15000, 10000],
        "Cash (Millions)": [50000, 40000, 45000, 35000, 20000]}

df = pd.DataFrame(data)
df = df.set_index("Sector")

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Using pcolor() to plot the heatmap
heatmap = ax.pcolor(df, cmap="coolwarm")

# Setting ticks and ticklabels
ax.set_xticks(np.arange(df.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(df.shape[0]) + 0.5, minor=False)
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df.index)

# Setting ticks and ticklabels in the center of rows and columns
ax.tick_params(axis="both", which="major", labelsize=12, pad=10)
ax.set_xticks(np.arange(df.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(df.shape[0]) + 0.5, minor=False)
ax.set_xticklabels(df.columns, rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(df.index, rotation=0)

# Adding colorbar
plt.colorbar(heatmap)

# Automatically resize the image
plt.tight_layout()

# Saving the figure
plt.savefig("output/final/heatmap/png/20231228-163105_14.png", bbox_inches="tight")

# Setting the title
ax.set_title("Company Performance in Different Sectors", fontsize=16)

# Clearing the current image state
plt.clf()