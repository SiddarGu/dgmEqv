import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Data
data_labels = ['Asset Class', 'Average ROI (%)']
line_labels = ['Stocks', 'Bonds', 'Real Estate', 'Commodities', 'Private Equity', 'Hedge Funds', 'Cash']
data = [8.12, 5.75, 7.85, 3.90, 14.20, 6.55, 1.30]

# Combine data into a DataFrame
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Initialize figure and axis
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create a seaborn histogram
sns.barplot(x='Asset Class', y='Average ROI (%)', data=df, ax=ax)

# Set the title
ax.set_title('Average Return on Investment (ROI) by Asset Class in 2023')

# Improve label visibility
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", wrap=True)

# Add grid
ax.yaxis.grid(True)

# Tighten layout and save the image
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/2.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure state
plt.clf()
