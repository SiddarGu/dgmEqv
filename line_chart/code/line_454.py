
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 6))
plt.plot(['2009','2010','2011','2012','2013','2014','2015','2016'],
         [250000,320000,400000,450000,500000,550000,600000,650000],
         label='Average House Price (dollars)')
plt.plot(['2009','2010','2011','2012','2013','2014','2015','2016'],
         [3000,3500,4000,4500,5000,5500,6000,6500],
         label='Number of Houses Sold')

plt.title('Trend of Average House Price and Number of Houses Sold in the US from 2009 to 2016', fontsize=10)
plt.xlabel('Year', fontsize=8)
plt.ylabel('Price/Number of Houses Sold', fontsize=8)
plt.xticks(np.arange(8), ['2009','2010','2011','2012','2013','2014','2015','2016'], rotation=45)
plt.legend(loc='upper left', fontsize=8)
plt.grid(True, linestyle='--', color='gray', linewidth=0.5)
plt.tight_layout()
plt.savefig('line chart/png/146.png')
plt.clf()