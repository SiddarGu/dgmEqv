
import matplotlib.pyplot as plt
import numpy as np

# Set the data
region = ['North America','Europe','Asia','Oceania'] 
sports_teams = [18,20,15,12]
attendance = [55,45,35,25]

# Create the figure
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

# Plot the data
ax.bar(region, sports_teams, label='Sports Teams', bottom=0, width=0.4)
ax.bar(region, attendance, label='Attendance(hundred)', bottom=np.array(sports_teams), width=0.4)

# Set the title
ax.set_title('Number of sports teams and attendance in four regions in 2021')

# Adjust the legend
ax.legend(loc="best")

# Adjust the label
ax.set_xticks(region)
ax.set_xticklabels(region,rotation=45)


# Adjust the layout
plt.tight_layout()

# Save the image
plt.savefig('bar_331.png')

# Clear the current figure
plt.clf()