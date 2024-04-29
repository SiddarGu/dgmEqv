import matplotlib.pyplot as plt
import numpy as np

# Transformed data
data_labels = ['Housing Prices', 'Rent Prices', 'Availability', 'Home Age', 'Market Growth']
data = [[80,75,70,65], [70,75,80,85], [60,70,80,90], [75,70,65,60], [65,70,75,80]]
line_labels = ['Downtown', 'Midtown', 'Suburb', 'Rural']

# Calculate angles and radius
num_vars = len(data_labels)
angles = np.linspace(0, 2 * np.pi, num_vars+1, endpoint=True)
max_val = np.max(np.array(data))
radius = np.linspace(1, max_val, num_vars)

# Create figure
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Loop through data to generate plots
for idx, (values,line_label) in enumerate(zip(np.array(data).T, line_labels)):
  values = np.concatenate((values,[values[0]]))  # Close loop
  ax.plot(angles, values, label=line_label)
  ax.fill(angles, values, alpha=0.25)

  # Draw gridlines
  gridline_values = np.full_like(angles, ((idx+1)*max_val)/(len(line_labels)))
  ax.plot(angles, gridline_values, '-', color='gray', linewidth=0.5)

# Set axis labels
ax.set_thetagrids(angles[:-1]*180/np.pi, data_labels, fontsize=11, wrap=True)
max_value = np.amax(data)
step_size = max_value / len(line_labels)
ax.set_rgrids([step_size * i for i in range(1, len(line_labels) + 1)], labels=[f'{step_size * i}' for i in range(1, len(line_labels) + 1)], angle=150)

# Draw legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc="upper right")

# Set radial limits
ax.set_ylim(0, max_val)

# Set title
ax.set_title('Real Estate and Housing Market Analysis', fontsize=20, fontweight='bold', position=(0.5, 1.1))

# Remove background and gridlines
ax.yaxis.grid(False)
ax.spines['polar'].set_visible(False)
plt.tight_layout()

# Save and clear figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/101_2023122292141.png')
plt.clf()
