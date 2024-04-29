
import matplotlib.pyplot as plt

labels = ["Equity", "Fixed Income", "Commodities", "Real Estate", "Cash"]
sizes = [35, 25, 15, 15, 10]

fig = plt.figure(figsize=(8, 8)) 
ax = fig.add_subplot()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 14, 'wrap': True, 'rotation': 80})
ax.set_title("Distribution of Investment Assets in 2023")
plt.tight_layout()
plt.savefig('pie chart/png/420.png')
plt.clf()