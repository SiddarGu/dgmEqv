import matplotlib.pyplot as plt
import os

# Data parsing
raw_data = """Defense,721.0
Healthcare,935.0
Education,580.0
Social Security,895.0
Infrastructure,320.0
Research and Development,140.0
Environment,85.0"""

data_labels = ['Government Expenditure (Billion $)']
line_labels = []
data = []
for line in raw_data.split('\n'):
    label, value = line.split(',')
    line_labels.append(label)
    data.append(float(value))

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

ax.bar(line_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Title and labels
ax.set_title('Allocation of Federal Budget Across Government Programs')
ax.set_xlabel('Government Programs')
ax.set_ylabel('Expenditure (Billion $)')

# Customize appearance
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.6)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", wrap=True)
fig.tight_layout()  # Auto-adjust layout to prevent content overlap

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/105.png'
if not os.path.exists(os.path.dirname(save_path)):
    os.makedirs(os.path.dirname(save_path))
plt.savefig(save_path, bbox_inches='tight')

# Clear the current figure's state
plt.close(fig)
