
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))

city=["Los Angeles","New York","San Francisco","Chicago"]
price=[4.8,6.2,5.5,4.3]
sales=[300,400,350,250]

barWidth=0.3
r1=np.arange(len(price))
r2=[x+barWidth for x in r1]

plt.bar(r1,price,width=barWidth,label='Average Home Price (million)', color='#1F77B4')
plt.bar(r2,sales,width=barWidth,label='Homes Sold', color='#FF7F0E')

plt.xlabel('City')
plt.xticks([r+barWidth/2 for r in range(len(price))], city)

plt.title('Average Home Price and Homes Sold in Four Major US Cities in 2021')
plt.legend()
plt.tight_layout()

for i, v in enumerate(price):
    plt.text(i-0.1, v+0.2, str(v), color='black', fontsize=12)
for i, v in enumerate(sales):
    plt.text(i+barWidth-0.1, v+0.2, str(v), color='black', fontsize=12)

plt.savefig('Bar Chart/png/250.png')
plt.clf()