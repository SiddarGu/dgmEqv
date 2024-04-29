import pandas as pd
import matplotlib.pyplot as plt

# Data extraction and transformation
data_labels = ['Hotel Star Rating', 'Number of Bookings (Thousands)']
line_labels = ['1-star', '2-star', '3-star', '4-star', '5-star']
data = [12, 35, 50, 45, 25]

# Create a DataFrame using the data
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Create a histogram
df.plot(kind='bar', ax=ax, color='skyblue', grid=True, legend=False)

# Set title and labels
ax.set_title('Hotel Bookings by Star Rating in Tourism Industry')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])

# Setting rotation for x-tick labels if necessary and wrapping text
ax.tick_params(axis='x', labelrotation=0, labelsize=10)
plt.setp(ax.get_xticklabels(), ha="center", rotation=45, wrap=True)

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/238.png')

# Clear the current figure state
plt.clf()
