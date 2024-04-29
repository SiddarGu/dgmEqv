
import matplotlib.pyplot as plt
import numpy as np

retail_type = ['Grocery Stores','Online Shopping','Department Stores','Discount Stores','Specialty Stores']
percentage = [30,25,20,15,10]

plt.figure(figsize=(8, 8))
plt.title("Retail Shopping Trends in the USA, 2023")

pie_chart = plt.pie(percentage,labels=retail_type,autopct="%1.1f%%",textprops={'fontsize': 12})

plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=-45)

plt.savefig('pie chart/png/369.png')
plt.clf()