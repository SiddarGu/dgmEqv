import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Grade Level': ['Kindergarten', '1st Grade', '2nd Grade', '3rd Grade', '4th Grade', '5th Grade', '6th Grade', '7th Grade', '8th Grade'],
    'Average Test Score (Out of 100)': [82, 84, 86, 87, 90, 92, 91, 89, 90]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Create bar plot
df.plot(kind='bar', x='Grade Level', y='Average Test Score (Out of 100)', ax=ax, legend=False, color=plt.cm.Paired(range(len(df))))

# Set the title
ax.set_title('Average Test Scores by Grade Level in Elementary Education', fontsize=15)

# Set labels
ax.set_xlabel('Grade Level', fontsize=12)
ax.set_ylabel('Average Test Score', fontsize=12)

# Rotate x-axis labels if needed
ax.set_xticklabels(df['Grade Level'], rotation=45, ha="right")

# Enabling grid
ax.yaxis.grid(True)

# Adjusting layout for a better fit and saving the figure.
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/27.png', dpi=300)

# To clear the current figure's state.
plt.clf()
