import matplotlib.pyplot as plt
import os

# Given data
data_labels = ['No High School Diploma', 'High School Graduate', 'Some College, No Degree', 'Associate Degree', 
               'Bachelor\'s Degree', 'Master\'s Degree', 'Professional Degree', 'Doctorate Degree']
data = [2450, 3870, 1990, 1120, 2650, 1430, 780, 320]
line_labels = ['Number of Graduates (Thousands)']

# Create figure and axis
plt.figure(figsize=(10,8))
ax = plt.subplot(111)

# Plotting the histogram
ax.bar(data_labels, data, color='skyblue')

# Add grid
ax.yaxis.grid(True)
ax.set_axisbelow(True)

# Add labels and title
plt.xticks(rotation=45, ha='right', wrap=True) # This ensures the labels are not stacked on each other
plt.xlabel('Educational Level')
plt.ylabel(line_labels[0])
plt.title('Educational Attainment and the Number of Graduates in 2023')

# Automatically adjust subplot params
plt.tight_layout()

# Creating directories if not exist and saving the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/125.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure.
plt.clf()
