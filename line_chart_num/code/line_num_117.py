
import matplotlib.pyplot as plt 
import matplotlib as mpl
import numpy as np

# Create figure
plt.figure(figsize=(15, 8))

# Create data
grade = np.array([1,2,3,4,5,6])
number_students = np.array([50,60,55,45,50,60])
average_class_size = np.array([20,25,22,17,21,25])

# Plot line chart
plt.plot(grade, number_students, label='Number of Students', color='red', marker='o', markersize=8)
plt.plot(grade, average_class_size, label='Average Class Size', color='blue', marker='o', markersize=8)

# Set axis labels
plt.xlabel('Grade')
plt.ylabel('Number')

# Set title
plt.title('Number of Students and Average Class Size in a School in 2021')

# Show legend
plt.legend(loc='best')

# Set background grid
plt.grid(True, axis='y', color='gray', linestyle='--', linewidth=1)

#Label data points
for x, y in zip(grade, number_students):
    plt.annotate(f'{y}', (x, y), xytext=(0, 10), textcoords='offset points')

for x, y in zip(grade, average_class_size):
    plt.annotate(f'{y}', (x, y), xytext=(0, 10), textcoords='offset points')
    
# Set xticks
plt.xticks(grade)

# Resize image
plt.tight_layout()

# Save chart
plt.savefig('line chart/png/278.png')

# Clear current image state
plt.clf()