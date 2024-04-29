
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

investment = ["Mutual Funds","Stocks","Bonds","Commodities","Real Estate","Cash"]
percentage = [25,30,15,15,10,5]

ax.pie(percentage, labels=investment, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14, 'wrap': True}, counterclock=False)
ax.set_title("Popular Investment Types in the USA, 2023")

plt.tight_layout()
plt.savefig("pie chart/png/88.png")
plt.clf()