import matplotlib.pyplot as plt
import pandas as pd

# Given data
data_labels = ['Violent Crime', 'Property Crime', 'White-collar Crime', 
               'Cyber Crime', 'Drug-related Crime', 'Homicides', 'Theft', 'Assault']
data = [372.5, 2500.3, 150.7, 87.9, 695.4, 5.2, 1800.1, 345.6]
line_labels = ['Crime Rate per 100,000 People', 'Number of Cases']

# Create a DataFrame
df = pd.DataFrame({'Crime Category': data_labels, 'Crime Rate': data})

# Create a figure and add a subplot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot()

# Plot horizontal bar chart
df.plot(kind='barh', y='Crime Rate', x='Crime Category', ax=ax, legend=False, color='skyblue')

# Set title and labels
ax.set_title('National Crime Statistics by Category', fontsize=20)
ax.set_xlabel('Crime Rate per 100,000 People', fontsize=14)
ax.set_ylabel('Crime Category', fontsize=14)

# Customize x-axis labels to prevent overlapping
plt.xticks(rotation=45, ha='right')
plt.yticks(wrap=True)

# Adding grid lines
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Layout and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/234.png')

# Clear the current figure state
plt.clf()
