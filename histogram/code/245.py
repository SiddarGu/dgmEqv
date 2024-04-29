import matplotlib.pyplot as plt

# Transform the given data into three variables
data_labels = ['1-Star', '2-Star', '3-Star', '4-Star', '5-Star']
data = [50, 75, 115, 180, 320]
line_labels = ['Average Nightly Rate ($)']

# Visualize the data as a horizontal histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Adding a grid for better readability
ax.grid(zorder=0)

# Create horizontal bar chart
bars = ax.barh(data_labels, data, color=plt.cm.Paired.colors, edgecolor='black', zorder=3)

# Add data values on the bars
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 5 # padding the labels slightly right of the bar ends
    ax.text(label_x_pos, bar.get_y() + bar.get_height() / 2, 
            f'{width}', va='center')

# Set title and labels for axes
plt.title('Average Nightly Rates by Hotel Star Rating in the Tourism Industry', fontsize=16)
plt.xlabel('Average Nightly Rate ($)', fontsize=12)

# To prevent content from being overwritten if the label is too long, rotate the label
ax.set_yticklabels(data_labels, rotation=0, fontsize=12, wrap=True)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/245.png', format='png', dpi=300)

# Clear the figure after saving to not waste memory
plt.clf()
