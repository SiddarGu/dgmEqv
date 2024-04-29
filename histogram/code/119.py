import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Data as provided
raw_data = """BMI Category,Percentage (%)
Underweight (<18.5),2.3
Normal weight (18.5-24.9),35.7
Overweight (25-29.9),32.8
Obesity I (30-34.9),14.5
Obesity II (35-39.9),7.6
Extreme Obesity (≥40),7.1"""

# Split the data into lines and then on commas
lines = raw_data.split("\n")
data_labels = lines[0].split(",")
line_labels = [line.split(",")[0] for line in lines[1:]]
data = [float(line.split(",")[1]) for line in lines[1:]]

# Create a DataFrame for plotting
df = pd.DataFrame({
    data_labels[0]: line_labels,
    data_labels[1]: data
})

# Set the aesthetic style of the plots
sns.set_style("whitegrid")

# Prepare figure to plot
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plot horizontal histogram (barh) using seaborn
sns.barplot(x=data_labels[1], y=data_labels[0], data=df, palette='viridis', ax=ax)

# Set title with automatic resizing for long strings
plt.title('Prevalence of BMI Categories in the Adult Population', y=1.02)
ax.set_xlabel(data_labels[1])
ax.set_ylabel('')

# Rotate the y-axis labels if too long
plt.yticks(wrap=True)

# Automatically resize the image layout and save figure
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/119.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure directory exists
plt.savefig(save_path, dpi=300)

# Clear current figure
plt.clf()
