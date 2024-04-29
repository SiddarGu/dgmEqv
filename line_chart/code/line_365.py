
import matplotlib.pyplot as plt
import numpy as np

# Data
Month = np.array(["January", "February", "March", "April", "May", "June"])
Facebook_Users = np.array([1000, 1200, 1500, 1800, 2000, 2200])
Twitter_Users = np.array([500, 600, 700, 800, 900, 1000])
Instagram_Users = np.array([100, 150, 200, 250, 300, 350])

# Create figure
fig = plt.figure(figsize=(12, 7))

# Plot line chart
ax = fig.add_subplot()
ax.plot(Month, Facebook_Users, label="Facebook Users(million people)")
ax.plot(Month, Twitter_Users, label="Twitter Users(million people)")
ax.plot(Month, Instagram_Users, label="Instagram Users(million people)")

# Set ticks
ax.set_xticks(np.arange(len(Month)))
ax.set_xticklabels(Month, rotation=20, ha="right")

# Set titles, labels and legend
ax.set_title("Global Social Media User Growth in the First Half of 2021", fontsize=20)
ax.set_xlabel("Month", fontsize=15)
ax.set_ylabel("Number of users(million people)", fontsize=15)
ax.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Resize image
plt.tight_layout()

# Save figure
plt.savefig("line chart/png/363.png")

# Clear figure
plt.clf()