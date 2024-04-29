
import matplotlib.pyplot as plt

plt.figure(figsize=(7,7))
plt.subplot()

labels = ['Automotive', 'Electronics', 'Food and Beverage', 'Apparel', 'Pharmaceuticals', 'Aerospace', 'Construction', 'Other']
sizes = [20, 15, 15, 10, 10, 10, 10, 20]

plt.pie(sizes, labels=labels, autopct='%.2f%%', textprops={'fontsize': 12}, pctdistance=0.8, labeldistance=1.1, 
        rotatelabels=True, startangle=90, wedgeprops={'linewidth':2, 'edgecolor':'white'})

plt.title('Manufacturing Industry Distribution in the USA, 2023', fontsize=14)

plt.tight_layout()
plt.savefig('pie chart/png/105.png')
plt.clf()