import pandas as pd
import matplotlib.pyplot as plt

# The given data
data_labels = ['Global Internet Speed (Mbps)', 'Number of Countries']
line_labels = ['1-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50']
data = [
    [4],
    [8],
    [14],
    [17],
    [21],
    [25],
    [19],
    [15],
    [10],
    [6]
]

# Create a DataFrame using the data and labels
df = pd.DataFrame(data, index=line_labels, columns=data_labels[1:])

# Create a figure with a larger size
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Plotting the data
df.plot(kind='barh', ax=ax, legend=False)

# Adding grid, labels, and title
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_xlabel(data_labels[1])
ax.set_title('Global Distribution of Internet Connection Speeds')

# Set rotation or wrap if necessary for long text
ax.set_yticklabels(line_labels, rotation=0, wrap=True)

# Resize the image before saving using tight_layout
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/16.png'
plt.savefig(save_path, dpi=300)

# Clear the current image state
plt.clf()
