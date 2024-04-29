import matplotlib.pyplot as plt
import numpy as np

# Data
data_labels = ["Q1", "Q2", "Q3", "Q4"]
data = np.array([[100, 105, 110, 120], [80, 85, 90, 95], [85, 90, 95, 100], [75, 70, 65, 60], [70, 75, 80, 85]] )
line_labels = ["Price", "Location", "Size", "Age", "Maintenance"]

# Number of variables we're plotting
num_vars = len(data_labels)

# Split the circle into even parts and save the angles so we know where to put each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# The plot is a circle, so we need to "complete the loop" and append the start to the end
data = np.concatenate((data, data[:, :1]), axis=1)
angles += angles[:1]

# Create figure and polar subplot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Helper function to plot each row of the data
def draw_poly(row_data, color, label):
    ax.fill(angles, row_data, color=color, alpha=0.25, label=label)

# Helper function to draw the lines
def draw_outline(max_value, color):
    radii = np.full_like(angles, max_value)
    ax.plot(angles, radii, color=color, linestyle='dashed')

# Loop over each row
colors=['red', 'blue', 'green', 'purple', 'orange']
for i, row_data in enumerate(data):
    draw_poly(row_data, color=colors[i], label=line_labels[i])
    draw_outline((i + 1) * np.amax(data) / len(data), color='grey')

# Set the y tick values - radial axes
max_value = np.amax(data)
step_size = max_value / len(data)
ax.set_rgrids([step_size * i for i in range(1, len(data) + 1)], labels=[f'{step_size * i}' for i in range(1, len(data) + 1)], angle=90)

# Set the x tick values - circular axes
ax.set_thetagrids(np.degrees(angles[:-1]), data_labels, fontsize=11, wrap=True)

# Make the labels go clockwise
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Remove the circular gridline
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(False)

# Add a title
plt.title('Radar Chart for Real Estate and Housing Market in 2023', size=20, color='black', y=1.1)

# Add legend
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, line_labels, loc='upper right')

# Adjusting the image size
plt.tight_layout()

# Save and show
fig_path = "/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/radar_polygon/png/113_2023122292141.png"
plt.savefig(fig_path)

plt.show()

# Clear figure
plt.clf()
plt.close()
