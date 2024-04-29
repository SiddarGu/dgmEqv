
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
ax = plt.subplot()

x_labels = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007']

plt.plot(x_labels, [200, 210, 220, 230, 250, 270, 290, 310], label='Average Home Price (thousands of dollars)')
plt.plot(x_labels, [100, 105, 110, 115, 120, 125, 130, 135], label='Average Rental Price (thousands of dollars)')

ax.set_title('US Median Home and Rental Prices from 2000 to 2007')
ax.set_xlabel('Year')
ax.set_ylabel('Price (thousands of dollars)')
ax.legend()

for x, y1, y2 in zip(x_labels, [200, 210, 220, 230, 250, 270, 290, 310], [100, 105, 110, 115, 120, 125, 130, 135]):
    ax.annotate(f"({x}, {y1}, {y2})", (x, y1))

plt.xticks(x_labels)
plt.tight_layout()
plt.savefig('line chart/png/383.png')

plt.clf()