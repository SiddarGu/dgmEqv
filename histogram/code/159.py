import matplotlib.pyplot as plt

data_labels = ['Freight Volume (Million Tonnes)']
line_labels = ['Truck', 'Rail', 'Ship', 'Air', 'Pipeline', 'Inland Waterways']
data = [2520, 1130, 980, 350, 560, 210]

fig, ax = plt.figure(figsize=(10, 7)), plt.gca()
bars = ax.barh(line_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

ax.set_title('Freight Transportation Volume by Mode')
ax.set_xlabel(data_labels[0])
ax.set_ylabel('Vehicle Type')
ax.set_xlim(0, max(data) * 1.1)  # Set the x-axis limit a bit higher to make the chart clearer
ax.yaxis.grid(True, linestyle='--', which='major', color='gray', alpha=0.7)

# Adding data labels on each bar
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + max(data) * 0.02
    ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, f'{width}', va='center')

# Handle long text labels
plt.xticks(rotation=45)
plt.tight_layout()

save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/159.png'
plt.savefig(save_path, dpi=300)
plt.clf()
