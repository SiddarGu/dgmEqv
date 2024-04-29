import matplotlib.pyplot as plt

# Define your data
categories = ['Tax Law', 'Environmental Law', 'Immigration Law', 'Constitutional Law', 'Intellectual Property Law']
data = [[12,36,60,84,120], [10,30,50,70,90], [15,45,75,100,125], [20,35,50,65,100], [8,24,40,54,64]]
outliers = [[], [150], [180], [5,140], [4,10]]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

# Create boxplot
bp = ax.boxplot(data, whis=1.5)

# Iterate through outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'x')

# Add labels and title
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.set_title('Sentence Length Distribution in Different Law Categories (2019-2022)')
ax.set_ylabel('Sentence Length (months)')
ax.grid(True)

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/179_202312310058.png')

# Clear current figure
plt.clf()
