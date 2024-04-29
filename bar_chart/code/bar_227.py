

import matplotlib.pyplot as plt

Country=['USA','UK','Germany','France']
Restaurants=[40000,30000,20000,25000]
Fast_Food_Chains=[7000,6000,5000,5500]
Delivery_Service=[35000,33000,30000,32000]

plt.figure(figsize=(10,6))
ax=plt.subplot()
ax.bar(Country,Restaurants,label='Restaurants',width=0.3,color='blue')
ax.bar(Country,Fast_Food_Chains,bottom=Restaurants,label='Fast Food Chains',width=0.3,color='orange')
ax.bar(Country,Delivery_Service,bottom=[a+b for a,b in zip(Restaurants,Fast_Food_Chains)],label='Delivery Service',width=0.3,color='green')
plt.xticks(Country)
plt.title('Number of food outlets and delivery services in four countries in 2021')
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/105.png')
plt.clf()