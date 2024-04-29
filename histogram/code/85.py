import pandas as pd
import matplotlib.pyplot as plt

# Data
data_labels = ['Number of Bookings (Thousands)']
line_labels = ['Budget', 'Mid-Range', 'Premium', 'Luxury', 'Boutique']
data = [35, 50, 45, 25, 20]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create figure and subplot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Plot histogram
df.plot(kind='bar', ax=ax, color=['skyblue', 'orange', 'green', 'red', 'purple'])

# Set titles and labels
ax.set_title('Number of Hotel Bookings by Category in the Tourism Industry')
ax.set_xlabel('Hotel Category')
ax.set_ylabel('Number of Bookings (Thousands)')

# Rotate x-axis labels if too long
ax.set_xticklabels(line_labels, rotation=45, ha='right')

# Enable grid
ax.yaxis.grid(True)

# Prevent label overlap and ensure layout is tight
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/85.png', dpi=300)

# Clear the current figure's state
plt.clf()
