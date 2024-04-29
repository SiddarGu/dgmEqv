import seaborn as sns
import matplotlib.pyplot as plt

# Given data
data_labels = ['Number of Hotels']
line_labels = ['< $100', '$100-$199', '$200-$299', '$300-$399', '$400-$499', '$500+']
data = [12, 27, 17, 6, 3, 2]

# Create a figure
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Creating the histogram
sns.barplot(x=data, y=line_labels, palette='viridis')

# Set the title and labels
ax.set_title('Average Daily Rate Distribution Among Hotels')
ax.set_xlabel('Number of Hotels')
ax.set_ylabel('Average Daily Rate (ADR)')

# Adjust label text to prevent overlapping
plt.xticks(rotation=45)
ax.tick_params(axis='y', which='major', labelsize=10)
plt.yticks(wrap=True)

# Make the layout fit the figure size to prevent overlapping
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/86.png')

# Clear the current figure's state to prevent interference with future plots
plt.clf()
