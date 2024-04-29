
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {"Industry": ["Technology", "Financial Services", "Consumer Goods", "Healthcare", "Energy"], 
        "Revenue ($ Billions)": [100, 200, 150, 300, 250], 
        "Profits ($ Billions)": [25, 50, 30, 60, 40], 
        "Market Capitalization ($ Billions)": [150, 250, 200, 400, 300], 
        "Debt to Equity Ratio": [2.5, 1.5, 2, 1, 1.5], 
        "Return on Equity (%)": [10, 15, 12.5, 20, 18], 
        "Earnings per Share": [5, 10, 8, 12, 10]
        }

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Set the index to the Industry column
df.set_index('Industry', inplace=True)

# Create a heatmap using seaborn
fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(df, cmap='Blues', annot=True, linewidths=.5, cbar=False)

# Set the x and y ticks and labels in the center of each row and column
ax.set_xticks(np.arange(len(df.columns))+0.5)
ax.set_yticks(np.arange(len(df.index))+0.5)

ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='right', rotation_mode='anchor')

# Set the title and resize the image
plt.title('Key Metrics for Top Industries')
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_76.png', bbox_inches='tight')

# Clear the current image state
plt.clf()