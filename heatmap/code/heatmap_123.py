
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {"Category": ["Federal", "State", "Local"], "Education": [35, 25, 40], "Healthcare": [30, 35, 35], "Infrastructure": [20, 15, 20], "Environment": [10, 10, 80], "Defense": [50, 40, 10], "Social Services": [30, 25, 45]}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10,8))
plt.imshow(df.iloc[:,1:], cmap='plasma', interpolation='nearest', aspect='auto')
plt.colorbar()

ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df["Category"])))
ax.set_xticklabels(df.columns[1:])
ax.set_yticklabels(df["Category"])

ax.tick_params(axis='both', which='major', labelsize=12, width=2, length=6)

plt.title("Government and Public Policy Spending by Category", fontsize=16)

plt.tight_layout()

plt.savefig("output/final/heatmap/png/20231228-131639_29.png", bbox_inches='tight')

plt.clf()