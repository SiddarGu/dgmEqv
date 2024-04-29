
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))
ax = plt.subplot()
ax.bar(x=['January','February', 'March', 'April'], height=[100,110,120,130], label='Retail Sales', color='b')
ax.bar(x=['January','February', 'March', 'April'], height=[200,220,240,260], bottom=[100,110,120,130], label='E-commerce Sales', color='r', alpha=0.5)
ax.set_title('Comparison of Retail and E-commerce Sales in 2021')
ax.set_ylabel('Sales (billion)')
ax.legend()
plt.xticks(['January','February', 'March', 'April'], rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/492.png')
plt.clf()