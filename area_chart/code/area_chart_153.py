
# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create a dictionary to hold the data
data = {"Category": ["Football (Events)", "Basketball (Events)", "Soccer (Events)", "Tennis (Events)", "Baseball (Events)"],
        "2021": [200, 150, 180, 130, 250],
        "2022": [100, 120, 150, 100, 200],
        "2023": [150, 180, 200, 150, 250],
        "2024": [100, 200, 250, 180, 150],
        "2025": [200, 180, 150, 130, 100],
        "2026": [150, 200, 100, 250, 120],
        "2027": [180, 150, 100, 200, 170],
        "2028": [130, 100, 150, 180, 200],
        "2029": [250, 130, 100, 200, 150],
        "2030": [120, 100, 200, 180, 150],
        "2031": [180, 200, 150, 100, 250],
        "2032": [150, 180, 130, 200, 100],
        "2033": [120, 150, 200, 170, 130],
        "2034": [100, 200, 250, 150, 180]
        }

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(10,6))

# Create ax variable for plotting
ax = fig.add_subplot(111)

# Plot the data with area chart
ax.stackplot(df["Category"], df.iloc[:,1], 
             df.iloc[:,2], df.iloc[:,3], df.iloc[:,4], df.iloc[:,5],
             df.iloc[:,6], df.iloc[:,7], df.iloc[:,8], df.iloc[:,9],
             df.iloc[:,10], df.iloc[:,11], df.iloc[:,12], df.iloc[:,13],
             df.iloc[:,14],
             labels=["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "2033", "2034"])

# Set x and y axis limits
ax.set_xlim(0, len(df.index) - 1)
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 10) * 10
ax.set_ylim(0, max_total_value)

# Set yticks with length in list of [3, 5, 7, 9, 11]
yticks_length = np.random.choice([3, 5, 7, 9, 11])
ax.set_yticks(np.linspace(0, max_total_value, yticks_length, dtype=np.int32))

# Set x and y axis labels
ax.set_xlabel("Category")
ax.set_ylabel("Number of Events")

# Set title of the figure
plt.title("Events by Sport for Upcoming Years")

# Set background grid lines
ax.grid(color='gray', linestyle='-', linewidth=0.5)

# Set legend and its position
ax.legend(loc="upper left")

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig("output/final/area_chart/png/20231228-140159_7.png", bbox_inches='tight')

# Clear the current image state
plt.clf()