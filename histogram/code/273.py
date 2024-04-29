import matplotlib.pyplot as plt

# Data provided
data_labels = ['Daily Active Users (millions)']
line_labels = ['Facebook', 'YouTube', 'WhatsApp', 'Instagram', 'Twitter', 'Snapchat', 'Pinterest', 'LinkedIn', 'TikTok']
data = [1760, 1220, 1000, 500, 330, 210, 150, 100, 690]

# Start plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)  # Create a subplot in a grid of 1x1

# Plotting the histogram
ax.bar(line_labels, data, color='tab:blue')

# Add grid
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

# Rotate x-axis labels to prevent overlapping
plt.xticks(rotation=45, ha="right", rotation_mode="anchor", wrap=True)

# Set title
plt.title('Daily Active Users on Major Social Media Platforms')

# Make layout tight to fit everything
plt.tight_layout()

# Save figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/623.png', format='png')

# Clear the current figure state to avoid interference with further plotting
plt.clf()
