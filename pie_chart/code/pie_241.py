
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Create figure 
fig = plt.figure(figsize=(7.5,7.5))

# Plot pie chart
segments = ['Processed Foods', 'Fresh Foods', 'Soft Drinks', 'Snack Foods', 'Dairy Products', 'Alcoholic Beverages']
percentage = [35,30,15,10,5,5]
plt.pie(percentage, labels=segments, autopct='%.2f%%', shadow=True, startangle=90, pctdistance=0.8, labeldistance=1.2)

# Set the title
plt.title('Global Food and Beverage Market Distribution in 2023', fontsize=11)

# Set xticks to prevent interpolation
plt.xticks(rotation=360)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save image
plt.savefig('pie chart/png/485.png', bbox_inches = 'tight')

# Clear the current image state
plt.clf()