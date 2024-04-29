
import matplotlib.pyplot as plt

Country =['USA','UK','Germany','France'] 
Manufacturing_Cost =[10,15,12,11] 
Retail_Cost =[20,30,25,22] 

fig = plt.figure(figsize=(9,5))
ax = fig.add_subplot()
ax.bar(Country,Manufacturing_Cost,bottom=Retail_Cost,label='Manufacturing Cost',width=0.4,color='#a9a9a9')
ax.bar(Country,Retail_Cost,label='Retail Cost',width=0.4,color='#000000')
ax.set_title('Manufacturing and Retail Costs in four countries in 2021')
plt.xticks(Country,rotation=45)
ax.set_ylabel('Cost($)')
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/21.png')
plt.clf()