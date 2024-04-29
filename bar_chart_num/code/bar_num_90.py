
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Number_of_Companies = [180, 150, 170, 160]
GDP_billion = [2100, 2000, 2200, 1900]

fig = plt.figure(figsize=(15, 8))
ax = plt.subplot()
ax.set_title('Number of companies and GDP in four countries in 2021', fontsize=20)
ax.set_xticks(np.arange(len(Country)))
ax.set_xticklabels(Country, fontsize=15)
ax.bar(Country, Number_of_Companies, width=.3, bottom=GDP_billion, label='Number of Companies')
ax.bar(Country, GDP_billion, width=.3, label='GDP (billion)')
for i in range(len(Country)):
    ax.text(i, Number_of_Companies[i]/2+GDP_billion[i], Number_of_Companies[i], fontsize=15, ha='center', va='bottom', rotation=30, wrap=True)
    ax.text(i, GDP_billion[i]/2, GDP_billion[i], fontsize=15, ha='center', va='top', rotation=30, wrap=True)
ax.legend(fontsize=15)
plt.tight_layout()
plt.savefig('Bar Chart/png/616.png')
plt.clf()