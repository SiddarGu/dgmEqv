

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Create figure and set figsize
fig, ax = plt.subplots(figsize=(10, 8))

# Set Data
Donations = ['Individuals', 'Foundations', 'Corporations', 'Government', 'Other']
Percentage = [45, 20, 15, 15, 5]

# Plot Pie Chart
ax.pie(Percentage, labels=Donations, autopct='%1.1f%%', radius=1.2, startangle=90, 
        textprops={'fontsize': 12}, labeldistance=1.2, pctdistance=0.5)

# Adjust text position
ax.set_title("Distribution of Donations to Nonprofit Organizations in the USA in 2023", 
             fontsize=16, wrap=True, y=1.15)

# Adjust text length
ax.legend(Donations, loc='center', bbox_to_anchor=(1.25, 0.2), fontsize=14, frameon=False)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/270.png')

# Clear the current image state
plt.clf()