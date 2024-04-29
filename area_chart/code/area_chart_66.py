
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data
data = {'Category': ['Civil', 'Criminal', 'Employment', 'Intellectual Property', 'Family', 'Corporate', 'Real Estate', 'Personal Injury', 'Environmental', 'Immigration', 'Tax', 'Bankruptcy', 'Constitutional'],
        'Cases Filed': [150, 200, 180, 130, 120, 100, 100, 150, 180, 130, 170, 200, 120],
        'Settlements': [180, 250, 150, 100, 130, 150, 120, 200, 200, 150, 180, 100, 150],
        'Appeals': [200, 100, 200, 150, 110, 180, 150, 100, 150, 200, 200, 150, 100],
        'Lawsuits Won': [100, 180, 130, 180, 150, 200, 180, 120, 100, 180, 100, 180, 200],
        'Lawsuits Lost': [130, 150, 170, 200, 190, 120, 200, 250, 130, 100, 130, 130, 180]}

# Create dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Round max total value up to nearest multiple of 10, 100, or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value/10)*10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value/100)*100
else:
    max_total_value = np.ceil(max_total_value/1000)*1000

# Set y limit and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(True, color='gray', alpha=0.2)

# Set colors and transparency
colors = ['tomato', 'skyblue', 'orange', 'yellowgreen', 'purple']
alpha = 0.7

# Plot area chart
ax.stackplot(df['Category'], df['Cases Filed'], df['Settlements'], df['Appeals'], df['Lawsuits Won'], df['Lawsuits Lost'], colors=colors, alpha=alpha)

# Set legend
ax.legend(['Cases Filed', 'Settlements', 'Appeals', 'Lawsuits Won', 'Lawsuits Lost'], loc='upper left')

# Set x and y labels
ax.set_xlabel('Category')
ax.set_ylabel('Number of Cases')

# Set title
ax.set_title('Legal Cases by Category')

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig('output/final/area_chart/png/20231228-131755_47.png', bbox_inches='tight')

# Clear current image state
plt.clf()