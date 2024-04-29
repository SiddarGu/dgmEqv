import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

# Raw data
data = '''Event Type,Min Attendance,Q1 Attendance,Median Attendance,Q3 Attendance,Max Attendance,Outlier Attendance
Music Concert,100,250,500,750,1000,
Art Exhibition,50,150,350,600,1000,4000
Theater Performance,80,200,400,700,1200,"20,35"
Film Festival,150,400,600,880,1200,"500,2000"
Book Fair,100,300,550,750,1050,80'''

# Convert raw data into dataframe
df = pd.read_csv(StringIO(data))

# Create figure and axis
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

# Prepare data for boxplot
boxplot_data = [df[col].dropna().tolist() for col in df.columns[1:6]]

# Parse outliers from strings to lists of integers
outliers = df['Outlier Attendance'].apply(lambda x: [int(i) for i in str(x).split(',') if i.isdigit()])

# Plot boxplot
bp = ax.boxplot(boxplot_data, whis=1.5, patch_artist=True)

# Colors for each boxplot
colors = ['lightblue', 'lightgreen', 'lightyellow', 'pink', 'lightgrey']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

# Plot outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, 'ro')

# Set labels and title
ax.set_xticklabels(df['Event Type'], rotation=30, ha='right')
ax.set_title('Festival Attendance Distribution in Arts and Culture Events in 2021')
ax.set_ylabel('Attendance')

# Show grid
ax.yaxis.grid(True)

# Save and clear figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/194_202312310058.png')
plt.clf()
