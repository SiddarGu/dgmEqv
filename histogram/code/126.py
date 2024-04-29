import matplotlib.pyplot as plt

# Data
data_labels = ['Number of Online Stores']
line_labels = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
data = [
    [150, 120, 180, 200, 160, 170, 210, 190, 180, 220, 240, 230]
]

# Create figure and add subplot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111)

# Plotting the histogram
for i in range(len(data)):
    ax.bar(range(len(data[i])), data[i], label=data_labels[i])

# Add some fancy features
ax.set_title('Monthly Online Retail Sales Distribution',  fontsize=16)
ax.set_xlabel('Monthly Sales ($Millions)', fontsize=14)
ax.set_ylabel('Number of Online Stores', fontsize=14)
ax.set_xticks(range(len(line_labels)))
ax.set_xticklabels(line_labels, rotation=45, ha='right', fontsize=12)
ax.legend()

# Background grid
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_val/126.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
