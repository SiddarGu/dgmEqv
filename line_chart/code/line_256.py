
import matplotlib.pyplot as plt
import numpy as np

data = [['US', 500, 34], ['Canada', 100, 20], ['UK', 750, 48], ['Australia', 200, 16], ['India', 300, 25]]

country = [x[0] for x in data]
donations = [x[1] for x in data]
donors = [x[2] for x in data]

fig = plt.figure(figsize=(14, 8))
ax1 = fig.add_subplot(111)
ax1.plot(country, donations, 'b-', label='Donations in Dollars')
ax1.plot(country, donors, 'g-', label='Number of Donors')

ax1.set_title('Global Donations to Charitable Causes in 2021')
ax1.set_xticks(country)
ax1.set_xticklabels(country, rotation=45, wrap=True)

ax1.legend(loc='best')

plt.tight_layout()
plt.savefig('line chart/png/520.png')
plt.close()