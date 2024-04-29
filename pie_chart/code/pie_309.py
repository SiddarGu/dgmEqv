

import matplotlib.pyplot as plt

# Create figure 
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()

# Pie chart
products = ["Automobiles", "Electronics", "Machinery", "Textiles", "Food and Beverage", "Chemicals", "Other"]
percentages = [25, 20, 20, 15, 10, 10, 10]

ax.pie(percentages, labels=products, autopct='%1.1f%%', pctdistance=0.8, textprops={'fontsize': 14})
ax.set_title("Distribution of Manufacturing Production in the USA, 2023", fontsize=16)

# Tight layout and save
plt.tight_layout()
plt.savefig("pie chart/png/10.png")

# Clear the current image state
plt.clf()