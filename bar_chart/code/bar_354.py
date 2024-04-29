
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.bar(x=['2020','2021','2022','2023'],height=[21000,22000,23500,25000],width=0.5,
label='GDP (billion USD)',align='center',color='b',bottom=0)
ax.bar(x=['2020','2021','2022','2023'],height=[2.4,3.2,2.7,3.5],width=0.5,
label='Inflation Rate',align='center',color='r',bottom=0)
plt.xticks(rotation=90)
plt.title('GDP and inflation rate in four consecutive years - 2020 to 2023')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('bar chart/png/303.png')
plt.clf()