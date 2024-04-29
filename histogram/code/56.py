import matplotlib.pyplot as plt
import seaborn as sns

# Data preparation
data_labels = ['Percentage of Total Energy Produced (%)']
line_labels = ['Natural Gas', 'Coal', 'Nuclear', 'Hydroelectric', 'Wind', 'Solar', 'Biomass', 'Geothermal']
data = [38.2, 23.7, 19.6, 8.8, 5.5, 3.2, 1.0, 0.5]

# Create figure and axis
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Create the histogram using seaborn
sns.barplot(x=line_labels, y=data, palette='viridis')

# Set the title and labels
ax.set_title('United States Energy Production by Source (2023)', fontsize=18)
ax.set_ylabel(data_labels[0], fontsize=15)
ax.set_xlabel('Energy Source', fontsize=15)

# Fix the text overlap by rotating the x labels
plt.xticks(rotation=45, ha='right')

# Set background grid
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')

# Adjust layout to fit and prevent content from being cut off
plt.tight_layout()

# Save the histogram to the specified path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/56.png'
plt.savefig(save_path, dpi=300)

# Clear the current figure state
plt.clf()
