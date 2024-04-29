
import matplotlib.pyplot as plt
import numpy as np

# Transform the data
data_labels = ["Carbon Dioxide", "Methane", "Nitrogen Oxides", "Chlorofluorocarbons", "Volatile Organic Compounds", "Ozone"]
data = [10, 8, 6, 3, 1, 2]
line_labels = ["Pollutant", "Amount"]

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='polar')

# Set the number of categories
num_categories = len(data_labels)

# Calculate the sector angle
sector_angle = (2 * np.pi) / num_categories

# Plot the data
for i in range(num_categories):
    ax.bar(sector_angle * i, data[i], width=sector_angle, bottom=0.0, label=data_labels[i], color=plt.cm.Set1(i))

# Add a legend
ax.legend(data_labels, loc="upper right", bbox_to_anchor=(1.3, 1.2))

# Set the ticks
ax.set_xticks(np.linspace(0, 2*np.pi, num_categories, endpoint=False))
ax.set_xticklabels(data_labels, fontsize=10)

# Set the title
ax.set_title("Greenhouse Gas Emissions in 2021", va="bottom", fontsize=20)

# Resize the image
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rose/png/20231227-021234_102.png')

# Clear the current image state
plt.clf()