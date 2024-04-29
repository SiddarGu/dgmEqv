import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Prepare the data
data = [
    ["Provider A", 2000, 3400, 5000, 6600, 8000, []],
    ["Provider B", 2200, 3600, 5100, 6700, 8200, [10500]],
    ["Provider C", 2300, 3800, 5400, 7000, 8600, [11000, 12000]],
    ["Provider D", 2400, 4000, 5600, 7200, 8800, []],
    ["Provider E", 2500, 4200, 5900, 7600, 9300, [15000]],
]

# Reshape the data
box_data = [d[1:6] for d in data]
outliers_data = [d[6] for d in data]

# Create Figure
fig = plt.figure(figsize=(10,6))
gs = gridspec.GridSpec(1,1)
ax = fig.add_subplot(gs[0])

# Create box plot
bp = ax.boxplot(box_data, vert=False, widths=0.6, notch=True, whis=1.5)

# Plotting outliers
for i, outlier in enumerate(outliers_data):
    if outlier:
        ax.plot(outlier, [i + 1]*len(outlier), "ro")

# Plot customization
ax.grid(which='both', axis='x', linestyle="--", color='gray', alpha=0.6)
ax.set_yticklabels([d[0] for d in data], fontsize=8)
ax.set_title('Power Consumption Distribution across Utility Providers (2021)')
ax.set_xlabel("Consumption (kWh)", fontsize=8)
ax.xaxis.grid(True)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/72_202312270030.png')

# Clear the current image state
plt.clf()
