
import matplotlib.pyplot as plt
import numpy as np

# Create an array of data points
data = np.array([['The Avengers', 'April 26, 2012', 143],
                 ['Avengers: Endgame', 'April 26, 2019', 181],
                 ['Black Panther', 'February 16, 2018', 134],
                 ['Captain Marvel', 'March 8, 2019', 124]])

# Get the data points from the array
titles = data[:,0]
release_dates = data[:,1]
durations = data[:,2]

# Set the figure size
plt.figure(figsize=(9, 6))

# Create a subplot
ax = plt.subplot()

# Plot the data
plt.plot(release_dates, durations)

# Set the x ticks
plt.xticks(rotation=45)

# Annotate each data point
for x, y, title in zip(release_dates, durations, titles):
    ax.annotate(title, xy=(x, y))

# Set the title
plt.title('Film genres and duration of Marvel movies released between 2012 and 2019')

# Set the x and y labels
plt.xlabel('Release Date')
plt.ylabel('Duration (minutes)')

# Adjust the layout
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/198.png')

# Clear the figure
plt.clf()