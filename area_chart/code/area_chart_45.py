
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define data dictionary
data = {'Subject': ['Math', 'Science', 'English', 'History', 'Art'], 
        'Elementary School': [30, 40, 25, 20, 10], 
        'Middle School': [40, 30, 25, 20, 20], 
        'High School': [50, 30, 20, 20, 20], 
        'Undergraduate Studies': [60, 40, 20, 20, 10], 
        'Graduate Studies': [70, 30, 20, 10, 10]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round up to nearest multiple of 10, 100, or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y axis range and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set background grid lines
ax.grid(axis='y', alpha=0.5)

# Plot stacked area chart
ax.stackplot(df['Subject'], df['Elementary School'], df['Middle School'], df['High School'], df['Undergraduate Studies'], df['Graduate Studies'], labels=['Elementary School', 'Middle School', 'High School', 'Undergraduate Studies', 'Graduate Studies'], colors=['#78C2C4', '#F5793A', '#A95AA1', '#85A4C1', '#FABD61'], alpha=0.8)

# Set x and y axis labels
ax.set_xlabel('Subject')
ax.set_ylabel('Number of Students')

# Set title
ax.set_title('Subject Performance by Education Level')

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=5)

# Automatically resize image and save
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-131755_18.png', bbox_inches='tight')

# Clear current image state
plt.clf()