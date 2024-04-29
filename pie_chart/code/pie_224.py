
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

plt.figure(figsize=(8,8))
ax = plt.subplot(111)

products = ['Fruits','Dairy','Grains','Meat and Seafood','Vegetables','Oils and Fats','Nuts and Seeds']
percentage = [25,20,20,15,10,10,10]

ax.pie(percentage, labels=products, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10, 'wrap':True, 'rotation':45})

plt.title('Distribution of Food and Beverage Products in the USA, 2023')

ax.xaxis.set_major_locator(ticker.NullLocator())
ax.yaxis.set_major_locator(ticker.NullLocator())

plt.tight_layout()
plt.savefig('pie chart/png/102.png')
plt.clf()