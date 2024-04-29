
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create dictionary for data
data = {
    'Year': [2015, 2016, 2017, 2018, 2019],
    'Apartment Sales (000s)': [200, 220, 250, 240, 230],
    'House Sales (000s)': [300, 330, 350, 320, 310],
    'Condo Sales (000s)': [150, 180, 200, 190, 180],
    'Vacant Land Sales (000s)': [100, 120, 140, 130, 120]
}

# convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# plot the data with type of area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df['Year'], df.iloc[:, 1:].values.T, labels=df.iloc[:, 1:].columns)

# set x and y axis ticks and ticklabels
if np.random.uniform() < 0.7:
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')
    ax.set_xlabel('Year')
    
    # calculate max total value and set y limit and ticks
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_ylabel('Sales (000s)')
    
    # randomly set background grid lines
    ax.grid(color='lightgrey', linestyle='--', linewidth=0.5)

    # adjust legend's position
    ax.legend(loc='upper left')

    # automatically resize image and save
    plt.tight_layout()
    plt.savefig('output/final/area_chart/png/20231228-145339_99.png', bbox_inches='tight')
    
    # clear current image state
    plt.close(fig)

# add title to the figure
plt.title('Real Estate Sales by Type from 2015 to 2019')

# show the chart
plt.show()