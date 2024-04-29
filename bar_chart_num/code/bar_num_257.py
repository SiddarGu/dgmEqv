
import matplotlib.pyplot as plt
import numpy as np

# Set the width of the bars
barWidth = 0.25

# Set the data
month = ["January", "February", "March", "April"]
fulltime = [50, 50, 50, 55]
parttime = [25, 30, 35, 30]
contract = [25, 20, 15, 15]

# Set the position of the bars
r1 = np.arange(len(fulltime))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

# Make the plot
plt.figure(figsize=(10,6))
plt.bar(r1, fulltime, width=barWidth, label="Full-time Staff(%)", edgecolor='white')
plt.bar(r2, parttime, width=barWidth, label="Part-time Staff(%)", edgecolor='white')
plt.bar(r3, contract, width=barWidth, label="Contract Staff(%)", edgecolor='white')

# Add xticks on the middle of the group bars
plt.xlabel("Month", fontweight='bold')
plt.xticks([r + barWidth for r in range(len(fulltime))], month)

# Add text labels at the top of the bars
for i in range(len(fulltime)):
    plt.text(x = r1[i]-0.08 , y = fulltime[i]+0.5, s = fulltime[i], size = 10)
    plt.text(x = r2[i]-0.08 , y = parttime[i]+0.5, s = parttime[i], size = 10)
    plt.text(x = r3[i]-0.08 , y = contract[i]+0.5, s = contract[i], size = 10)

# Add legend
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)

# Add title
plt.title("Percentage of staff in three categories from January to April 2021")

# Adjust the figure
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/586.png')

# Clear the current image state
plt.clf()