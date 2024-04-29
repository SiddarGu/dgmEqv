import matplotlib.pyplot as plt

# Transforming the given data into three variables: data_labels, data, line_labels
data_labels = ['Number of TV Shows']
line_labels = ['1-3', '3-5', '5-7', '7-9', '9-11', '11-13', '13-15', '15-17', '17-20']
data = [6, 8, 12, 15, 9, 7, 5, 3, 2]

# Creating figure and adding subplot
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Plotting the histogram
ax.bar(line_labels, data, color='skyblue', edgecolor='grey')

# Adding grid, title, and labels
ax.set_title('TV Show Viewership Levels in the Entertainment Industry')
ax.set_xlabel('Viewership Level (Millions)')
ax.set_ylabel('Number of TV Shows')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Configure the rotation to prevent label overlap
plt.xticks(rotation=45)

# Making sure layout is tight so nothing is cut off
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/230.png'
plt.savefig(save_path)

# Clear the current image state
plt.clf()
