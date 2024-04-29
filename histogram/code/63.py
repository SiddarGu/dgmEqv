import matplotlib.pyplot as plt

# Data
data_labels = ['No High School Diploma', 'High School Graduate', 'Some College, No Degree', 'Associate\'s Degree', 'Bachelor\'s Degree', 'Master\'s Degree', 'Professional Degree', 'Doctorate']
data = [850, 1240, 950, 650, 1100, 550, 180, 120]
line_labels = ['Number of Graduates (Thousands)']

# Create figure and add subplot
plt.figure(figsize=(14, 8))
ax = plt.subplot()

# Plot histogram
bars = ax.bar(data_labels, data, color=plt.cm.Paired.colors, edgecolor='black')

# Set grid
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

# Title and labels
plt.title('Educational Attainment and Graduate Statistics')
plt.xlabel('Education Level')
plt.ylabel('Number of Graduates (Thousands)')

# Rotate x-axis labels if too long
plt.xticks(rotation=45, ha='right')

# Adding a legend
ax.legend(bars, line_labels)

# Automatically adjust subplot params for the figure layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/63.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current state
plt.clf()
