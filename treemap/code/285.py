import matplotlib.pyplot as plt
import squarify

# Data
raw_data = """Defense,30
Health Care,20
Education,15
Social Security,10
Infrastructure,9
Research and Development,7
Energy,5
Agriculture,3
Foreign Aid,1"""

# Transform data into variables
data_labels = [row.split(',')[0] for row in raw_data.split('\n')]
data = [int(row.split(',')[1]) for row in raw_data.split('\n')]

# Create a figure with matplotlib
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, aspect="auto")
ax.set_title("Budget Distribution Across Government Public Policy Areas")

# Use squarify to plot a treemap
colors = plt.cm.Spectral([float(i) / max(data) for i in data])
squarify.plot(sizes=data, label=data_labels, color=colors, alpha=.8, text_kwargs={'fontsize':10, 'wrap':True})

# Remove axes
plt.axis('off')

# Resize the figure to fit all the content
plt.tight_layout()

# Save the figure to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1035.png'
plt.savefig(save_path, format='png', dpi=300, bbox_inches='tight')

# Clear the current figure state to avoid any overlap if the script is run again
plt.clf()
