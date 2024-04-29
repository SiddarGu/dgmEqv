
import pandas as pd
import matplotlib.pyplot as plt

# Data processing
data = {'Department':['Sales', 'Marketing', 'HR', 'IT', 'Finance', 'Operations', 'Legal', 'Customer Service', 'Manufacturing'],
        'Employee Satisfaction (%)':[85, 90, 95, 80, 92, 88, 93, 91, 86],
        'Employee Turnover (%)':[12, 10, 8, 15, 9, 11, 7, 8, 13],
        'Training Hours':[50, 40, 60, 70, 55, 65, 45, 55, 60],
        'Salary ($)':[50000, 55000, 65000, 70000, 60000, 65000, 70000, 55000, 65000]}
df = pd.DataFrame(data)

# Plotting the chart
fig, ax = plt.subplots(figsize=(10,6))
heatmap = ax.imshow(df.iloc[:, 1:], cmap='coolwarm', interpolation='nearest', aspect='auto')

# Set the ticks and ticklabels for x and y axis
ax.set_xticks(range(len(df.columns[1:])))
ax.set_yticks(range(len(df['Department'])))

ax.set_xticklabels(df.columns[1:], rotation=45, ha='right', rotation_mode='anchor', wrap=True)
ax.set_yticklabels(df['Department'], wrap=True)

# Center the ticks and ticklabels
ax.set_xticks([x - 0.5 for x in ax.get_xticks()], minor=True)
ax.set_yticks([y - 0.5 for y in ax.get_yticks()], minor=True)
ax.tick_params(which='minor', length=0)

# Show the value of each cell
for i in range(len(df['Department'])):
    for j in range(len(df.columns[1:])):
        text = ax.text(j, i, df.iloc[i, j+1], ha='center', va='center', color='w')

# Add a colorbar
cbar = plt.colorbar(heatmap)

# Set the title of the figure
plt.title('Human Resources Metrics')

# Automatically resize the image
fig.tight_layout()

# Save the chart
plt.savefig('output/final/heatmap/png/20231228-131639_62.png', bbox_inches='tight')

# Clear the current image state
plt.clf()