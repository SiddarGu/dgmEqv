
import matplotlib.pyplot as plt
import numpy as np

# Data
Year = np.array([2000,2001,2002,2003,2004,2005])
Performances = np.array([200,220,240,260,280,300])
Attendance = np.array([50000,60000,65000,70000,75000,80000])

# Create figure
plt.figure(figsize=(10,8))

# Plot
plt.plot(Year, Performances, label="Performances")
plt.plot(Year, Attendance, label="Attendance")

# Label axis
plt.xlabel('Year', fontsize=14)
plt.ylabel('Attendance/Performances', fontsize=14)

# Label points
plt.annotate(str(Performances[0]), (Year[0], Performances[0]))
plt.annotate(str(Performances[1]), (Year[1], Performances[1]))
plt.annotate(str(Performances[2]), (Year[2], Performances[2]))
plt.annotate(str(Performances[3]), (Year[3], Performances[3]))
plt.annotate(str(Performances[4]), (Year[4], Performances[4]))
plt.annotate(str(Performances[5]), (Year[5], Performances[5]))

plt.annotate(str(Attendance[0]), (Year[0], Attendance[0]))
plt.annotate(str(Attendance[1]), (Year[1], Attendance[1]))
plt.annotate(str(Attendance[2]), (Year[2], Attendance[2]))
plt.annotate(str(Attendance[3]), (Year[3], Attendance[3]))
plt.annotate(str(Attendance[4]), (Year[4], Attendance[4]))
plt.annotate(str(Attendance[5]), (Year[5], Attendance[5]))

# Set title
plt.title('Attendance growth in music performances in the US from 2000 to 2005', fontsize=15)

# Set xticks
plt.xticks(np.arange(2000,2006,1))

# Legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1), fontsize=13)

# Resize figure
plt.tight_layout()

# Save figure
plt.savefig("line chart/png/167.png")

# Clear figure
plt.clf()