
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Represent data using dictionary
data = {'Month':['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'Energy Consumption (kWh)':[1000, 1100, 1050, 900, 800, 950, 1000, 1050, 1100, 1000, 950, 900],
        'Water Usage (gal)':[2000, 2200, 2300, 2100, 2400, 2100, 2000, 1900, 1800, 2000, 2300, 2400],
        'Waste Production (lbs)':[500, 450, 475, 400, 425, 425, 450, 475, 500, 500, 450, 425]}

# Process data
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df.index, df.iloc[:, 1:].T, labels=df.iloc[:, 1:].columns, colors=['#2ca02c', '#1f77b4', '#d62728'], alpha=0.7)
ax.grid(linestyle='--', alpha=0.3)

# Set ticks and tick labels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(0, len(df.index), 2))
    ax.set_xticklabels(df['Month'][::2].tolist(), rotation=45, ha='right', rotation_mode='anchor')
    ax.set_xlim(0, len(df.index) - 1)
if np.random.choice([True, False], p=[0.7, 0.3]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 1000) * 1000
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_yticklabels(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_ylim(0, max_total_value)

# Set legend and labels
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax.set_xlabel('Month')
ax.set_ylabel('Energy Consumption (kWh), Water Usage (gal), Waste Production (lbs)')
ax.set_title('Energy and Resource Usage in 2020')

# Automatically resize image and save
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231226-103019_12.png', bbox_inches='tight')

# Clear current image state
plt.clf()