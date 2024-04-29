
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {'Product':['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G', 'Product H', 'Product I', 'Product J'],
        'Revenue ($ Million)':[500, 400, 600, 300, 800, 200, 700, 900, 1000, 150],
        'Cost of Goods Sold ($ Million)':[300, 250, 400, 200, 500, 150, 450, 600, 700, 100],
        'Gross Margin (%)':[40, 38, 33, 33, 38, 25, 36, 33, 30, 33],
        'Operating Expenses ($ Million)':[100, 90, 120, 60, 150, 50, 120, 140, 180, 30],
        'Net Income ($ Million)':[100, 70, 80, 40, 150, 50, 130, 160, 200, 20]}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10,8))

sns.heatmap(df.iloc[:,1:], annot=True, fmt='g', cmap='coolwarm', center=0, cbar=False, ax=ax)

ax.set_xticks(np.arange(5)+0.5)
ax.set_yticks(np.arange(10)+0.5)

ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Product'], rotation=0, va='center', wrap=True)

ax.set_xlabel('Financial Performance')
ax.set_ylabel('Product')

plt.title('Financial Performance by Product in Manufacturing')

plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-155147_57.png', bbox_inches='tight')

plt.clf()