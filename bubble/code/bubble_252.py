import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd
from matplotlib.colors import Normalize
from matplotlib.cm import get_cmap

df = pd.DataFrame({
    'Company': ['Microsoft', 'Apple', 'Amazon', 'Google', 'Facebook', 'IBM', 'Oracle', 'SAP', 'Salesforce'],
    'Revenue (Billion $)': [143, 260, 280, 162, 70, 77, 39, 27, 17],
    'Market Share (%)': [48, 37, 13, 12, 9, 8, 6, 4, 2],
    'Employment (Thousands)': [144, 137, 798, 114, 44, 352, 135, 93, 49],
    'Corporate Social Responsibility Score': [8, 7, 6, 9, 6, 9, 7, 8, 8]
})

fig, ax = plt.subplots(figsize=(12, 8))

# Normalizing values
norm = Normalize(df['Corporate Social Responsibility Score'].min(), df['Corporate Social Responsibility Score'].max())
cmap = get_cmap()
df['color'] = df['Corporate Social Responsibility Score'].map(lambda x: cmap(norm(x)))
df['size'] = Normalize(df['Employment (Thousands)'].min(),
                       df['Employment (Thousands)'].max())(df['Employment (Thousands)']) * 4500 + 600

# Plotting
sc = ax.scatter(df['Revenue (Billion $)'],
                df['Market Share (%)'],
                c=df['color'],
                s=df['size'],
                alpha=0.6,
                edgecolors='w')

# Scatter empty points for legend
for i, line in enumerate(df.itertuples()):
    ax.scatter([], [], color=line.color, label=line.Company + f' {df["Employment (Thousands)"][i]}')

plt.legend(title='Employment (Thousands)')
plt.title("Comparison of Major Tech Companies in Terms of Revenue, Market Share, and Employment")

ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y/100)))
ax.set_xlabel('Revenue (Billion $)')
ax.set_ylabel('Market Share (%)')

plt.grid(True, which='both', linestyle='-', linewidth=0.3)

# Adding a color bar
cbar = plt.colorbar(sc)
cbar.set_label('Corporate Social Responsibility Score')

plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/51_202312301731.png')
plt.cla()
