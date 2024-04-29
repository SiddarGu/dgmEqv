import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Data preparation
data = {
    "Job Satisfaction Level": [
        "1 (Low)", "2", "3", "4", "5", "6", "7", "8", "9", "10 (High)"
    ],
    "Number of Employees": [50, 75, 100, 150, 120, 95, 80, 60, 40, 30]
}

df = pd.DataFrame(data)

# Create the plot
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Use Seaborn to create the histogram
sns.barplot(x="Job Satisfaction Level", y="Number of Employees", data=df, ax=ax, palette="viridis")

# Set title and labels
plt.title("Employee Job Satisfaction Levels Across the Corporation")
plt.xlabel("Job Satisfaction Level")
plt.ylabel("Number of Employees")

# Improve label readability if text is too long
ax.set_xticklabels(df["Job Satisfaction Level"], rotation=45, ha='right', wrap=True)

# Set grid
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')

# Automatically size the plot and save it
plt.tight_layout()
plt.savefig("/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/608.png", format='png')

# Clear the current figure
plt.clf()
