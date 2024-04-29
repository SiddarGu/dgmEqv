
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data processing
data = {'Region': ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia'],
        'Crop Production (Tonnes)': [500000, 400000, 450000, 600000, 300000, 350000],
        'Livestock Production (Tonnes)': [600000, 550000, 650000, 800000, 400000, 450000],
        'Fishing Production (Tonnes)': [30000, 35000, 25000, 50000, 20000, 30000],
        'Forestry Production (Tonnes)': [40000, 45000, 35000, 60000, 25000, 35000],
        'Poultry Production (Tonnes)': [200000, 180000, 220000, 300000, 150000, 180000],
        'Dairy Production (Litres)': [150000, 120000, 170000, 200000, 100000, 140000]}

df = pd.DataFrame(data)
df = df.set_index('Region')

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
ax = sns.heatmap(df, annot=True, cmap='coolwarm', linewidths=0.5, fmt=',.0f', cbar_kws={'label': 'Production (Tonnes/Litres)'})
ax.tick_params(axis='both', which='both', length=0, labelsize=12)
ax.set_title('Agricultural Production by Region', fontsize=16)
ax.set_ylabel('Region', fontsize=14)
ax.set_xlabel('Production Type', fontsize=14)
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_50.png', bbox_inches='tight')
plt.close(fig)