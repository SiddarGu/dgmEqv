import pandas as pd
import matplotlib.pyplot as plt

# Define the variables
data_labels = ['Monthly Sales (Million $)', 'Number of Restaurants']
line_labels = ['1-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
data = [
    [150],
    [120],
    [100],
    [70],
    [50],
    [30],
    [20],
    [10],
    [5],
    [2]
]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels[1:])

# Create a figure with larger size
plt.figure(figsize=(12, 8))
ax = plt.subplot(111)

# Plot the histogram
df.plot(kind='bar', ax=ax, color='skyblue', grid=True, legend=False)

# Setting the title
plt.title('Monthly Sales Distribution Among Restaurants')

# Set axes labels
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])

# Customize tick parameters
plt.xticks(rotation=45, ha='right', wrap=True)
plt.yticks(range(0, 160, 10))

# Automatically resize the image
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/215.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current image state
plt.clf()
