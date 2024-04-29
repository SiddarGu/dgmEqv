
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Represent the data using a dictionary
data = {'Year': ['2017','2018','2019','2020','2021'], 'Legal Cases Filed': [100,120,150,180,200], 'Legal Cases Disposed': [80,90,100,120,150], 'Arbitration Cases Filed': [60,70,80,90,100], 'Arbitration Cases Disposed': [50,60,70,80,90]}

# Use pandas "df = pd.DataFrame(data)" to process the data
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with the type of area chart
fig, ax = plt.subplots(figsize=(12,8))
ax.stackplot(df['Year'], df['Legal Cases Filed'], df['Legal Cases Disposed'], df['Arbitration Cases Filed'], df['Arbitration Cases Disposed'], labels=['Legal Cases Filed', 'Legal Cases Disposed', 'Arbitration Cases Filed', 'Arbitration Cases Disposed'], colors=['skyblue', 'lightgreen', 'yellow', 'orange'], alpha=0.8)

# Set title
plt.title('Legal Cases and Arbitration Trends from 2017 to 2021.')

# Set x and y axis labels
plt.xlabel('Year')
plt.ylabel('Number of Cases')

# Set x and y axis ticks and ticklabels
if np.random.choice([0,1], p=[0.3,0.7]) == 1:
    ax.set_xticks(np.arange(0, len(df.index), 1))
    if len(df.iloc[:, 0].values[0]) > 6:
        plt.xticks(rotation=45, ha='right', rotation_mode='anchor', wrap=True)
else:
    ax.set_xticklabels([])
if np.random.choice([0,1], p=[0.3,0.7]) == 1:
    ax.set_xlim(0, len(df.index) - 1)
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_ylim(0, max_total_value)
    if len(str(max_total_value)) > 2:
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])
else:
    ax.set_yticklabels([])
    
# Set legend
plt.legend(loc='upper left')

# Set background grid lines
plt.grid(axis='y', color='#D3D3D3', linestyle='-', linewidth=0.5, alpha=0.5)

# Automatically resize the image
plt.tight_layout()

# Save the chart as a png file
plt.savefig('output/final/area_chart/png/20231228-131755_11.png', bbox_inches='tight')

# Clear the current image state
plt.clf()