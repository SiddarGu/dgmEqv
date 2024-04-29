
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

plt.figure(figsize=(8,8))
labels = ['Grains','Fruits and Vegetables','Oilseeds','Dairy','Livestock','Other']
values = [30,25,15,10,15,5]
explode = [0.1,0,0,0,0,0]

plt.pie(values, labels=labels, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 12})
plt.title('Distribution of Agricultural Commodities in the United States, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/464.png')

plt.clf()