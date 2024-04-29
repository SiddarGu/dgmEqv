
import matplotlib.pyplot as plt
import numpy as np

# Transform the given data into three variables: data_labels, data, line_labels. 
data_labels = ['Primary School', 'Secondary School', 'College', 'University', 'Postgraduate']
data = [1000, 2000, 3000, 4000, 500]
line_labels = ['Level of Education', 'Number of Students']

# Plot the data with the type of rose chart. 
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
sector_angle = (2 * np.pi) / len(data)

# Create colored wedges for each data category.
for i, (value, label) in enumerate(zip(data, data_labels)):
    ax.bar(i * sector_angle, value, width=sector_angle, label=label, bottom=0.0)

# Set the axes properties
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N')
ax.set_xticks(np.linspace(0, 2*np.pi, len(data_labels), endpoint=False))
ax.set_xticklabels(data_labels, fontsize=12, wrap=True, ha='center')

# Position the legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=5)

# Set the title of the figure.
plt.title('Number of Students Pursuing Different Levels of Education in 2023', fontsize=14)

# Automatically resize the image by tight_layout().
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231228-070122_71.png')

# Clear the current image state.
plt.clf()