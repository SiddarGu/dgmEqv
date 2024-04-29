
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define data dictionary
data = {
    'Category': ['Language Arts', 'Mathematics', 'Natural Sciences', 'Social Sciences', 'Business', 'Fine Arts', 'Law', 'Medicine', 'Education', 'Engineering', 'History', 'Computer Science', 'Psychology', 'Communications', 'Philosophy', 'Nursing'],
    'Undergraduate Students': [500, 400, 600, 450, 550, 300, 200, 400, 800, 650, 250, 700, 450, 350, 300, 400],
    'Graduate Students': [300, 200, 400, 350, 300, 200, 100, 250, 500, 400, 150, 450, 350, 250, 200, 300],
    'Faculty Members': [50, 40, 60, 40, 50, 30, 20, 30, 100, 50, 20, 60, 40, 30, 25, 25]
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Calculate max total value and ceil it to the nearest multiple of 100
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Set colors and transparency
colors = ['#F44336', '#FFC107', '#9C27B0']
alpha = 0.7

# Plot the data with the type of area chart
ax.stackplot(df.index, df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], colors=colors, alpha=alpha)

# Set x and y axis ticks and ticklabels
ax.set_xlim(0, len(df.index) - 1)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
ax.set_yticklabels([str(i) for i in ax.get_yticks()], rotation=45, ha='right', rotation_mode='anchor')

# Set x and y axis labels
ax.set_xlabel('Academic Disciplines')
ax.set_ylabel('Total Number')

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Set legend
ax.legend(['Undergraduate Students', 'Graduate Students', 'Faculty Members'], loc='upper left')

# Set title, resize image and save
ax.set_title('Student and Faculty Distribution across Academic Disciplines')
fig.tight_layout()
fig.savefig('output/final/area_chart/png/20231228-145339_15.png', bbox_inches='tight')

# Clear current image state
plt.clf()