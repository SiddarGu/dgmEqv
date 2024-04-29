
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax=plt.subplot()
plt.bar(x=['Paintings','Sculptures','Photographs','Drawings'],height=[100000,40000,50000,30000],width=0.8,bottom=0,align='center',color=['#A8C1D8','#FFD9B6','#F5C89C','#A3A2A2'])
plt.bar(x=['Paintings','Sculptures','Photographs','Drawings'],height=[800,300,500,400],width=0.8,bottom=0,align='center',color=['#A8C1D8','#FFD9B6','#F5C89C','#A3A2A2'],alpha=0.5)
plt.xticks(rotation=45,ha='right')
plt.title('Revenue from artworks and number of customers in 2021')
plt.xlabel('Types')
plt.ylabel('Sales(USD)')
ax.legend(labels=['Sales','Number of customers'],loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/546.png')
plt.clf()