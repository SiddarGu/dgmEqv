

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax = plt.subplot()

# Parse data
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
users = [100, 130, 160, 190, 220, 250, 280, 310]
time = [45, 50, 55, 60, 65, 70, 75, 80]

# Plot data
ax.plot(year, users, color='blue', marker='o', linestyle='--', label='Average Users(million)')
ax.plot(year, time, color='red', marker='o', linestyle='--', label='Average Time Spent(minutes)')

# Set title
plt.title('Increase in Average Social Media Users and Time Spent on Platforms from 2011-2018')

# Set x-axis label
ax.set_xlabel('Year', fontsize=12)

# Set y-axis label
ax.set_ylabel('Average Users(million) & Average Time Spent(minutes)', fontsize=12)

# Set xtick
ax.set_xticks(year)

# Annotate each data point
for i in range(len(year)):
    ax.annotate(str(users[i])+'&'+str(time[i]), xy=(year[i], users[i]), rotation=45,
                ha='right', va='bottom', fontsize=10, wrap=True)

# Set legend
ax.legend(loc='upper left')

# Automatically resize the image by tight_layout
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/368.png')

# Clear the current image state
plt.clf()