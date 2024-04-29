

import matplotlib.pyplot as plt

# Create data
Food_Groups = ['Dairy','Fruit','Vegetables','Meat','Grains','Fats and Oils','Sugars and Sweets']
Percentage = [18,20,25,15,14,6,2]

# Create figure
fig = plt.figure(figsize=(10,5))

# Plot
ax = fig.add_subplot()
ax.pie(Percentage, labels=Food_Groups, autopct='%1.1f%%', startangle=90, rotatelabels=True, textprops={'wrap':True})

# Title
ax.set_title('Food Distribution in the USA, 2023')

# Save figure
fig.savefig('pie chart/png/115.png')

# Clear figure
plt.clf()