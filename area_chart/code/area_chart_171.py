
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a dictionary with the data
data = {"Level": ["High School", "Undergraduate", "Graduate", "Post-Graduate"],
        "Science (Students)": [350, 400, 450, 300],
        "Math (Students)": [400, 350, 300, 350],
        "Literature (Students)": [450, 300, 350, 400],
        "History (Students)": [300, 200, 250, 500],
        "Art (Students)": [200, 250, 300, 250]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Calculate max total value and round up to nearest multiple of 100
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 100) * 100

# Set y-axis limit and ticks
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Plot stackplot
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], df.iloc[:, 5],
             labels=["Science", "Math", "Literature", "History", "Art"],
             colors=["#FFB4D9", "#C2DFFF", "#FFFFB4", "#FFB4B4", "#B4FFB4"],
             alpha=0.8)

# Set background grid lines
ax.grid(axis='y', color='gray', linestyle='dashed', alpha=0.5)

# Set legend position and title
ax.legend(loc='upper right', title="Education Level")

# Set x-axis ticks and tick labels
ax.set_xticks(np.arange(len(df)))
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha='right', rotation_mode='anchor')

# Set title and labels
ax.set_title("Student Enrollment by Education Level")
ax.set_xlabel("Education Level")
ax.set_ylabel("Number of Students")

# Automatically resize image and save
plt.tight_layout()
plt.savefig("output/final/area_chart/png/20231228-140159_91.png", bbox_inches='tight')

# Clear current state
plt.clf()