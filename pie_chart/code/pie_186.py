

import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(8, 8))

# Create data
Education_Levels = ['Primary', 'Secondary', 'Tertiary', 'Vocational']
Percentage = [20, 30, 40, 10]

# Create plot
ax = fig.add_subplot()
ax.pie(Percentage, labels=Education_Levels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 14})
ax.axis('equal')

# Set plot title
plt.title("Education Level Distribution in the US, 2023", fontsize=18)

# Ensure labels are not overlapped
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/121.png', bbox_inches='tight')

# Clear current image state
plt.clf()