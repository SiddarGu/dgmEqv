
import pandas as pd
import matplotlib.pyplot as plt

data = {"Country": ["France", "Spain", "United States", "China"], "Foreign Visitors (Millions)": [90, 70, 100, 120], "Revenue (Billion USD)": [80, 60, 90, 70], "Hotel Occupancy (%)": [80, 70, 85, 75], "Average Daily Rate (USD)": [150, 130, 170, 120], "Tourism Growth (%)": [7, 6, 8, 9], "Hospitality Growth (%)": [8, 7, 9, 10]}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(df.iloc[:, 1:], cmap='Blues')

# set ticks and tick labels for x and y axis
ax.set_xticks(range(len(df.iloc[0, 1:])))
ax.set_yticks(range(len(df.iloc[:, 0])))
ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df['Country'])

# add colorbar
cbar = plt.colorbar(im)

# add values to heatmap cells
for i in range(len(df.iloc[:, 1:])):
    for j in range(len(df.iloc[:, 1:].columns)):
        text = ax.text(j, i, df.iloc[i, j+1], ha='center', va='center', color='black')

# set title
plt.title("Tourism and Hospitality Statistics by Country")

# resize image and save
plt.tight_layout()
plt.savefig("output/final/heatmap/png/20231228-124154_52.png", bbox_inches='tight')

# clear current image
plt.clf()