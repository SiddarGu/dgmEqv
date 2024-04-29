import matplotlib.pyplot as plt
import os

# Data processing
data_labels = ['Student Enrollment (Thousands)', 'Number of Schools']
line_labels = ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50']
data = [
    [3],
    [5],
    [15],
    [20],
    [12],
    [10],
    [7],
    [4],
    [2],
    [1]
]

# Plotting the histogram
plt.figure(figsize=(10, 8))

# Adding a subplot
ax = plt.subplot(111)

# Creating a bar plot
bars = ax.bar(line_labels, [val[0] for val in data], color='skyblue')

# Adding the grid
ax.yaxis.grid(True)

# Labels and Title
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Trends in School Enrollments Across Various Educational Institutions')

# Handling long label texts
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/111.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clearing the figure
plt.clf()
