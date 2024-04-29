
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Import data
data = {"Category": ["Fast Food", "Fine Dining", "Casual Dining", "Cafes", "Food Trucks"],
        "Revenue (in millions)": [6000, 800, 400, 200, 100],
        "Market Share (%)": ["20%", "5%", "10%", "5%", "3%"],
        "Profit Margin (%)": ["15%", "30%", "20%", "25%", "10%"],
        "Employee Count (in thousands)": [500, 50, 200, 100, 25],
        "Sales Growth (%)": ["8%", "5%", "10%", "15%", "20%"],
        "Avg. Price ($)": [5, 50, 15, 8, 10]}

df = pd.DataFrame(data)

# Convert percentage values to float
df["Market Share (%)"] = df["Market Share (%)"].apply(lambda x: float(x.strip("%")) / 100)
df["Profit Margin (%)"] = df["Profit Margin (%)"].apply(lambda x: float(x.strip("%")) / 100)
df["Sales Growth (%)"] = df["Sales Growth (%)"].apply(lambda x: float(x.strip("%")) / 100)

# Set the figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Create heatmap using seaborn
sns.heatmap(df[["Revenue (in millions)", "Market Share (%)", "Profit Margin (%)", "Employee Count (in thousands)", "Sales Growth (%)", "Avg. Price ($)"]],
            annot=True,
            cmap="Blues",
            fmt=".2f",
            cbar=True,
            ax=ax)

# Set ticks and tick labels for x and y axis
ax.set_xticks(np.arange(6) + 0.5)
ax.set_yticks(np.arange(5) + 0.5)
ax.set_xticklabels(["Category", "Revenue", "Market Share", "Profit Margin", "Employee Count", "Sales Growth"], rotation=45, ha="right", rotation_mode="anchor")
ax.set_yticklabels(["Fast Food", "Fine Dining", "Casual Dining", "Cafes", "Food Trucks"])

# Set the title
plt.title("Industry Performance Metrics")

# Automatically resize the image
fig.tight_layout()

# Save the figure
plt.savefig("output/final/heatmap/png/20231228-124154_13.png", bbox_inches="tight")

# Clear the current image state
plt.clf()