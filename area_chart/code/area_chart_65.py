
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Convert data to dictionary
data = {"Country": ["USA", "UK", "France", "Germany", "Spain", "Italy", "China", "Japan", "Brazil", "Mexico", "Canada", "Australia", "Russia", "India"],
        "Hotel Bookings": [10000, 8000, 5000, 4000, 3000, 2000, 1000, 500, 1000, 500, 800, 500, 800, 1000],
        "Restaurant Reservations": [20000, 15000, 10000, 8000, 6000, 4000, 2000, 1000, 1500, 1000, 1500, 1000, 1500, 2000],
        "Museum Visits": [5000, 4000, 3000, 2000, 1000, 500, 1000, 1500, 800, 400, 500, 400, 300, 1000],
        "Airport Arrivals": [100000, 80000, 50000, 40000, 30000, 20000, 10000, 5000, 10000, 5000, 8000, 5000, 8000, 10000]}

# Convert data to dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(10,7))

# Set colors
colors = ['#5C9BD5', '#ED7D31', '#A5A5A5', '#FFC000']

# Set transparency
alpha = 0.7

# Plot the chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], colors=colors, alpha=alpha)

# Set background grid lines
ax.grid(color='white', linestyle='-', linewidth=0.5)

# Set x and y axis ticks and ticklabels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xticks(np.arange(len(df.iloc[:, 0])))
    ax.set_xticklabels(df.iloc[:, 0])
    ax.set_xlim(0, len(df.index) - 1)
    
if np.random.choice([True, False], p=[0.7, 0.3]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 1000) * 1000
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))
    ax.set_ylim(0, max_total_value)

# Set x and y axis labels
ax.set_xlabel("Country")
ax.set_ylabel("Count")

# Set legend
ax.legend(["Hotel Bookings", "Restaurant Reservations", "Museum Visits", "Airport Arrivals"], loc="upper left")

# Set title
ax.set_title("Tourism and Hospitality Trends")

# Automatically resize image
plt.tight_layout()

# Save figure
fig.savefig("output/final/area_chart/png/20231228-131755_46.png", bbox_inches="tight")