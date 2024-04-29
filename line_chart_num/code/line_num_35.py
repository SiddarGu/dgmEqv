
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
ax = plt.subplot()

year=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
price=[2.4, 2.7, 3.2, 3.6, 3.8, 4.1, 4.4, 4.7]
rent=[1.2, 1.5, 1.3, 1.4, 1.6, 1.7, 1.9, 2.1]

ax.plot(year, price, label="Average House Price (million dollars)", color="red", marker="o")
ax.plot(year, rent, label="Average Rent (thousand dollars)", color="blue", marker="o")

ax.set_xlabel("Year")
ax.set_ylabel("Price (million/thousand dollars)")
ax.set_xticks(year)
plt.title("Average House Price and Rent in the United States from 2010 to 2017")
ax.legend(loc="upper left")

for a,b in zip(year, price):
    ax.annotate('{}'.format(b), xy=(a,b), xytext=(a-0.2,b+0.1))
for c,d in zip(year, rent):
    ax.annotate('{}'.format(d), xy=(c,d), xytext=(c-0.2,d+0.1))
    
plt.tight_layout()
plt.savefig('line chart/png/57.png')
plt.clf()