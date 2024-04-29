import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_str = """Housing Price Range (Thousands),Number of Houses Sold
100-200,55
200-300,75
300-400,90
400-500,60
500-600,40
600-700,30
700-800,20
800-900,15
900-1000,10"""

# Transforming the data into three variables: data_labels, data, and line_labels
data_lines = data_str.strip().split('\n')
data_labels = [data_lines[0].split(',')[1]]  # Only one data_label
line_labels = [line.split(',')[0] for line in data_lines[1:]]  # Price ranges
data = [int(line.split(',')[1]) for line in data_lines[1:]]  # Number of houses sold

# Create a DataFrame for easy plotting with pandas
df = pd.DataFrame(data={'Number of Houses Sold': data}, index=line_labels)

# Set up the matplotlib figure and axes
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plot the data as a vertical histogram
df.plot(kind='bar', ax=ax, color='skyblue', legend=False)

# Adding grid, titles and labels
ax.set_title("Housing Sales Distribution by Price Range")
ax.set_xlabel("Housing Price Range (Thousands)")
ax.set_ylabel("Number of Houses Sold")

# Handle long text labels
plt.xticks(rotation=45, wrap=True)

# Resize the image to fit content
plt.tight_layout()

# Save the figure to the specified path
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/220.png"
plt.savefig(save_path)

# Clear the current image state at the end of the code
plt.clf()
