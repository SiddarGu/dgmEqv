
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data processing
data = {"Country":["United States", "China", "Japan", "Germany", "United Kingdom"], "Stock Market (Billion USD)":[30, 20, 10, 15, 12], "GDP Growth (%)":[2.5, 6.5, 1.5, 2.2, 1.8], "Unemployment Rate (%)":[4.2, 3.8, 3.2, 3.5, 4.0], "Inflation Rate (%)":[2.3, 2.0, 1.7, 1.8, 2.2], "Interest Rate (%)":[1.5, 2.0, 0.5, 1.0, 0.8], "Debt to GDP Ratio (%)":[85, 65, 250, 70, 90]}

df = pd.DataFrame(data)
df = df.set_index("Country")

# Plotting the chart
fig, ax = plt.subplots(figsize=(10, 6))
heatmap = sns.heatmap(df, cmap="Blues", annot=True, fmt=".1f", linewidths=0.5, ax=ax)

# Setting the ticks and tick labels
ax.set_xticks(np.arange(len(df.columns)) + 0.5)
ax.set_yticks(np.arange(len(df.index)) + 0.5)
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.index)

# Centering the ticks
plt.setp(ax.get_xticklabels(), ha="right", rotation=45, rotation_mode="anchor")
plt.setp(ax.get_yticklabels(), ha="right", rotation=45)

# Adding labels and title
plt.xlabel("Economic Indicators")
plt.title("Economic Indicators by Country")

# Resizing and saving the figure
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-155147_54.png", bbox_inches="tight")

# Clearing the current image state
plt.clf()