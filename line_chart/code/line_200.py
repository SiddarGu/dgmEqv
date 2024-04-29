
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.xticks([2015,2016,2017,2018,2019,2020])
plt.plot([2015,2016,2017,2018,2019,2020], [3000,3200,3400,3600,3800,4000], label='Retail sales (billion dollars)', color='red')
plt.plot([2015,2016,2017,2018,2019,2020], [200,400,600,800,1000,1200], label='E-commerce sales (billion dollars)', color='blue')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.title('Total retail sales and e-commerce sales in the US from 2015 to 2020', fontsize=12, wrap=True, pad=10)
plt.xlabel('Year')
plt.ylabel('Sales (billion dollars)')
plt.tight_layout()
plt.savefig(r'line chart/png/444.png', bbox_inches='tight')
plt.clf()