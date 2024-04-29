
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111)

# Plotting of pie chart
data = [25, 15, 13, 10, 9, 7, 6, 4, 4, 17]
labels = ['United States', 'Spain', 'France', 'China', 'Germany', 'Italy', 'United Kingdom', 'Mexico', 'Canada', 'Other']
ax.pie(data, labels=labels, autopct='%.2f%%', shadow=True, startangle=90, textprops={'fontsize': 14})

# Configure the figure
plt.title('Global Tourism Share in 2023', fontsize=18)
plt.tight_layout()
plt.xticks(rotation=15, fontsize=14)

# Save figure
plt.savefig('pie chart/png/378.png')

# Clear the current image state
plt.clf()