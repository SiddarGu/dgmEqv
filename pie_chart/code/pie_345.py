

import matplotlib.pyplot as plt

labels = ['Mutual Funds', 'Real Estate', 'Bonds', 'Stocks', 'Commodities']
percentages = [30, 20, 25, 15, 10]

fig = plt.figure(figsize=(8, 8))
plt.title('Popular Investment Types in the US in 2023')
plt.pie(percentages, labels=labels, autopct='%1.1f%%', textprops={'fontsize':14, 'wrap':True, 'rotation':90})
plt.tight_layout()
plt.xticks(rotation=90)

plt.savefig('pie chart/png/371.png')
plt.close(fig)