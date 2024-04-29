
import matplotlib.pyplot as plt

# Restructure the data
primary_school = [5, 25, 50, 75, 95]
secondary_school = [20, 45, 65, 85, 100]
university = [35, 55, 70, 85, 95]
postgraduate = [45, 60, 75, 90, 100]
vocational = [15, 30, 50, 70, 90]

# Set up figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)

# Plot the data
ax.boxplot([primary_school, secondary_school, university, postgraduate, vocational],
            labels=['Primary School', 'Secondary School', 'University',
                    'Postgraduate', 'Vocational'])

# Plot outliers
ax.plot(2,110,'o', color='red')
ax.plot(3,2,'o', color='red')
ax.plot(3,105,'o', color='red')
ax.plot(4,110,'o', color='red')
ax.plot(5,110,'o', color='red')

# Set title
ax.set_title('Exam Score Distribution of Different Education Levels (2021)')

# Set label
ax.set_xlabel('Education Level')
ax.set_ylabel('Score (Percentage)')

# Set background grid
ax.grid(axis='y', alpha=0.75)

# Automatically resize the image
fig.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/5_202312251044.png')

# Clear the current image state
plt.clf()