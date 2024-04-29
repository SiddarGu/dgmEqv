
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
attractions = ['Historical Sites','Natural Wonders','Museums','Theme Parks','Outdoor Activities','Shopping']
percentage = [30,25,15,15,10,5]
explode = [0.1,0,0,0,0,0]
plt.pie(percentage, explode=explode, labels=attractions, autopct='%1.1f%%',shadow=True, startangle=90)
plt.title('Popular Tourist Attractions in the USA, 2023', fontsize=20, wrap=True)
plt.axis('equal')
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig("pie chart/png/390.png")
plt.clf()