import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Grade Level': ['Kindergarten', '1st Grade', '2nd Grade', '3rd Grade', '4th Grade', '5th Grade', '6th Grade', '7th Grade', '8th Grade'],
    'Number of Students (thousands)': [300, 320, 310, 305, 315, 325, 335, 345, 340]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Setting up the plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Create histogram
df.plot(kind='bar', x='Grade Level', y='Number of Students (thousands)', ax=ax, legend=False, color=plt.cm.tab20c.colors)

# Set the title and labels
ax.set_title('Student Enrollment Numbers by Grade Level in Elementary and Middle Schools')
ax.set_xlabel('Grade Level')
ax.set_ylabel('Number of Students (thousands)')

# Add grid
ax.grid(axis='y')

# Rotate x-axis labels if necessary to prevent overlapping
ax.set_xticklabels(df['Grade Level'], rotation=45, ha="right")

# Automatically adjust subplot params for better layout
plt.tight_layout()

# Save plot to file
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/75.png')

# Clear the current figure's state to prevent overlap with future plots
plt.clf()

