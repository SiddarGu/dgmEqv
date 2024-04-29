
import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))
plt.pie(
    [35,25,15,10,10,5], 
    labels=['Electronics','Automobiles','Aerospace','Furniture','Clothing','Food and Beverage'], 
    autopct='%1.1f%%',
    textprops={'fontsize': 10, 'rotation': 30},
    startangle=90,
    shadow=True)
plt.title('Manufacturing Production Distribution in the World, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/304.png')

plt.clf()