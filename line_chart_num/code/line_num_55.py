
import matplotlib.pyplot as plt
import numpy as np

# Initialize Figure
plt.figure(figsize=(14,7))

# Create the data
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
techA = [20, 30, 40, 50, 60, 65, 70, 75]
techB = [15, 18, 22, 25, 30, 35, 40, 45]
techC = [10, 15, 20, 25, 30, 35, 40, 45]

# Plotting
plt.plot(year, techA, label="Technology A", color='red')
plt.plot(year, techB, label="Technology B", color='blue')
plt.plot(year, techC, label="Technology C", color='green')

# Setting Labels
plt.xlabel("Year", fontsize=14)
plt.ylabel("Adoption (%)", fontsize=14)
plt.title("Adoption of Latest Technologies in the Last Decade", fontsize=16)

# Setting Ticks
plt.xticks(year)

# Setting Legend
plt.legend(loc="upper left", fontsize=14)

# Setting Grids
plt.grid(True)

# Adding Labels to Data Points
for i, j in zip(year, techA):
    plt.annotate(str(j), xy=(i, j+1), fontsize=14)
for i, j in zip(year, techB):
    plt.annotate(str(j), xy=(i, j+1), fontsize=14)
for i, j in zip(year, techC):
    plt.annotate(str(j), xy=(i, j+1), fontsize=14)

# Resize the plot
plt.tight_layout()

# Save the plot
plt.savefig("line chart/png/476.png")

# Clear the plot
plt.clf()