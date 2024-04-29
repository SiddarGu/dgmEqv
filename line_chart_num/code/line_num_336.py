
import matplotlib.pyplot as plt
plt.figure(figsize=(18,8))
ax = plt.subplot()

year = [2001, 2002, 2003, 2004]
wheat = [500, 600, 650, 700]
rice = [700, 750, 800, 850]
maize = [900, 950, 1000, 1100]
barley = [1000, 1100, 1200, 1300]

ax.plot(year, wheat, label="Wheat Yield(tons)")
ax.plot(year, rice, label="Rice Yield(tons)")
ax.plot(year, maize, label="Maize Yield(tons)")
ax.plot(year, barley, label="Barley Yield(tons)")

ax.set_xticks(year)
ax.set_title("Yields of Major Crops in the US in the last 20 Years")
ax.legend(loc="best")

for a,b in zip(year,wheat): 
    ax.annotate('{}'.format(b),xy=(a,b), textcoords='offset points')
for a,b in zip(year,rice): 
    ax.annotate('{}'.format(b),xy=(a,b), textcoords='offset points')
for a,b in zip(year,maize): 
    ax.annotate('{}'.format(b),xy=(a,b), textcoords='offset points')
for a,b in zip(year,barley): 
    ax.annotate('{}'.format(b),xy=(a,b), textcoords='offset points')

plt.tight_layout()
plt.savefig('line chart/png/599.png')
plt.clf()