import matplotlib.pyplot as plt

# pre-parsed data 
categories = ['Restaurant A','Restaurant B','Restaurant C','Restaurant D','Restaurant E']
data = [[5,9,12,15,20], [6,10,14,18,22], [4,8,11,17,21], [7,11,15,19,23], [6,9,13,17,21]]
outliers = [[], [1,25], [27], [2,28], [4,29]]

# Create figure before plotting
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Plot the data with the type of box plot
bp = ax.boxplot(data,whis=1.5)
plt.setp(bp['medians'], color='red') # Set color of medians
plt.setp(bp['boxes'], color='black') # Set color of boxes
plt.setp(bp['caps'], color='blue') # Set color of caps
for i, outlier in enumerate(outliers):
    if outlier: # only if there are outliers for that category
        ax.plot([i + 1] * len(outlier), outlier, "ro")

ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set(title='Order Time Distribution in Food and Beverage Restaurants (2021)', ylabel='Order Time (Minutes)')
plt.xticks([1, 2, 3, 4, 5], categories, rotation=45, ha='right')  # x-axis labels

# Tight layout
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/163_202312310058.png')

# Clear the current image state
plt.clf()
