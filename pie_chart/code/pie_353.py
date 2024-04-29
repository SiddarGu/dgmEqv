

import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(7,7))

# Create list of sports and corresponding percentages
sports = ['Football', 'Basketball', 'Baseball', 'Hockey', 'Soccer', 'Tennis', 'Other']
percentages = [30, 20, 15, 10, 10, 10, 5]

# Plot pie chart
ax = fig.add_subplot()
ax.pie(percentages, labels = sports, autopct='%1.1f%%', shadow=True, startangle=90, wedgeprops={'linewidth': 2, 'edgecolor': "white"}, textprops={'wrap':True, 'rotation':45})

# Set title
ax.set_title('Popular Sports in North America, 2023')

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/528.png')

# Clear figure
plt.clf()