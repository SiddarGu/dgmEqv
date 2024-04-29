
import matplotlib.pyplot as plt
import numpy as np

# Setting figure size
plt.figure(figsize=(7,7))

# Generate data
genres = ['Pop', 'Hip-Hop', 'Rock', 'R&B', 'Country', 'Jazz', 'Classical', 'Other']
percentage = [25, 20, 15, 10, 10, 10, 5, 5]

# Plotting pie chart
ax = plt.subplot()
ax.pie(percentage, labels=genres, autopct='%1.1f%%', shadow=True, startangle=90, rotatelabels=True)

# Setting chart title
ax.set_title('Music Genre Popularity in the USA, 2023')

# Tidying up
plt.tight_layout()
plt.savefig('pie chart/png/282.png')
plt.clf()