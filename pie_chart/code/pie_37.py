
import matplotlib.pyplot as plt

# Set figure size
plt.figure(figsize=(8,6))

# Create a subplot
ax = plt.subplot()

#Set title
ax.set_title('Energy Sources Distribution in the US, 2023')

# Set data
sources = ['Fossil Fuels', 'Nuclear', 'Non-Renewable', 'Renewable'] 
percentage = [45, 20, 15, 20]

# Plot pie chart
plt.pie(percentage, labels=sources, autopct='%1.1f%%', startangle=180, textprops={'fontsize': 14}, shadow=True, rotatelabels=True)

# Set legend
plt.legend(loc='best', fontsize='large')

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig('pie chart/png/153.png')

# Clear the current image state
plt.clf()