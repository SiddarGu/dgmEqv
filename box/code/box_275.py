import matplotlib.pyplot as plt

# Data restructuring
charity_names = ['Charity A', 'Charity B', 'Charity C', 'Charity D', 'Charity E']
data = [[10, 50, 100, 150, 200], [20, 75, 125, 175, 225], [15, 85, 130, 180, 250], [30, 90, 140, 200, 270], [25, 80, 120, 175, 230]]
outliers = [[], [8, 300], [5, 12, 350], [400], [5, 10, 500]]

# Create figure and add subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Boxplot parameters
boxplot_params = dict(vert=False, patch_artist=True, meanline=False, showmeans=True, showcaps=True, 
                      showbox=True, showfliers=False, notch=False)

# Boxplot
bp = ax.boxplot(data, **boxplot_params, whis=1.5)

# Iterate over outlier lists
for i, outlier in enumerate(outliers):
    if outlier:
        y = [i + 1] * len(outlier)
        ax.plot(outlier, y, 'k+', mew=2)

# Style
ax.set_yticklabels(charity_names)
ax.set_xlabel('Donation Amount (USD)')
ax.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.7)
plt.title('Summary of Donations Distribution in Charity and Nonprofit Organizations in 2023')

# Save figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/249_202312310058.png')

# Clear current figure
plt.clf()
