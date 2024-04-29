
import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))

browsers = ["Chrome", "Safari", "Firefox", "Edge", "Opera", "Other"]
market_share = [45, 25, 15, 5, 5, 5]

plt.pie(market_share, labels=browsers, autopct='%1.1f%%', textprops={'fontsize': 10, 'wrap':True, 'rotation': 30})
plt.title('Market Share of Web Browsers in the USA, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/446.png')
plt.xticks([])
plt.show()
plt.clf()