
import matplotlib.pyplot as plt
import numpy as np

# Data
Year = [2019, 2020, 2021]
Bio_tech = [200, 220, 240]
Computer_Science = [400, 450, 500]
Engineering = [800, 850, 900]

# Create figure
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot()

# Plot the data
ax.bar(Year, Bio_tech, color='b', width=0.2, align='edge', label='Bio-technology Patents')
ax.bar(Year, Computer_Science, color='g', width=0.2, align='edge', bottom=Bio_tech, label='Computer Science Patents')
ax.bar(Year, Engineering, color='r', width=0.2, align='edge', bottom=[Bio_tech[i] + Computer_Science[i] for i in range(len(Bio_tech))], label='Engineering Patents')

# Adjust the style of the graph
ax.set_title('Patents in Bio-technology, Computer Science and Engineering from 2019 to 2021', fontsize=14, fontweight='bold')
ax.set_xlabel('Year', fontweight='bold')
ax.set_ylabel('Number of Patents', fontweight='bold')
ax.set_xticks(Year)
ax.grid(True, axis='y', linestyle='-.', color='black', linewidth=0.5)

# Add labels
ax.annotate(str(Bio_tech[0]), xy=(2019, Bio_tech[0]), xytext=(2019.2, Bio_tech[0] + 10), fontsize=10, fontweight='bold')
ax.annotate(str(Bio_tech[1]), xy=(2020, Bio_tech[1]), xytext=(2020.2, Bio_tech[1] + 10), fontsize=10, fontweight='bold')
ax.annotate(str(Bio_tech[2]), xy=(2021, Bio_tech[2]), xytext=(2021.2, Bio_tech[2] + 10), fontsize=10, fontweight='bold')
ax.annotate(str(Computer_Science[0]), xy=(2019, Bio_tech[0] + Computer_Science[0]), xytext=(2019.2, Bio_tech[0] + Computer_Science[0] + 10), fontsize=10, fontweight='bold')
ax.annotate(str(Computer_Science[1]), xy=(2020, Bio_tech[1] + Computer_Science[1]), xytext=(2020.2, Bio_tech[1] + Computer_Science[1] + 10), fontsize=10, fontweight='bold')
ax.annotate(str(Computer_Science[2]), xy=(2021, Bio_tech[2] + Computer_Science[2]), xytext=(2021.2, Bio_tech[2] + Computer_Science[2] + 10), fontsize=10, fontweight='bold')
ax.annotate(str(Engineering[0]), xy=(2019, Bio_tech[0] + Computer_Science[0] + Engineering[0]), xytext=(2019.2, Bio_tech[0] + Computer_Science[0] + Engineering[0] + 10), fontsize=10, fontweight='bold')
ax.annotate(str(Engineering[1]), xy=(2020, Bio_tech[1] + Computer_Science[1] + Engineering[1]), xytext=(2020.2, Bio_tech[1] + Computer_Science[1] + Engineering[1] + 10), fontsize=10, fontweight='bold')
ax.annotate(str(Engineering[2]), xy=(2021, Bio_tech[2] + Computer_Science[2] + Engineering[2]), xytext=(2021.2, Bio_tech[2] + Computer_Science[2] + Engineering[2] + 10), fontsize=10, fontweight='bold')

ax.legend(bbox_to_anchor=(1.02,1), loc="upper left")
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/40.png')

# Clear the current image state
plt.cla()