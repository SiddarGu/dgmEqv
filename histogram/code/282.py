import matplotlib.pyplot as plt
import seaborn as sns

# Data
data = [
    [8],
    [45],
    [38],
    [22],
    [15],
    [10]
]

data_labels = ['Number of Individuals']
line_labels = [
    'Underweight (<18.5)',
    'Normal weight (18.5-24.9)',
    'Overweight (25-29.9)',
    'Obesity Class I (30-34.9)',
    'Obesity Class II (35-39.9)',
    'Obesity Class III (>40)'
]

# Create figure and axis
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Set the palette color
sns.set_palette("pastel")

# Plotting data with seaborn
sns.barplot(data, ax=ax)

# Set x-axis labels
ax.set_xticks(range(len(data)))
ax.set_xticklabels(line_labels, rotation=45, ha='right', wrap=True)

# Set y-axis label
ax.set_ylabel(data_labels[0])

# Set the title of the figure
plt.title('Prevalence of BMI Categories in a Health Study')

# Tight layout to prevent content from being displayed improperly
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/histogram/png/282.png')

# Clear the current image state
plt.clf()
