import matplotlib.pyplot as plt
import ast

# Correctly parsing the outlier data using a different approach
data_str = "McTavish's,3,8,15,22,28,[35,40]; Bella Italia,6,12,20,25,32,[38,45]; Curry House,1,5,10,15,25,[]; Eat Evergreen,2,10,20,30,40,[50,60]; Dine & Wine,15,20,30,35,45,[65,70]"
data = [i.split(",") for i in data_str.split("; ")]

# Extract labels and data
labels = [i[0] for i in data]
data_values = [[int(j) for j in i[1:6]] for i in data]

# Manually parse outliers
fliers_data = []
for i in data:
    if i[-1] == '[]':
        fliers_data.append([])
    else:
        outliers = i[-1].strip('[]').split(',')
        fliers_data.append([int(x) for x in outliers])

# Create figure and axes
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Boxplot with custom settings
bp = ax.boxplot(data_values, whis=1.5, patch_artist=True, medianprops={'linewidth': 2})

# Colors for each boxplot
colors = ['lightblue', 'lightgreen', 'pink', 'yellow', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, flier in enumerate(fliers_data):
    if flier:
        ax.plot([i + 1] * len(flier), flier, 'k.')

# Grid and labels
ax.yaxis.grid(True)
ax.set_xticklabels(labels, rotation=45, ha="right")
plt.ylabel('Meal Price (USD)')
plt.title('Restaurant Meal Price Distribution in the Food and Beverage Industry')

# Show plot
plt.tight_layout()

fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/223_202312310058.png', bbox_inches='tight')
plt.close(fig)
