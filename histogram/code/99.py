import matplotlib.pyplot as plt

# Given data
data = [
    [1-5, 30],
    [5-10, 25],
    [10-15, 20],
    [15-20, 15],
    [20-25, 10],
    [25-30, 5],
    [30-35, 3],
    [35-40, 2]
]

# Transforming data
data_labels = ['Sales Volume (Billion USD)', 'Number of Companies']
line_labels = ['1-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30-35', '35-40']
sales_data = [row[1] for row in data]

# Create figure and plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Vertical histogram
ax.bar(line_labels, sales_data, color='skyblue')

# Set title
ax.set_title('Sales Volume Distribution Among Food and Beverage Companies')

# Set grid
ax.yaxis.grid(True)

# Rotate x labels if necessary
plt.xticks(rotation=45)
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/99.png')
plt.close('all')  # Clear the current image state
