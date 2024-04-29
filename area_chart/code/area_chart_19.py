

# Data
data = {'Year': [2016, 2017, 2018, 2019, 2020],
        'Donations (Millions)': [50, 60, 70, 80, 90],
        'Grants (Millions)': [30, 35, 40, 45, 50],
        'Volunteers (Thousands)': [200, 210, 220, 230, 240],
        'Beneficiaries (Thousands)': [100, 110, 120, 130, 140],
        'Awareness (Percentage)': [60, 65, 70, 75, 80]}

# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Process data using pandas
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create axes
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Calculate max total value for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value/10)*10

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot stacked area chart
ax.stackplot(df['Year'], df['Donations (Millions)'], df['Grants (Millions)'], df['Volunteers (Thousands)'], df['Beneficiaries (Thousands)'], df['Awareness (Percentage)'], labels=['Donations (Millions)', 'Grants (Millions)', 'Volunteers (Thousands)', 'Beneficiaries (Thousands)', 'Awareness (Percentage)'], colors=['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728', '#9467bd'], alpha=0.6)

# Set background grid lines
ax.grid(color='gray', linestyle='dotted', linewidth=1, alpha=0.3)

# Set legend position and labels
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.set_ylabel('Total Contributions')

# Set x and y axis labels
ax.set_xlabel('Year')
ax.set_ylabel('Total Contributions')

# Set title
plt.title('Charitable Contributions and Impact')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231226-103019_3.png', bbox_inches='tight')

# Clear current image state
plt.clf()