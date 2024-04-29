
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

savings = [20,25,22,21]
debt = [40,50,45,42]
investment = [60,70,65,63]

country = ['USA','UK','Germany','France']

bar1 = ax.bar(country,savings,bottom=debt,label='Savings')
bar2 = ax.bar(country,debt,label='Debt')
bar3 = ax.bar(country,investment,bottom=[sum(x) for x in zip(debt, savings)],label='Investment')

for bar in bar1+bar2+bar3:
    h = bar.get_height()
    ax.annotate('{}'.format(h),
                xy=(bar.get_x() + bar.get_width() / 2, h/2),
                xytext=(0, 3),  
                textcoords="offset points",
                ha='center', va='bottom',rotation=90)

plt.xticks(country)
plt.legend()
plt.title('Financial data of four countries in 2021')
plt.tight_layout()
plt.savefig('bar_110.png')
plt.clf()