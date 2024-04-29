import matplotlib.pyplot as plt

# Restructured data
data = [['Primary School', 45, 70, 80, 90, 100], ['Secondary School', 50, 65, 85, 95, 110], 
        ['High School', 60, 70, 80, 90, 120], ['Undergraduate', 50, 75, 85, 95, 120], 
        ['Postgraduate', 70, 80, 90, 100, 110]]
outliers = [['Primary School', [130]], ['Secondary School', [40, 140]], ['High School', [30, 150]], 
            ['Undergraduate', [160]], ['Postgraduate', [35, 145]]]

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
bp = ax.boxplot([d[1:] for d in data], vert=False, patch_artist=True, whis=1.5)

ax.set_title('Academic Scores Distribution by School Level in 2021')
ax.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.5)
ax.set_axisbelow(True)
ax.set_xlabel('Scores')
ax.set_ylabel('School Level')

ax.set_yticklabels([d[0] for d in data], rotation=45)

for i, out in enumerate(outliers):
    y = [i + 1] * len(out[1])
    ax.plot(out[1], y, 'ro')
    
# Remove axes on the top and right
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.tight_layout()
fig.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/54_202312270030.png')
plt.clf()
