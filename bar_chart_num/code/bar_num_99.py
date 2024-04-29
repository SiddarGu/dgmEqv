
import matplotlib.pyplot as plt
import numpy as np

# Data
Country = ['USA', 'UK', 'Germany', 'France']
Criminal_Cases = [150, 170, 160, 140]
Civil_Cases = [350, 400, 380, 370]

# Create figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

# Stacked bar chart
width = 0.4
x = np.arange(len(Country))
ax.bar(x, Criminal_Cases, width, label='Criminal Cases')
ax.bar(x, Civil_Cases, width, bottom=Criminal_Cases, label='Civil Cases')

# Label the bars
for i in range(len(Country)):
    ax.annotate('{}'.format(Criminal_Cases[i]),
                xy=(i, Criminal_Cases[i]),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', rotation=45)
    ax.annotate('{}'.format(Civil_Cases[i]),
                xy=(i, Criminal_Cases[i]+Civil_Cases[i]),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', rotation=45)

# Naming the x-axis
plt.xticks(x, Country, rotation=45)

# Add legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=2)

# Add title
ax.set_title('Number of criminal and civil cases in four countries in 2021')

# Resize the figure
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/88.png')

# Clear the current image state
plt.cla()