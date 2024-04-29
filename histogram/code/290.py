import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    "Type of Legal Cases": [
        "Criminal",
        "Civil",
        "Intellectual Property",
        "Family Law",
        "Corporate Litigation",
        "Environmental",
        "Employment/Labor",
        "Taxation",
        "Immigration",
        "Real Estate"
    ],
    "Number of Cases Filed": [
        2750, 3250, 1500, 2000, 1750, 1200, 1450, 950, 850, 1100
    ]
}

# Create DataFrame from the data
df = pd.DataFrame(data)

# Prepare labels
data_labels = list(df.columns)
line_labels = list(df["Type of Legal Cases"])

# Set up the matplotlib figure and axes
fig = plt.figure(figsize=(14, 8))  # Set a larger figure size
ax = fig.add_subplot()

# Create a horizontal bar plot
bars = ax.barh(df["Type of Legal Cases"], df["Number of Cases Filed"], color=plt.cm.tab10(range(len(df))))

# Add grid
ax.grid(zorder=0, linestyle='--', linewidth=0.5)

# Set x-axis label
ax.set_xlabel(data_labels[1])

# Set title
ax.set_title('Annual Number of Legal Cases Filed by Type')

# If the text length of the label is too long, rotate the labels or use wrap (uncomment the one you need)
# ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
# ax.set_xticklabels(ax.get_xticklabels(), wrap=True)

# Improve layout to accomodate long text
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/640.png', bbox_inches='tight')

# Clear the current figure after saving it
plt.clf()
