import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_labels = ['Power Generation (GWh)']
data = [
    [2150],  # Coal
    [3120],  # Natural Gas
    [2650],  # Nuclear
    [900],   # Hydropower
    [1820],  # Wind
    [1340],  # Solar
    [120],   # Geothermal
    [330]    # Biomass
]
line_labels = ['Coal', 'Natural Gas', 'Nuclear', 'Hydropower', 'Wind', 'Solar', 'Geothermal', 'Biomass']

# Create the figure and the axes
plt.figure(figsize=(12, 6))
ax = plt.subplot()

# Using Seaborn to create the histogram
sns.barplot(x=line_labels, y=[val[0] for val in data], palette="viridis")

# Set the title
ax.set_title('Power Generation Mix in Energy and Utilities Sector')

# Change the labels to vertical if they are too long
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=10, wrap=True)

# Set background grid
ax.grid(True)

# Adjust layout to fit and prevent content clipping
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/180.png', dpi=300)

# Clear the current figure state
plt.clf()
