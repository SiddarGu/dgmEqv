import matplotlib.pyplot as plt
import seaborn as sns

# Given data
raw_data = """Underweight (<18.5),4.8
Normal weight (18.5-24.9),57.2
Overweight (25-29.9),68.4
Obesity I (30-34.9),41.8
Obesity II (35-39.9),26.1
Extreme Obesity (≥40),18.7"""

# Transform the data into the required variables
line_labels = []
data = []
for line in raw_data.splitlines():
    label, value = line.split(',')
    line_labels.append(label)
    data.append(float(value))

# Visualization
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plot histogram
sns.barplot(x=line_labels, y=data, ax=ax, palette="viridis")

# Set the title and labels
ax.set_title('Population Distribution by BMI Categories in the United States')
ax.set_xlabel('BMI Category')
ax.set_ylabel('Population (Millions)')

# Rotate x labels and wrap them if they are too long
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right', wrap=True)

# Layout adjustment and grid
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/98.png', dpi=300)

# Clear the current image state
plt.clf()
