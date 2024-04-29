import matplotlib.pyplot as plt
import pandas as pd

# Prepare Data
data = [['Twitter', 1, 2, 3.5, 4.5, 7, [20]],
        ['Instagram', 2, 4, 7, 10, 15, [20]],
        ['Facebook', 5, 8, 12, 17, 25, [30]],
        ['YouTube', 1.5, 4, 6, 8.5, 12, [15]],
        ['TikTok', 2, 3.5, 6, 8.5, 11, [20]]]

df = pd.DataFrame(data, columns=['Social Network', 'Min Users (Million)', 'Q1 Users (Million)', 
                                 'Median Users (Million)', 'Q3 Users (Million)', 'Max Users (Million)', 
                                 'Outlier Users (Million)'])

# Prepare boxplot data and outliers
boxplot_data = df.iloc[:, 1:6].values.T  # Transpose to match boxplot format
outliers = df['Outlier Users (Million)'].tolist()

# Draw Box Plot
fig = plt.figure(figsize=(15, 7))
ax = fig.add_subplot(111)
ax.set_title('User Distribution in Popular Social Networks in 2021')

# Create boxplot
bp = ax.boxplot(boxplot_data, positions=range(1, len(df) + 1))

# Add outliers to the plot
for i, outlier in enumerate(outliers):
    if outlier:
        ax.scatter([i + 1] * len(outlier), outlier, color='red', marker='o')

ax.set_xticklabels(df['Social Network'], rotation=45, fontsize=11, wrap=True)

#Resize Image
plt.tight_layout()

#Save Image
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/2.png')

#Clear Image State
plt.clf()