
import matplotlib.pyplot as plt
import matplotlib as mpl

# Create figure before plotting
plt.figure(figsize=(10,8))

# Define data
types = ['Video Games', 'Streaming Services', 'Social Media', 'Apps', 'Online Shopping']
percentages = [25, 20, 30, 15, 10]

# Plot pie chart
plt.pie(percentages, labels=types, autopct='%1.1f%%',
        shadow=True, startangle=90, rotatelabels=True,
        counterclock=False, textprops={'wrap':True})

# Set title
plt.title('Distribution of Technology Usage in the US, 2023')

# Resize image
plt.tight_layout()

# Save the image
plt.savefig('pie chart/png/465.png')

# Clear the current image state
plt.clf()