

import matplotlib.pyplot as plt
import pandas as pd

# import data
data = [['New York', 2.5, 4.5], 
        ['Los Angeles', 3.2, 3.9], 
        ['London', 2.8, 4.2], 
        ['Tokyo', 3.0, 5.0]]

# Create DataFrame
df = pd.DataFrame(data, columns =['City', 'Average Home Price(million)', 'Average Rent(thousand)']) 

# Create figure
fig = plt.figure(figsize=(10, 6))

# Plot bar chart
ax = fig.add_subplot(111)
ax.bar(df['City'], df['Average Home Price(million)'], width=0.2, bottom=df['Average Rent(thousand)'], color='b', label="Average Home Price(million)")
ax.bar(df['City'], df['Average Rent(thousand)'], width=0.2, color='r', label="Average Rent(thousand)")

# Add title
ax.set_title('Average home prices and rents in four major cities in 2021')

# Label each bar
for i in range(len(df)):
    ax.text(x = df['City'][i], y = df['Average Home Price(million)'][i] + df['Average Rent(thousand)'][i]/2, s = round(df['Average Home Price(million)'][i] + df['Average Rent(thousand)'][i], 1), size = 10, horizontalalignment='center', verticalalignment='center')

# Add legend
ax.legend(loc='upper right')

# Make sure text is not cut off
plt.tight_layout()

# save figure
plt.savefig('Bar Chart/png/527.png', dpi=300)

# Clear current image state
plt.clf()