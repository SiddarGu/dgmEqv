
import matplotlib.pyplot as plt
import numpy as np

year=np.array([2001, 2002, 2003, 2004])
income_tax_rate=np.array([25,30,35,40])
corporate_tax_rate=np.array([15,20,25,30])

plt.figure(figsize=(15, 8))
plt.plot(year, income_tax_rate, label='Income Tax Rate', linewidth=2)
plt.plot(year, corporate_tax_rate, label='Corporate Tax Rate', linewidth=2)
plt.xlabel('Year')
plt.ylabel('Tax Rates (%)')
plt.title('Tax Rates Changes in the U.S. from 2001 to 2004')
plt.xticks(year,year,rotation=20,fontsize=12)
plt.legend(prop={'size': 15}, loc='best')
plt.tight_layout()
plt.savefig('line chart/png/439.png')
plt.clf()