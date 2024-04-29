
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Set x,y labels
ax.set_xlabel('Grade', fontsize=14)
ax.set_ylabel('Average GPA&Score', fontsize=14)

# Set data
grade = [6,7,8,9,10]
average_gpa = [3.5,3.6,3.7,3.8,3.9]
average_score = [85,90,95,97,99]

# Plot two line charts
plt.plot(grade, average_gpa, label='Average GPA', color='green')
plt.plot(grade, average_score, label='Average Test Score', color='blue')

# Set xticks
plt.xticks(grade)

# Set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=2)

# Set title
ax.set_title('Academic Performance Trends among Students in Grades 6-10', fontsize=16)

# Set grid
plt.grid()

# Automatically adjust subplot parameters
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/290.png')

# Clear the current image state
plt.cla()