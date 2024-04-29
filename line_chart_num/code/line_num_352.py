
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(8,6))
plt.plot(['KG','1','2','3','4','5','6','7'],[1000,1500,1800,1400,1600,1750,2200,2100],linestyle='dashed',marker='o',color='red')
plt.annotate('1000',xy=('KG',1000),xytext=(-20,-20),textcoords='offset points')
plt.annotate('1500',xy=('1',1500),xytext=(-20,-20),textcoords='offset points')
plt.annotate('1800',xy=('2',1800),xytext=(-20,-20),textcoords='offset points')
plt.annotate('1400',xy=('3',1400),xytext=(-20,-20),textcoords='offset points')
plt.annotate('1600',xy=('4',1600),xytext=(-20,-20),textcoords='offset points')
plt.annotate('1750',xy=('5',1750),xytext=(-20,-20),textcoords='offset points')
plt.annotate('2200',xy=('6',2200),xytext=(-20,-20),textcoords='offset points')
plt.annotate('2100',xy=('7',2100),xytext=(-20,-20),textcoords='offset points')
plt.title('Number of Students in Different Grades in a School')
plt.xticks(np.arange(8), ('KG', '1', '2', '3', '4', '5', '6', '7'), rotation=30)
plt.tight_layout()
plt.savefig('line chart/png/37.png')
plt.clf()