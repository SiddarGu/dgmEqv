
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define data dictionary
data = {
    'Category': ['Employee Satisfaction', 'Employee Turnover', 'Training & Development', 'HR Policies',
                 'Recruitment'],
    'Finance': [80, 15, 20, 10, 12],
    'Marketing': [90, 10, 15, 8, 15],
    'IT': [75, 20, 18, 12, 20],
    'Operations': [85, 12, 15, 10, 18],
    'Customer Service': [80, 15, 17, 9, 14],
}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10, 8))

# Calculate max total value and round up to nearest multiple of 10, 100 or 1000
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
if max_total_value < 10:
    max_total_value = round(max_total_value)
elif max_total_value < 100:
    max_total_value = round(max_total_value, -1)
elif max_total_value < 1000:
    max_total_value = round(max_total_value, -2)
else:
    max_total_value = round(max_total_value, -3)

# Set y ticks and tick labels
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)
ax.set_yticklabels(yticks)

# Set x ticks and tick labels
xticks = np.arange(len(df.index))
ax.set_xticks(xticks)
ax.set_xticklabels(df.iloc[:, 0])

# Plot area chart
ax.stackplot(xticks, df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5], 
             labels=df.columns[1:],
             colors=['#FFC0CB', '#FFA07A', '#FFDAB9', '#F0E68C', '#7FFFD4'], alpha=0.7)

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)

# Set grid lines
ax.grid(linestyle='--')

# Set title
plt.title('Employee Performance and Development in Various Departments')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig('output/final/area_chart/png/20231226-130527_6.png', bbox_inches='tight')

# Clear current image state
plt.clf()