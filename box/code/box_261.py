import matplotlib.pyplot as plt

# Data
data = [
    ['Provider A', 10, 20, 30, 40, 50, []],
    ['Provider B', 15, 25, 35, 45, 55, [5, 65]],
    ['Provider C', 20, 30, 40, 50, 60, [5.0, 70.0]],
    ['Provider D', 10, 25, 35, 45, 60, [4.6, 75.0]],
    ['Provider E', 12, 22, 32, 42, 52, [80.0]]
]

# Separating data into lists of values and outliers
box_plot_values = [row[1:6] for row in data]
outliers = [row[6] for row in data]
x_ticks = [row[0] for row in data]

# Creating figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Box plots
ax.boxplot(box_plot_values, whis=1.5)

# Outliers
for i, out in enumerate(outliers):
    if out:
        y = out
        x = [i + 1] * len(out)
        ax.plot(x, y, "rx")

# Background grid
ax.grid(True)

# Set axis labels
ax.set_xticklabels(x_ticks, rotation=45, ha='right')
ax.set_ylabel('Ping Time (ms)')

# Set title
plt.title('Ping Time Distribution Across Internet Service Providers')

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/159_202312310058.png')

# Clear the current figure
plt.clf()
