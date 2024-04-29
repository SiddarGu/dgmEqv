import matplotlib.pyplot as plt

# structuring the data
positions = ["Entry-Level", "Mid-Level", "Senior-Level", "Management", "Executive"]
salaries = [[30000, 37500, 40000, 42500, 50000], 
            [60000, 65000, 70000, 75000, 80000], 
            [90000, 97500, 105000, 112500, 120000], 
            [120000, 125000, 130000, 135000, 140000], 
            [150000, 200000, 250000, 300000, 350000]]
outliers = [[], [90000], [75000, 130000], [], [100000]]

# create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# creating box plot
ax.boxplot(salaries, whis=1.5)

# plotting outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'rx')

# setting labels and title
ax.set_xticklabels(positions, rotation=30)
ax.set_ylabel('Salary ($)')
ax.set_title('Salary Distribution Across Employee Positions in a Corporation (2021)')

# improving layout and saving figure
fig.tight_layout()
plt.grid(True)
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/191_202312310058.png')

# clear current figure
plt.clf()
