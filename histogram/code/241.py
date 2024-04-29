import matplotlib.pyplot as plt

# Define data and labels
data_labels = ['Freshman', 'Sophomore', 'Junior', 'Senior', 'Graduate']
line_labels = ['Average GPA']
data = [2.9, 3.0, 3.1, 3.2, 3.5]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_title('Average GPA by Academic Level in US Colleges')

# Plot a horizontal bar chart
bars = ax.barh(data_labels, data, color=plt.cm.tab20.colors)

# Add data labels with a different style, by iterating over the bars
for bar in bars:
    ax.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f"{bar.get_width():.1f}",
        va='center',
        ha='left'
    )

# Add grid lines behind bars
ax.set_axisbelow(True)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.25)
ax.set_xlabel('Average GPA')
# Rotate labels if necessary - in this case, not required since the labels are short
# plt.xticks(rotation=45, ha='right')
# plt.yticks(wrap=True)  # Wraps the y labels if the text is too long

# Check the representation to make sure everything fits well
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/hancheng/histogram/png_val/241.png')

# Clear the current figure to prevent re-plotting the same data
plt.clf()
