import matplotlib.pyplot as plt
import seaborn as sns

# Transforming the given data
data_labels = ['Average Daily Hours Spent on Social Media']
line_labels = ['13-17', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
data = [3.2, 2.9, 2.7, 2.1, 1.8, 1.4, 1.1]

# Create figure and axis for the histogram
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

# Plot histogram with seaborn
sns.barplot(x=line_labels, y=data, palette='viridis', ax=ax)

# Set the title and labels of the histogram
ax.set_title('Social Media Usage by Age Group on the Web', fontsize=16)
ax.set_xlabel('Age Group (Years)', fontsize=14)
ax.set_ylabel(data_labels[0], fontsize=14)

# Set rotation for xtick labels if they are too long
plt.xticks(rotation=45)

# Automatically resize the figure layout to prevent content from being displayed improperly
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/171.png')

# Clear the current figure state at the end of the code to avoid overlap in case of multiple plots
plt.clf()
