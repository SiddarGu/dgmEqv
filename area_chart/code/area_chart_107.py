
## Import necessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Define data as a dictionary and convert first column to string type
data = {"Month": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "Hotel Bookings (%, Total)": [25, 30, 35, 20, 25, 30, 35, 20, 25, 30, 35, 20],
        "AirBnB Rentals (%, Total)": [20, 25, 30, 40, 35, 30, 25, 35, 30, 35, 25, 30],
        "Vacation Packages (%, Total)": [30, 15, 20, 30, 25, 20, 25, 30, 35, 25, 30, 40],
        "Cruise Ship Bookings (%, Total)": [25, 30, 25, 10, 15, 20, 15, 15, 10, 10, 10, 10]}

df = pd.DataFrame(data) # Process data using pandas

df.iloc[:, 0] = df.iloc[:, 0].astype(str) # Convert first column to string type

## Set up figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

## Plot data as an area chart
ax.stackplot(df["Month"], df.iloc[:, 1:].values.T, labels=df.columns[1:], colors=["#ffc0cb", "#add8e6", "#90ee90", "#d3d3d3"], alpha=0.7)

## Set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]): # Set axis ticks and ticklabels with 70% probability
    ax.set_xlim(0, len(df.index) - 1) # Set x axis limits
    ax.set_xticks(np.arange(len(df))) # Set x axis ticks
    ax.set_xticklabels(df["Month"], rotation=45, ha="right", rotation_mode="anchor") # Set x axis ticklabels with rotation of 45 degrees
    ax.set_ylim(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10) # Set y axis limits and round up max total value to nearest multiple of 10
    ax.set_yticks(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) # Set y axis ticks with randomly chosen number of ticks
    ax.set_yticklabels(np.linspace(0, np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 10) * 10, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) # Set y axis ticklabels
else:
    ax.set_xticks([])
    ax.set_yticks([])

## Add background grid lines
ax.grid(axis="y", color="grey", linestyle="--", linewidth=1, alpha=0.3)

## Set legend and legend title
legend = ax.legend(loc="upper left", title="Legend", framealpha=0.8)
legend.get_title().set_fontsize(10) # Set legend title font size

## Set title and labels
ax.set_title("Tourism and Hospitality Trends by Month", fontsize=12)
ax.set_xlabel("Month")
ax.set_ylabel("Percentage of Total Bookings")
ax.set_facecolor("#f0f0f0") # Set background color of chart area

## Automatically resize image and save
fig.tight_layout()
fig.savefig("output/final/area_chart/png/20231228-140159_12.png", bbox_inches="tight")

## Clear current image state
plt.clf() 