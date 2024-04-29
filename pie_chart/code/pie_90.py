
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,10))

types = ['Air Travel', 'Accommodation', 'Food and Beverages', 'Transportation', 'Entertainment']
percentage = [40, 20, 25, 8, 7]

# Create the pie chart
ax1 = fig.add_subplot(111)
ax1.pie(percentage, labels=types, autopct='%.2f%%', shadow=True, startangle=90, textprops={'fontsize': 12})

# Create a title
ax1.set_title('Distribution of Tourism Expenditures in the USA, 2023', fontsize=14)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig('pie chart/png/68.png')

# Clear the current image state
plt.clf()