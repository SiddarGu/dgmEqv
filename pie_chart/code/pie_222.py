


import matplotlib.pyplot as plt

# Create figure before plotting
fig=plt.figure(figsize=(6,6))

# Plot the data with the type of pie chart
labels = ['Cereals','Vegetables','Fruits','Legumes','Nuts','Oils','Spices','Dairy','Other']
sizes = [35,20,15,10,5,5,5,5,5]
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# Automatically resize the image by tight_layout()
fig.tight_layout()

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, textprops={'fontsize': 8})

# Set the title of the figure 
plt.title('Distribution of Agricultural Crops in the USA, 2023')

# Rotate the x-axis labels to prevent them from overlapping
plt.xticks(rotation=-40)

# Save the figure
plt.savefig('pie chart/png/28.png')

# Clear the current image state at the end of the code 
plt.clf()