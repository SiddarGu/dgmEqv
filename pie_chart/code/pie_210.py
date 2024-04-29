
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Create figure
fig = plt.figure(figsize=(8,8))

# Plot pie chart
labels = ['Pop','Rock','Jazz','Electronic','Hip-Hop','Classical','Folk']
listeners = [30,20,15,15,10,5,5]
plt.pie(listeners, labels=labels, autopct='%.1f%%', textprops={'rotation': 90, 'wrap': True})

# Set title
plt.title("Popular Music Genres Listening Distribution in 2023", fontsize=20)

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('pie chart/png/436.png', dpi=300)

# Clear the current image state
plt.clf()