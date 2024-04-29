
import matplotlib.pyplot as plt

# Create figure and set size
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Set ticks
x_ticks = ['5th Grade', '6th Grade', '7th Grade', '8th Grade', '9th Grade', '10th Grade', '11th Grade', '12th Grade']
plt.xticks(list(range(len(x_ticks))), x_ticks, rotation=45, wrap=True)

# Plot data
ax.plot(x_ticks, [50, 60, 70, 80, 90, 100, 90, 80], color='red', marker='o')

# Set title
ax.set_title('Number of Students Enrolled in a School from 5th to 12th Grade')

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/431.png')

# Clear the current image state
plt.cla()