
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary with data
data = {'Year': [2019, 2020, 2021, 2022, 2023],
        'Number of Hospitals': [200, 220, 240, 260, 280],
        'Number of Doctors': [1000, 1100, 1200, 1300, 1400],
        'Number of Nurses': [5000, 5500, 6000, 6500, 7000],
        'Number of Patients': [50000, 55000, 60000, 65000, 70000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Define colors and transparency
colors = ['lightblue', 'lightgreen', 'lightcoral', 'pink']
alpha = 0.7

# Plot area chart
ax.stackplot(df['Year'], df['Number of Hospitals'], df['Number of Doctors'],
             df['Number of Nurses'], df['Number of Patients'], colors=colors,
             alpha=alpha, labels=['Number of Hospitals', 'Number of Doctors',
                                  'Number of Nurses', 'Number of Patients'])

# Set x and y axis ticks and ticklabels
if np.random.choice([0, 1], p=[0.3, 0.7]):
    ax.set_xticks(np.arange(len(df['Year'])))
    ax.set_xticklabels(df['Year'], rotation=45, ha='right', rotation_mode='anchor')
    ax.set_xlim(0, len(df['Year']) - 1)
if np.random.choice([0, 1], p=[0.3, 0.7]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value <= 10:
        max_total_value = np.ceil(max_total_value)
    elif max_total_value <= 100:
        max_total_value = np.ceil(max_total_value / 10) * 10
    elif max_total_value <= 1000:
        max_total_value = np.ceil(max_total_value / 100) * 100
    else:
        max_total_value = np.ceil(max_total_value / 1000) * 1000
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_ylim(0, max_total_value)

# Add grid lines
if np.random.choice([0, 1], p=[0.3, 0.7]):
    ax.grid(ls='dashed', lw=0.5, color='gray')

# Set legend and adjust position
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1))

# Set title
ax.set_title('Healthcare and Health Statistics')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-145339_84.png', bbox_inches='tight')

# Clear current image state
plt.clf()