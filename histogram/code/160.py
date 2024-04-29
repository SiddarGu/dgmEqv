import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    'Daily Time Spent on Site (minutes)': ['0-30', '30-60', '60-90', '90-120', '120-150', '150-180', '180-210', '210-240', '240+'],
    'Number of Users (Thousands)': [200, 500, 400, 300, 150, 100, 50, 25, 10]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Plotting the histogram
fig = plt.figure(figsize=(10, 8))  # Set the figsize to something larger
ax = fig.add_subplot(111)

# Create a horizontal bar chart
ax.barh(df['Daily Time Spent on Site (minutes)'], df['Number of Users (Thousands)'])

# Set grid on
ax.grid(True)

# Set the title of the figure
ax.set_title('User Engagement: Average Daily Time Spent on Social Media Websites')

# To avoid overlapping of axis labels, set rotation or wrapping
plt.xticks(rotation=45)
plt.yticks(wrap=True)

# Automatically adjust subplot params for the plot to look better
plt.tight_layout()

# Save the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/160.png', format='png')

# Clear the current figure
plt.clf()
