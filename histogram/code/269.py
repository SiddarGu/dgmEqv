import matplotlib.pyplot as plt
import seaborn as sns

# Data preparation
data_labels = ["Number of Cases", "Case Type"]
line_labels = [
    "Criminal", "Civil", "Family", "Corporate", "Taxation",
    "Intellectual Property", "Environmental", "Immigration", 
    "Maritime", "Competition"
]
data = [
    500, 350, 200, 150, 100,
    80, 60, 40, 30, 20
]

# Create DataFrame
import pandas as pd

df = pd.DataFrame({
    data_labels[1]: line_labels, 
    data_labels[0]: data
})

# Set the style
sns.set_theme(style="whitegrid")

# Create the figure and the axes (subplots)
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Draw the plot
sns.barplot(x=data_labels[0], y=data_labels[1], data=df, ax=ax)

# Set title
ax.set_title('Number of Legal Cases by Type in 2023')

# Automatically adjust subplot params for the subplot(s) to fit in to the figure area.
plt.tight_layout()

# Avoid labels overlapping by rotating them
plt.xticks(rotation=45)

# Save the figure
output_path = "/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/619.png"
plt.savefig(output_path)

# Clear the current figure's state
plt.clf()
