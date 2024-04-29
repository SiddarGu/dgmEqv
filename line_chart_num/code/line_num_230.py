
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create figure before plotting
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

# Create DataFrame
df = pd.DataFrame({'Year': [2010, 2011, 2012, 2013, 2014],
                   'Number of Users (million)': [100, 150, 200, 300, 400],
                   'Number of Posts (million)': [50, 80, 100, 150, 200],
                   'Number of Ads (million)': [30, 45, 60, 90, 120]})

# Plot line chart
ax.plot(df['Year'], df['Number of Users (million)'], label='Number of Users (million)', color='green', linewidth=3)
ax.plot(df['Year'], df['Number of Posts (million)'], label='Number of Posts (million)', color='blue', linewidth=3)
ax.plot(df['Year'], df['Number of Ads (million)'], label='Number of Ads (million)', color='red', linewidth=3)

# Set ticks
ax.set_xticks(np.arange(2010, 2015, 1))

# Add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=5)

# Add title
ax.set_title('Global Online Social Networking Trends from 2010 to 2014')

# Annotate
x = df['Year']
y1 = df['Number of Users (million)']
y2 = df['Number of Posts (million)']
y3 = df['Number of Ads (million)']

for i in range(len(x)):
    label1 = '(' + str(x[i]) + ',' + str(y1[i]) + ')'
    label2 = '(' + str(x[i]) + ',' + str(y2[i]) + ')'
    label3 = '(' + str(x[i]) + ',' + str(y3[i]) + ')'
    ax.annotate(label1, xy=(x[i], y1[i]), fontsize=10, ha='center')
    ax.annotate(label2, xy=(x[i], y2[i]), fontsize=10, ha='center')
    ax.annotate(label3, xy=(x[i], y3[i]), fontsize=10, ha='center')

# Automatically resize
fig.tight_layout()

# Save figure
plt.savefig('line chart/png/327.png')

# Clear current image state
plt.clf()