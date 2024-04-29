
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import data
data = {"Product Category": ["Snacks", "Beverages", "Frozen Foods", "Dairy Products", "Baked Goods", "Meat and Poultry", "Canned Goods", "Condiments", "Fruits and Vegetables"],
        "Revenue (in millions)": [100, 150, 75, 125, 90, 200, 50, 60, 100],
        "Sales (in millions)": [85, 120, 60, 100, 75, 180, 40, 50, 80],
        "Expenditure (in millions)": [60, 90, 45, 80, 60, 150, 30, 40, 70],
        "Profit (in millions)": [25, 30, 15, 20, 15, 30, 10, 10, 10]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Create heatmap chart
fig, ax = plt.subplots(figsize=(12, 8))
heatmap = ax.imshow(df.iloc[:, 1:], cmap="Blues", interpolation="nearest")
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df["Product Category"])))
ax.set_xticklabels(list(df.columns[1:]))
ax.set_yticklabels(list(df["Product Category"]))
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
plt.setp(ax.get_yticklabels(), rotation=0, ha="center")
for i in range(len(df["Product Category"])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, round(df.iloc[i, j + 1], 1), ha="center", va="center", color="black")
ax.set_title("Financial Performance of Food and Beverage Industry by Product Category")
fig.tight_layout()
fig.colorbar(heatmap)
fig.savefig("output/final/heatmap/png/20231228-163105_20.png", bbox_inches="tight")
plt.close(fig)