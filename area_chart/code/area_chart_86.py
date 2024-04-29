
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data dictionary
data = {'Category': ['Litigation (Cases)', 'Contracts (Cases)', 'Intellectual Property (Cases)', 'Criminal (Cases)', 'Employment (Cases)', 'Real Estate (Cases)', 'Immigration (Cases)', 'Family (Cases)'],
        'Law Firm A': [100, 80, 50, 30, 60, 40, 20, 10],
        'Law Firm B': [80, 50, 40, 25, 70, 20, 15, 5],
        'Law Firm C': [60, 40, 30, 20, 50, 10, 5, 5],
        'Law Firm D': [50, 30, 20, 10, 40, 10, 5, 0]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 6))

# Plot the chart using ax.stackplot method
ax = plt.subplot(111)
ax.stackplot(df['Category'], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=['#4e79a7', '#f28e2c', '#e15759', '#76b7b2'], alpha=0.7)

# Set x-axis and y-axis labels
ax.set_xlabel('Case Type')
ax.set_ylabel('Number of Lawsuits')

# Set title
plt.title('Lawsuits by Law Firm and Case Type')

# Set ticks and ticklabels
if np.random.rand() < 0.7:
    ax.set_xticks(np.arange(len(df['Category'])))
    ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
    ax.set_xlim(0, len(df['Category']) - 1)
if np.random.rand() < 0.7:
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 100) * 100
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(linestyle='--', linewidth=0.5, alpha=0.5)

# Set legend and adjust its position
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('output/final/area_chart/png/20231228-131755_7.png', bbox_inches='tight')

# Clear the current image state
plt.clf()