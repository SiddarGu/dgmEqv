
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data as dictionary
data = {'Category': ['Dance', 'Music', 'Theatre', 'Museums', 'Art Galleries'],
        'January': [50, 80, 60, 40, 30],
        'February': [60, 90, 70, 50, 40],
        'March': [70, 100, 80, 60, 50],
        'April': [80, 110, 90, 70, 60],
        'May': [90, 120, 100, 80, 70]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(12, 8))

# Calculate max total value and ceil it up to the nearest multiple of 10, 100 or 1000
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value <= 10:
    max_total_value = 10
elif max_total_value <= 100:
    max_total_value = int(np.ceil(max_total_value / 10.0)) * 10
elif max_total_value <= 1000:
    max_total_value = int(np.ceil(max_total_value / 100.0)) * 100

# Set y axis ticks and ticklabels
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
plt.yticks(yticks)

# Set background grid lines
plt.grid(color='grey', linestyle='dotted', linewidth=1, alpha=0.3)

# Set colors
colors = ['#FF9999', '#FFCC99', '#FFFF99', '#99FF99', '#99CCFF']

# Set transparency
alpha = 0.8

# Plot the data with area chart
ax = plt.gca()
ax.stackplot(df['Category'], df['January'], df['February'], df['March'], df['April'], df['May'], labels=df.columns[1:], colors=colors, alpha=alpha)
ax.legend(loc='upper left', bbox_to_anchor=(1.01, 1), borderaxespad=0, title='Month')

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, max_total_value)

# Set x and y axis labels
ax.set_xlabel('Category')
ax.set_ylabel('Attendees')

# Set title
ax.set_title('Attendance across Arts and Culture Events by Month')

# Set ticks and ticklabels
ax.set_xticks(ax.get_xticks())
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(yticks, rotation=0, ha='right', rotation_mode='anchor')

# Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-155112_21.png', bbox_inches='tight')

# Clear the current image state
plt.clf()
