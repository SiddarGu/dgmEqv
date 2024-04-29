
import matplotlib.pyplot as plt
import numpy as np

# Create figure and add subplot
fig = plt.figure()
ax = fig.add_subplot()

# Set data
Province = np.array(["Ontario", "Quebec", "Alberta", "British Columbia"])
Students_Enrolled = np.array([500, 700, 800, 600])
Faculty_Members = np.array([50, 60, 70, 80])

# Plot bar chart
x = np.arange(len(Province))
width = 0.35
ax.bar(x - width/2, Students_Enrolled, width = width, label = "Students Enrolled")
ax.bar(x + width/2, Faculty_Members, width = width, label = "Faculty Members")

# Set label
ax.set_xticks(x)
ax.set_xticklabels(Province, rotation = 45, ha = "right")
ax.set_ylabel("Number")
ax.set_title("Number of students and faculty members in four provinces in 2021")
ax.legend(loc = "upper right")

# Set figure size and save figure
fig.set_figwidth(13)
fig.set_figheight(8)
fig.tight_layout()
plt.savefig("bar chart/png/79.png")

# Clear figure
plt.clf()