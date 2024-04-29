
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define data as a dictionary
data = {'Subject': ['Math', 'Science', 'English', 'History', 'Art'],
        'Elementary School': [200, 180, 150, 130, 100],
        'Middle School': [250, 200, 180, 150, 120],
        'High School': [300, 250, 220, 200, 180],
        'Undergraduate': [350, 300, 250, 230, 200],
        'Graduate': [400, 350, 300, 280, 250]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
plt.figure(figsize=(10, 6))

# Set background grid lines
plt.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.5)

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up to nearest multiple of 10, 100 or 1000
max_total_value = np.ceil(max_total_value / 10) * 10

# Set y ticks and ticklabels
plt.yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
plt.ylabel('Number of Students')

# Set x ticks and ticklabels
plt.xticks(np.arange(len(df.index)), df.iloc[:, 0])
plt.xlabel('Subject')

# Set title
plt.title('Student Enrollment by Subject and Education Level')

# Set colors and transparency
colors = ['royalblue', 'tomato', 'mediumseagreen', 'goldenrod', 'orchid']
alpha = 0.7

# Plot the data with stacked area chart
plt.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], colors=colors, alpha=alpha)

# Set legend
labels = ['Elementary School', 'Middle School', 'High School', 'Undergraduate', 'Graduate']
plt.legend(labels=labels, loc='upper left')

# Automatically resize image
plt.tight_layout()

# Save the chart as a png image
plt.savefig('output/final/area_chart/png/20231228-131755_32.png', bbox_inches='tight')

# Clear current image state
plt.clf()