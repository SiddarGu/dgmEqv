
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

years = ['2001', '2002', '2003', '2004']
painting_A = [500, 550, 400, 600]
painting_B = [300, 350, 500, 450]
painting_C = [400, 450, 300, 350]
sculpture_A = [100, 150, 200, 250]

ax.plot(years, painting_A, label='Painting A')
ax.plot(years, painting_B, label='Painting B')
ax.plot(years, painting_C, label='Painting C')
ax.plot(years, sculpture_A, label='Sculpture A')

ax.xaxis.set_major_locator(ticker.IndexLocator(base=1, offset=0))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(years))
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Value', fontsize=14)
ax.set_title('Value of Arts in Four Categories from 2001 to 2004', fontsize=16)
ax.legend(loc='upper left')
ax.grid(axis='y')

for x, y in zip(years, painting_A):
    label = "{:.0f}".format(y)
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=14)

for x, y in zip(years, painting_B):
    label = "{:.0f}".format(y)
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=14)

for x, y in zip(years, painting_C):
    label = "{:.0f}".format(y)
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=14)

for x, y in zip(years, sculpture_A):
    label = "{:.0f}".format(y)
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=14)

plt.tight_layout()
plt.savefig('line chart/png/452.png')
plt.clf()