
import matplotlib.pyplot as plt
import numpy as np

# Set the font size of the label
plt.rcParams['font.size'] = 12

# Set the size of the image
fig = plt.figure(figsize=(8, 5))

# Set the title of the figure
plt.title("Average scores of students in four grades in 2021")

# Create an array of grade
grades = np.array([1, 2, 3, 4])

# Create an array of student
students = np.array([20, 22, 25, 24])

# Create an array of average score
average_score = np.array([90, 85, 80, 75])

# Create an array of bar width
width = 0.25

# Plot bar chart
ax = fig.add_subplot(1, 1, 1)

ax.bar(grades - width, students, width=width, label="Students")
ax.bar(grades, average_score, width=width, label="Average Score")

# Set the location of the legend
ax.legend(loc="upper right")

# Set the x-axis label
ax.set_xlabel("Grade")

# Set the y-axis label
ax.set_ylabel("Number")

# Set the range of the x-axis
ax.set_xlim(0.5, 4.5)

# Set the range of the y-axis
ax.set_ylim(0, 30)

# Set the x-axis tick labels
ax.set_xticks(grades)
ax.set_xticklabels(grades)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig("bar chart/png/217.png")

# Clear the current image state
plt.clf()