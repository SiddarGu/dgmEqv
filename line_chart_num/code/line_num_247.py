
import matplotlib.pyplot as plt
import numpy as np

data = [[2001,30,35,10,20],
        [2002,28,34,12,18],
        [2003,27,33,13,17],
        [2004,25,32,15,15]]

years = np.array([data[i][0] for i in range(len(data))])
income_tax_rates = np.array([data[i][1] for i in range(len(data))])
corporate_tax_rates = np.array([data[i][2] for i in range(len(data))])
capital_gains_tax_rates = np.array([data[i][3] for i in range(len(data))])
dividend_tax_rates = np.array([data[i][4] for i in range(len(data))])

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.plot(years, income_tax_rates, label='Income Tax Rate', color='#0767c8', marker='o')
ax.plot(years, corporate_tax_rates, label='Corporate Tax Rate', color='#fdd400', marker='o')
ax.plot(years, capital_gains_tax_rates, label='Capital Gains Tax Rate', color='#07c867', marker='o')
ax.plot(years, dividend_tax_rates, label='Dividend Tax Rate', color='#ff5900', marker='o')

for i in range(len(data)):
    ax.annotate(str(data[i][1])+'%', (years[i], income_tax_rates[i]), rotation=45, ha='center', va='bottom', fontsize=10)
    ax.annotate(str(data[i][2])+'%', (years[i], corporate_tax_rates[i]), rotation=45, ha='center', va='bottom', fontsize=10)
    ax.annotate(str(data[i][3])+'%', (years[i], capital_gains_tax_rates[i]), rotation=45, ha='center', va='bottom', fontsize=10)
    ax.annotate(str(data[i][4])+'%', (years[i], dividend_tax_rates[i]), rotation=45, ha='center', va='bottom', fontsize=10)

plt.xticks(np.arange(2001, 2005, 1))
plt.title('Tax Rate Changes in the US from 2001 to 2004')
plt.xlabel('Years')
plt.ylabel('Tax Rates (%)')
plt.legend(loc='best')

plt.grid(linestyle='--')
plt.tight_layout()
plt.savefig('line chart/png/591.png')
plt.clf()