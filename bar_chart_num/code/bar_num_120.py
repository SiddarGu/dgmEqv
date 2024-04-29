

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

# Set the x-axis data
sports = ["Football", "Basketball", "Baseball", "Hockey"]
x_pos = [i for i, _ in enumerate(sports)]

# Set the y-axis data
team_a = [30, 35, 25, 20]
team_b = [25, 30, 20, 15]
team_c = [20, 25, 15, 10]

# Plot the data
ax.bar(x_pos, team_a, width=0.5, color='#EE3224', label='Team A')
ax.bar(x_pos, team_b, width=0.5, color='#F78F1E', bottom=team_a, label='Team B')
ax.bar(x_pos, team_c, width=0.5, color='#FFC222', bottom=[i+j for i,j in zip(team_a, team_b)], label='Team C')

# Label the x-axis
plt.xticks(x_pos, sports)

# Set the chart title and legend
ax.set_title("Number of wins for three teams across four sports in 2021")
ax.legend(loc='upper right')

# Display the value of each data point on the figure
for i, j in enumerate(team_a):
    ax.annotate(str(j), xy=(i-0.2, j+0.5))

for i, j in enumerate(team_b):
    ax.annotate(str(j), xy=(i-0.2, j+team_a[i]+0.5))

for i, j in enumerate(team_c):
    ax.annotate(str(j), xy=(i-0.2, j+team_a[i]+team_b[i]+0.5))

plt.tight_layout()
plt.savefig('Bar Chart/png/497.png')
plt.clf()