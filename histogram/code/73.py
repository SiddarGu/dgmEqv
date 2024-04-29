import pandas as pd
import matplotlib.pyplot as plt

# Data
data_labels = ['Number of Cases']
line_labels = [
    'Civil Litigation',
    'Corporate Law',
    'Criminal Defense',
    'Intellectual Property',
    'Environmental Law',
    'Family Law',
    'Labor and Employment',
    'Tax Law',
    'Real Estate Law'
]
data = [120, 90, 70, 85, 40, 50, 65, 30, 55]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Plotting
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
df.plot(kind='bar', ax=ax, color='skyblue', grid=True)

# Set title and labels
ax.set_title('Number of Legal Cases by Type of Affair in 2023')
ax.set_xlabel('Type of Legal Affair')
ax.set_ylabel('Number of Cases')

# Rotate x-axis labels
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', wrap=True)

# Make the plot more fancy with aesthetics
ax.grid(zorder=0, linestyle='--', color='gray')
ax.set_facecolor('whitesmoke')
fig.set_facecolor('ivory')
ax.legend(loc='upper right')

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/73.png')

# Clear the current figure state
plt.clf()
