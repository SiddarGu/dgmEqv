
import matplotlib.pyplot as plt
import numpy as np

# Transform data into 3 variables
data_labels = ['Investment Banking', 'Private Equity', 'Venture Capital', 
               'Mutual Funds', 'Hedge Funds', 'Insurance', 
               'Accounting', 'Consulting', 'Real Estate']
data = [90, 70, 60, 50, 40, 30, 20, 10, 5]
line_labels = ['Financial Category', 'Number of Companies']

# Create figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='polar')

# Plot data
num_categories = len(data)
sector_angle = (2 * np.pi) / num_categories

# Set colors for each category
colors = ['#f9c166', '#f99d3c', '#f97d15', '#f94c02', '#d62728',
          '#ff7f0e', '#2ca02c', '#1f77b4', '#9467bd']

# Draw sectors
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, 
           color=colors[i], label=data_labels[i])

# Set ticks and labels
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories + 1)[:-1])
ax.set_xticklabels(data_labels, rotation=45, ha='right', wrap=True)

# Position legend outside of chart
ax.legend(bbox_to_anchor=(1.15, 1), loc='upper left')

# Set title
ax.set_title('Number of Companies in Different Financial Sectors in 2021')

# Resize image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_34.png')

# Clear current image
plt.clf()