
import matplotlib.pyplot as plt

year = [2011, 2012, 2013, 2014, 2015]
productionA = [100, 120, 130, 140, 180]
productionB = [200, 160, 210, 220, 240]
productionC = [150, 170, 150, 190, 210]

plt.figure(figsize=(10,7))
plt.plot(year, productionA, label='Production A (million units)', linewidth=2)
plt.plot(year, productionB, label='Production B (million units)', linewidth=2)
plt.plot(year, productionC, label='Production C (million units)', linewidth=2)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Units (million)', fontsize=12)
plt.xticks(year, rotation=45)
plt.title('Production of three categories of products in the manufacturing industry from 2011 to 2015', fontsize=14)
plt.legend(loc="best")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('line chart/png/380.png')
plt.clf()