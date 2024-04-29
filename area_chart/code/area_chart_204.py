
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'Year': [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], 
        'Government Spending ($)': [5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000], 
        'Public Programs ($)': [4000, 4300, 4500, 4800, 5000, 5200, 5500, 5700, 6000], 
        'Policy Implementation ($)': [3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000], 
        'Regulatory Enforcement ($)': [2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600], 
        'Public Services ($)': [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set x and y ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 1000) * 1000

    # Set yticks
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

    # Set yticklabels
    ax.set_yticklabels([str(x) for x in ax.get_yticks()])

# Plot area chart
ax.stackplot(df['Year'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=['#FF7F0E', '#1F77B4', '#2CA02C', '#D62728', '#9467BD'], alpha=0.8)

# Set background grid lines
ax.grid(axis='y', alpha=0.2)

# Set legend
ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1))

# Set title
ax.set_title('Government Spending and Public Services Allocation')

# Automatically resize figure
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-145339_39.png', bbox_inches='tight')

# Clear figure
plt.close(fig)