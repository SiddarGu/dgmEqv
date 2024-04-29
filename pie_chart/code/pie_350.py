
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# Set data
genres = ["Painting","Sculpture","Music","Theater","Dance","Photography","Literature","Film"]
percentage = [25,15,20,15,10,10,10,5]

# Plot pie chart
ax.pie(percentage, labels=genres, autopct='%.2f%%', textprops={'fontsize': 12, 'color':'black'}, shadow=True, startangle=90, labeldistance=1.05, rotatelabels=True, pctdistance=1.02)

# Add title
ax.set_title('Distribution of Arts and Culture Genres in 2023', fontsize=14, pad=15)

# Tight layout
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/37.png')

# Clear figure
plt.clf()