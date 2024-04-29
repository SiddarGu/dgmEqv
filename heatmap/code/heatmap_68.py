

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Technology': ['Solar', 'Wind', 'Hydro', 'Nuclear'],
    '2020 (GW)': [50, 45, 40, 30],
    '2021 (GW)': [55, 50, 45, 35],
    '2022 (GW)': [60, 55, 50, 40],
    '2023 (GW)': [65, 60, 55, 45],
    '2024 (GW)': [70, 65, 60, 50]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 8))

# Set ticks and ticklabels for x and y axis
# ax.set_xticks(range(len(df.columns)))
# ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
# ax.set_yticks(range(len(df['Technology'])))
# ax.set_yticklabels(df['Technology'])

# Plot the heatmap chart
sns.heatmap(df.set_index('Technology'), ax=ax, annot=True, cmap='YlGnBu', cbar=False)

# Set title and labels
ax.set_title('Renewable Energy Capacity by Technology')
# ax.set_xlabel('Year')
# ax.set_ylabel('Technology')

# Automatically resize the image and save
plt.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-124154_58.png', bbox_inches='tight')

# Clear current image state
plt.clf()