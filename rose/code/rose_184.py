
import matplotlib.pyplot as plt
import numpy as np

# Transform data
data_labels = ['Savings', 'Investment', 'Revenue', 'Expense', 'Debt', 'Profit', 'Assets', 'Credit']
data = [100, 90, 200, 150, 50, 100, 250, 100]
line_labels = ['Variable', 'Amount']
num_categories = len(data_labels)
sector_angle = (2 * np.pi) / num_categories

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Plot data
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, label=data_labels[i], color=np.random.rand(3))

# Set ticks
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_xticks(np.linspace(0, 2 * np.pi, num_categories + 1)[:-1])
ax.set_xticklabels(data_labels, rotation=90, fontsize=12)

# Set legend
ax.legend(bbox_to_anchor=(1.3,1.0), loc="upper right")

# Set title
plt.title('Financial Summary of a Business in 2021')

# Resize image
plt.tight_layout()

# Save image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-112325_19.png')

# Clear image
plt.clf()